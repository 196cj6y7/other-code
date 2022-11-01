def printPM(_size, _input_date, _table):
    rank = 1
    try:
        for i in range(1,_size,1): 
            ss = '//*[@id="PMTab1"]/table/tbody/tr['+str(i)+']/td[1]'
            tt = '//*[@id="PMTab1"]/table/tbody/tr['+str(i)+']/td[3]'
            pmd = _table.find_element(By.XPATH, ss)
            if pmd.text == _input_date:
                pm = _table.find_element(By.XPATH, tt)
                print(str(rank)+'\t'+pmd.text+'\t'+pm.text)
                rank += 1
    except:
        print("Today has no PM to print")
        time.sleep(3)
        driver.quit()
            
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
    pm_table_size = 0
    for i in _trlist:
        date = i.find_element(By.CLASS_NAME, 'C11')
        pm_table_size += 1
        if date.text == _input_date:
            pmNumber = pmNumber + 1
    return (pm_table_size, pmNumber)
    
def savePMtoRank(_size, _trlist, _input_date):
    j = 0
    PM_list = []
    for i in _trlist:
        date = i.find_element(By.CLASS_NAME, 'C11')
        if date.text == _input_date:
            temp_list = []
            xpath_number = j
            temp_list.append(xpath_number)
            pmDetailX = '//*[@id="PMTab1"]/table/tbody/tr['+str(j)+']/td[3]'
            PM_item = i.find_element(By.XPATH, pmDetailX).text
            temp_list.append(PM_item)    
            PM_list.append(temp_list)
        j += 1
    return PM_list    
    
def RankPM2(_a, size):
    strPM = ['C', '粉', '螺', 'E', '高'] # boiler department,coal ash section 
    final = []
    temp1 = []    # 建立暫存排序
    for str in strPM: # 選擇指定字元
        #---------------------------------------
        for i in range( len(_a)):
            PM_str = _a[i][1]
            
            for j in PM_str:
                
                if j == str:     # 找到指定字元
                    temp1.append(_a[i][:])
                    break
        #----------------------------------------
        if temp1 != []:
            temp2 = func_sort(temp1)
            final += temp2
            temp1=[] # clear temp1
        else:
            continue
    final2 = []
    for num in range( len(final) ):
        final2.append( final[num][0] )
        
    return final2    
    
def func_sort(list2D):
    numrow = len(list2D)
    #print(list2D)
    return_list = []
    
    for y in range(1, numrow+1):
        for i in range(numrow):
            #print(list2D[i][1][:])
            x = list2D[i][1][1] # str
            if x == str(y):
                return_list.append(list2D[i][:])
                
            elif x == '一' and y == 1:
                return_list.append(list2D[i][:])
                
            elif x == '二' and y == 2:
                return_list.append(list2D[i][:])
                
      
    return return_list    
    
def LoopToPrintPM(_size, _table ,_input_date, list_num):
    for i in list_num:
        xpathText = '//*[@id="PMTab1"]/table/tbody/tr['+ str(i) +']/td[1]'
        XpmDetailX = '//*[@id="PMTab1"]/table/tbody/tr['+str(i)+']/td[3]'
        date = _table.find_element(By.XPATH, xpathText)
        pm_name = _table.find_element(By.XPATH, XpmDetailX).text
        time.sleep(2)
        date.click()
        #----------------------
        time.sleep(2)
        driver.find_element(By.ID, 'CTRL_3_YES').click()
        #-----------------------
        os.system('cls')
        for j in range(7,0,-1):
            print(pm_name)
            print("準備列印，剩餘 " + str(j) + ' 秒')
            time.sleep(1)
            os.system('cls')
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.hotkey('ctrl' ,'w')
        time.sleep(2)
        #-------------------
        driver.back()
        _table = driver.find_element(By.ID, 'PMTab1')           
    time.sleep(2)
    
from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.common.by import By
import os
url = 'http://10.101.130.2/'
#account = input("account: ")
#pwd = input("pwd: ")
account = '480564'
pwd = '11111111'
printAccountData(account, pwd)


#######################
input_date = input("輸入保養工單日期 :(EX. 20220303)")
#######################
#input_date = '20221017'

opts = webdriver.EdgeOptions()
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(r"D:\otherfile\msedgedriver.exe",options=opts)
driver.implicitly_wait(8)
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
#====================================================================================
table = driver.find_element(By.ID, 'PMTab1')
trlist = table.find_elements(By.TAG_NAME, 'tr')

pmSizeData = countPm(trlist, input_date) # tuples
#printAllPM(pmSizeData[0], table)

printPM(pmSizeData[0], input_date, table)
size1 = pmSizeData[1]

list1 = savePMtoRank(size1, trlist, input_date)
list2 = RankPM2(list1, size1)
LoopToPrintPM(size1, table ,input_date,list2)
input("All PM have been printed. Press Enter to close browser")
driver.quit()    
