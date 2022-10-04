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
    time.sleep(3)
            
def printAccountData(_account, _pwd):
    print("興達發電廠MMS系統")
    print("登入帳號 :  " + _account)
    print("密    碼 :  " + _pwd)
    input("輸入任意鍵繼續")
    print("Open website...")
    
def printAllPM(_size, _table):
    for i in range(1, _size, 1):
        pmDateX = '//*[@id="PMTab1"]/table/tbody/tr['+str(i)+']/td[1]'
        pmDetailX = '//*[@id="PMTab1"]/table/tbody/tr['+str(i)+']/td[3]'
        pmDate = _table.find_element(By.XPATH, pmDateX)
        pmDetail = _table.find_element(By.XPATH, pmDetailX)
        print(str(i)+'\t'+pmDate.text+'\t'+pmDetail.text)
    

def countPm(_trlist, _input_date):
    pmNumber = 0
    size = 0
    for i in _trlist:
        date = i.find_element(By.CLASS_NAME, 'C11')
        size += 1
        if date.text == _input_date:
            pmNumber = pmNumber + 1
    return (size, pmNumber)
    
def LoopToPrintPM(_size, _table ,_input_date):
    i = 1
    while i<_size:
        xpathText = '//*[@id="PMTab1"]/table/tbody/tr['+ str(i) +']/td[1]'
        date = _table.find_element(By.XPATH, xpathText)
        if date.text == _input_date:
            time.sleep(2)
            date.click()
            #----------------------
            time.sleep(2)
            driver.find_element(By.ID, 'CTRL_3_YES').click()
            #-----------------------
            time.sleep(4)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.hotkey('ctrl' ,'w')
            time.sleep(2)
            #-------------------
            
            driver.back()
            i = i + 1
            _table = driver.find_element(By.ID, 'PMTab1')           
        else:
            i = i + 1
    time.sleep(2)
    
from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.by import By
url = 'http://10.101.130.2/'
account = input("account: ")
pwd = input("pwd: ")
#account = '480564'
#pwd = '11111111'
printAccountData(account, pwd)


#######################
input_date = input("輸入保養工單日期 :(EX. 20220303)")
#######################


opts = webdriver.EdgeOptions()
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(r"D:\otherfile\msedgedriver.exe",options=opts)
driver.get(url)
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-bar"]/li[5]/a').click()
time.sleep(2)
print("input account and password....")
driver.find_element(By.XPATH, '//*[@id="USER_ID"]').send_keys(account)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="PWD"]').send_keys(pwd)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="submit_btn"]').click()
time.sleep(2)





print('input date : ' + input_date)
table = driver.find_element(By.ID, 'PMTab1')
trlist = table.find_elements(By.TAG_NAME, 'tr')

pmSizeData = countPm(trlist, input_date) # tuples
#printAllPM(pmSizeData[0], table)
printPM(pmSizeData[0], input_date, table)
LoopToPrintPM(pmSizeData[0], table ,input_date)
input("All PM have been printed. Press Enter to close browser")
driver.quit()    
