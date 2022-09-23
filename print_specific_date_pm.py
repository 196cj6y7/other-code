from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(options=options)
driver.get(r'file:///C:\Users\Administrator\Desktop\auto_mms\new_folder\興達發電廠 - 電廠維護作業管理系統.html')


''' print all table data
table = driver.find_element(By.XPATH, '//*[@id="PMTab1"]/table')
trlist = table.find_elements(By.TAG_NAME, 'tr')


for row in trlist:
    tdlist = row.find_elements(By.TAG_NAME, 'td')
    
    for col in tdlist:
        print(col.text)
'''
input_date = '20220926'
table = driver.find_element(By.ID, 'PMTab1')
trlist = table.find_elements(By.TAG_NAME, 'tr')
pmNumber = 0
size = 0
for i in trlist:
    date = i.find_element(By.CLASS_NAME, 'C11')
    size += 1
    if date.text == input_date:
        pmNumber = pmNumber + 1
        
 
for i in range(1,size,1): 
    ss = '//*[@id="PMTab1"]/table/tbody/tr['+str(i)+']/td[1]'
    tt = '//*[@id="PMTab1"]/table/tbody/tr['+str(i)+']/td[3]'
    pmd = table.find_element(By.XPATH, ss)
    if pmd.text == input_date:
        pm = table.find_element(By.XPATH, tt)
        print(str(i)+'\t'+pmd.text+'\t'+pm.text)

    





driver.quit()
   

