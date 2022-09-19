from selenium import webdriver
option = webdriver.ChromeOptions()

# add UA
options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')

# 指定瀏覽器分辨率
options.add_argument('window-size=1920x3000') 

# google提到此行可避免BUG
chrome_options.add_argument('--disable-gpu') 

 # 隐藏滾動，應付一些特殊頁面
options.add_argument('--hide-scrollbars')

# 不載入圖片
options.add_argument('blink-settings=imagesEnabled=false') 

# 無頭模式
options.add_argument('--headless') 

# 以root執行
options.add_argument('--no-sandbox')

# 指定driver位置
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" 

#加入crx插件
option.add_extension('d:\crx\AdBlock_v2.17.crx') 

# 禁用JavaScript
option.add_argument("--disable-javascript") 

# 設定開發者模式啟動，該模式下webdriver属性为正常值
options.add_experimental_option('excludeSwitches', ['enable-automation']) 

# 禁用彈跳視窗
prefs = {  
    'profile.default_content_setting_values' :  {  
        'notifications' : 2  
     }  
}  
options.add_experimental_option('prefs',prefs)


driver=webdriver.Chrome(chrome_options=chrome_options)
