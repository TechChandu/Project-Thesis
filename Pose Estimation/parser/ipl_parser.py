from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

DRIVER_PATH = r'C:\Users\Chandu\Downloads\chromedriver_win32\chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.iplt20.com/video/highlights")


link = driver.find_element_by_xpath('//*[@id="main-content"]/div/div/section/div/ul/li[1]/a').get_attribute("href")

print(link)