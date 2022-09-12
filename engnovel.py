import numbers
import requests
from lxml import html
import re
import reqtest as req
judul = input("cari: ")
webLnk = ('https://engnovel.com/?s='+judul)

# path list:
LinkPath = '//*[@id="truyen-slide"]/div[1]/div/div[1]/div/div/div/div[1]/div[2]/a/@href'
TitlePath = '//*[@id="truyen"]/div[1]/div/div[1]/div/div[3]/h3'
RatePath = '/html/body/div[1]/div[3]/div[1]/div/div[1]/div/div[3]/div[1]'
DescPath = '//*[@id="truyen"]/div[1]/div/div[1]/div/div[3]/div[2]'
LastetChap = '//*[@id="new-chapter"]/div[2]/div/ul/li[1]/a/@href'

def chapterGetter(chapter):
    fn = re.findall("[0-9]",str(chapter))
    fr = list(map(int, fn))
    s = [str(integer) for integer in fr]
    a_string = "".join(s)
    res = int(a_string)
    return res
def linkGetter():
    resp = requests.get(webLnk)
    byte_data = resp.content
    source_code = html.fromstring(byte_data)
    tree = source_code.xpath(LinkPath)
    tr = source_code.xpath('//*[@id="truyen-slide"]/div[1]/div/div[1]/div/div/div/div/div[2]/div[4]')
    linkan = tree[0]
    chp = tr[0].text_content()
    print(linkan)
    return linkan

def listedChapter(lasted):
    resp = requests.get(webLnk)
    byte_data = resp.content
    source_code = html.fromstring(byte_data)
    tr = source_code.xpath('//*[@id="truyen-slide"]/div[1]/div/div[1]/div/div/div/div/div[2]/div[4]')
    chp = tr[0].text_content()
    chapamount = chapterGetter(chp)
    for x in range(1, chapamount):
        data = req.getLnk(lasted, x)
        print(data)
def descGetter():
    url = linkGetter()
    rsp = requests.get(url)
    bt = rsp.content
    sc = html.fromstring(bt)
    tr = sc.xpath(TitlePath)
    new = sc.xpath(DescPath)
    rw = sc.xpath(RatePath)
    lastcp = sc.xpath(LastetChap)
    Lasted = lastcp[0]
    lx = Lasted.split("chapter-")[1:]
    rating = rw[0].text_content()
    Deskirpsi = new[0].text_content()
    titles = tr[0].text_content()
    print("Title: ",titles+"\nrating: "+rating+"\nDesc: "+Deskirpsi)
    listedChapter(Lasted)
descGetter()