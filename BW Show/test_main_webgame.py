#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import sys





def setup_driver():
    
    # 創建一個 Chrome WebDriver 實例
    driver = webdriver.Chrome()
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver.implicitly_wait(10)  # 设置隐式等待时间
    driver.get("https://www.google.com.tw/?hl=zh_TW")
    return driver




def maximize_window(driver):# 最大化視窗
    

    driver.maximize_window()


def google_login(driver,email, password):#Google登入
    # 点击 Google 登录按钮
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div/div[2]/a").click()
    
    # 输入邮箱地址并点击下一步
    driver.find_element(By.ID, "identifierId").send_keys(email)
    driver.find_element(By.ID, "identifierNext").click()
    
    # 输入密码并点击下一步
    driver.find_element(By.NAME,"Passwd").send_keys(password)
    driver.find_element(By.ID, "passwordNext").click()


def connect_to_website_in_new_tab(driver, URL):  #連線到博悅
    # 打开一个新的空白标签页
    driver.execute_script("window.open('about:blank', '_blank');")
    # 获取当前窗口句柄
    current_window_handle = driver.current_window_handle
    # 切换到新打开的标签页
    for handle in driver.window_handles:
        if handle != current_window_handle:
            driver.switch_to.window(handle)
            break
    # 在新标签页中连接到指定的网站
    driver.get(URL)

def confirm_age(driver):#勾選18歲彈窗
    try:
        # 找到确认已满18岁的复选框并点击
        noremind_checkbox = driver.find_element(By.CLASS_NAME, "limitAge_checkbox__d6XiN")
        noremind_checkbox.click()
       

        # 找到确认按钮并点击
        confirm_button = driver.find_element(By.CLASS_NAME, "styles_greenButton__zIocO")
        confirm_button.click()
        
        print("18歲彈窗流程正確")
   
    

    except:print("18歲彈窗流程失敗")


def click_google_sign_in(driver):#立即玩登入
    # 找到 Google 三方登录按钮
    login_btn_google = driver.find_element(By.CLASS_NAME, "signIModal_loginBtnGoogle__bFsCU")
    
    # 创建 ActionChains 对象
    actions = ActionChains(driver)
    
    # 将鼠标移动到按钮上并点击
    actions.move_to_element(login_btn_google).click(login_btn_google).perform()
    time.sleep(5)

def Switch_mobile_mode(driver):
    # 使用 CDP 命令切換到移動設備模擬模式
    device_metrics = {
    "width": 375,
    "height": 812,
    "deviceScaleFactor": 3,
    "mobile": True
    }

    driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', device_metrics)
    driver.execute_cdp_cmd('Emulation.setUserAgentOverride', {
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15A372 Safari/604.1"
    })



driver = setup_driver()

maximize_window(driver)

google_login(driver,"HS070@heshuosg.com", "Ss850606")

connect_to_website_in_new_tab(driver,"https://qdl.1161023.lol/zh_tw/play-game/m")

confirm_age(driver)

click_google_sign_in(driver)

Switch_mobile_mode(driver)


    

time.sleep(100)






