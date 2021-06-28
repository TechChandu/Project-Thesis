import time
import pickle

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import threading

DRIVER_PATH = r'C:\Users\Chandu\Downloads\chromedriver_win32\chromedriver'
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

with open(r'C:\Users\Chandu\OneDrive\Documents\Pose Estimation\parser\iplList.pkl', 'rb') as f:
    url_list = pickle.load(f)

url_space = '//*[@id="dlURL"]'
download_button = '//*[@id="dlBTN1"]'
save_button = '/html/body/main/section[1]/div/div[2]/div[1]/div[2]/a'

def CloseNewWindows(driver, MainWindow):
    Windows = driver.window_handles
    for window in Windows:
        driver.switch_to_window(window)
        if MainWindow != driver.current_window_handle:
            driver.close()






def download_video(url):
    browser = webdriver.Chrome(chrome_options=option, executable_path=DRIVER_PATH)
    browser.get("https://keepv.id/")
    # Implement your test logic
    browser.find_element_by_xpath(url_space).send_keys(url)
    browser.find_element_by_xpath(download_button).click()
    MainWindow = browser.current_window_handle
    CloseNewWindows(browser, MainWindow)
    time.sleep(10)
    browser.switch_to_window(MainWindow)
    browser.find_elements_by_xpath(save_button)[0].click()
    time.sleep(80)
    browser.quit()

N = 100   # Number of browsers to spawn

# Start test
for i in range(100):
    download_video(url_list[i])
    print(i)

