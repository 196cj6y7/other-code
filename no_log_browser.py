from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import time

#open Firefox browser headless
opts = Options()
opts.set_headless(headless=True)
assert opts.headless

# no log file setting
browser = webdriver.Firefox(options=opts,service_log_path=os.devnull)
# service_log_path = os.devnull makes no geckodriver.log file

url = 'https://www.google.com.tw/'
brwoser.get(url)
time.sleep(3)

browser.quit()
