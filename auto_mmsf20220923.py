def printPM(_size, _input_date, _table):
    rank = 1
    for i in range(1,_size,1): 
        ss = '//*[@id="PMTab1"]/table/tbody/tr['+str(i)+']/td[1]'
        tt = '//*[@id="PMTab1"]/table/tbody/tr['+str(i)+']/td[3]'
        pmd = _table.find_element(By.XPATH, ss)
        if pmd.text == _input_date:
            pm = _table.find_element(By.XPATH, tt)
            print(str(rank)+'\t'+pmd.text+'\t'+pm.text)
            rank += 1

    



from selenium import webdriver
import time
import datetime
import pyautogui
from selenium.webdriver.common.by import By


url = 'http://10.101.130.2/'
account = '480564'
pwd = '11111111'
print("興達發電廠MMS系統")
print("登入帳號 :  " + account)
print("密    碼 :  " + pwd)
input("輸入任意鍵繼續")
input_date = input("輸入保養工單日期 :(EX. 20220923)")

print("Open website...")


options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(r"D:\otherfile\msedgedriver.exe",options=options)
driver.get(url)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-bar"]/li[5]/a').click()
time.sleep(2)

#login MMS by Account and Password
print("input account and password....")
driver.find_element(By.XPATH, '//*[@id="USER_ID"]').send_keys(account)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="PWD"]').send_keys(pwd)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="submit_btn"]').click()
time.sleep(2)
#==========================================================================




table = driver.find_element(By.ID, 'PMTab1')
trlist = table.find_elements(By.TAG_NAME, 'tr')
pmNumber = 0
size = 0
for i in trlist:
    date = i.find_element(By.CLASS_NAME, 'C11')
    size += 1
    if date.text == input_date:
        pmNumber = pmNumber + 1
time.sleep(2)



printPM(size, input_date, table)



i = 1
while i < size:
    xpathText = '/*[@id="PMTab1"]/table/tbody/tr['+ str(i) +']/td[1]'
    date = table.find_element(By.XPATH, xpathText)
    if date.text == input_date:
        time.sleep(2)
        date.click()
        #----------------------
        time.sleep(2)
        driver.find_element(By.ID, 'CTRL_3_YES').click()
        #-----------------------
        time.sleep(4)
        pyautogui.press('enter')
        time.sleep(4)
        dirver.close()
        #-------------------
        time.sleep(2)
        driver.back()
        i = i + 1
        table = driver.find_element(By.ID, 'PMTab1')
             
    else:
        i = i + 1
    time.sleep(2)
    

input("All PM have been printed. Press Enter to close browser")
########################################################
driver.quit()

