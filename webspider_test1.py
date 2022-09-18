from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui

'''
opts = Options()
opts.add_argument('--headless')
opts.add_argument('--disable-gpu')
'''
#options=opts

url = 'https://www.ptt.cc/bbs/Gov_owned/index.html'
browser = webdriver.Edge(r'E:\driver\edge\msedgedriver.exe')
browser.get(url)
time.sleep(2)

table = browser.find_elements(By.CLASS_NAME, 'r-ent')
i = int(0)
size = len(table)
'''
for i in range(size):
    t = table[i].find_element(By.CLASS_NAME, 'title')
    print(t.text)
    
    browser.find_element(By.LINK_TEXT, t.text).click()
    time.sleep(1)
'''

# go to first page
t = table[1].find_element(By.CLASS_NAME, 'title')
print(t.text)
browser.find_element(By.LINK_TEXT, t.text).click()
time.sleep(9)

browser.back() # go back 
time.sleep(5)

# second page
table = browser.find_elements(By.CLASS_NAME, 'r-ent')
t1 = table[2].find_element(By.CLASS_NAME, 'title')
print(t1.text)
browser.find_element(By.LINK_TEXT, t1.text).click()
time.sleep(9)
browser.back() # go back
time.sleep(3)

browser.quit()