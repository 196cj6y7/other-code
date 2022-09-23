

# location pm of input date
def location_pm(input_date):
    _input_date = input_date
    _table = driver.find_element(By.ID, "PMTab1")
    _trlist = _table.find_elements(By.TAG_NAME, 'tr')
    _pm_list = []
    for i in trlist:
    _date = i.find_element(By.CLASS_NAME, 'C11')
    if _date.text == _input_date:
      _pm_list.append(i)
      
    return _pm_list


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


#------------------- locate pm table ---------------------------------
print("Enter PM website...")
table = driver.find_element(By.ID, "PMTab1")
trlist = table.find_elements(By.TAG_NAME, 'tr') # total pm in one month

#------------  find all pm in the date ----------------------

pm_list = []  # the list include the pm of input date, type : selenium
for i in trlist:
    date = i.find_element(By.CLASS_NAME, 'C11')
    if date.text == input_date:
      pm_list.append(i) 

#------------ click and print all pm of input date -----------------------
time.sleep(2)
i = 0
for j in pm_list:
    time.sleep(2)
    temp = pm_list[i].find_elements(By.CLASS_NAME, 'C14') 
    # temp => [設備編號   保養項目], type : selenium
    
    print("Enter " + temp[1].text)
    driver.find_element(By.LINK_TEXT, temp[0].text).click()#*************
    #--------------------------------
    
    time.sleep(2)
    driver.find_element(By.ID, 'CTRL_3_YES').click() # 列印保養工單
    
    time.sleep(5)
    pyautogui.press('enter') # 跑出列印畫面按Enter
    time.sleep(3)
    driver.switch_to_window(driver.window_handles[0]) # 切回主頁面
    
    time.sleep(2)
    driver.back() # 上一頁
    i = i + 1
    pm_list = location_pm(input_date)
    
    
    
    
      
    
time.sleep(2)

input("All PM have been printed. Press Enter to close browser")
########################################################
driver.quit()

