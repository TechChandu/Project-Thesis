import time
import pickle

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = r'C:\Users\Chandu\Downloads\chromedriver_win32\chromedriver'
browser = webdriver.Chrome(executable_path=DRIVER_PATH)
browser.get("https://www.iplt20.com/video/highlights")

time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 100

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    no_of_pagedowns-=1

allElements = browser.find_elements_by_xpath('//*[@id="main-content"]/div/div/section/div/ul/li/a')

url_list = []

for element in allElements :
    url_list.append(element.get_attribute('href'))


with open('iplList.pkl', 'wb') as f:
    pickle.dump(url_list, f)


print(len(url_list))