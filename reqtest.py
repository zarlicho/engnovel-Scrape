from linecache import getline
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.headless = True
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome(executable_path="C:\\Users\\Diva Creative\\Downloads\\Compressed\chromedriver.exe", chrome_options=opt)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

actions = ActionChains(driver)
chapt = []
def getLnk(link, ammount):
    driver.get(link)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='chapter_jump']"))).click()
    chap = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='chapter_jump']/option[{rel}]".format(rel=ammount))))
    chapter = chap.text,chap.get_attribute("value")
    return chapter

