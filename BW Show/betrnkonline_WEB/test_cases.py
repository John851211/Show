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
import pytest
import allure

from WebTest.test_Websystem_main import *





# 設置編碼
sys.stdout.reconfigure(encoding='utf-8')


#設置版本
Version = "24.05.29"



#設置網頁URL
QAT = "https://qdl.1161023.lol/zh_tw"
PRD = "https://www.betrnkonline.com/zh_tw"

#選擇環境
URL = PRD

#google帳號密碼
email = "HS070@heshuosg.com"
password = "Ss850606"

#------------------------------------------------------------------------------

@pytest.fixture(scope="session")
def driver():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
     # 最大化視窗
    driver.maximize_window()
    yield driver

    driver.quit()




@allure.title("Google Login Test")
@allure.description("使用Google登入測試")
def test_google_login(driver):

    driver.get("https://www.google.com.tw/?hl=zh_TW")

    # 点击 Google 登录按钮
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div/div[2]/a").click()
    
    # 输入邮箱地址并点击下一步
    driver.find_element(By.ID, "identifierId").send_keys(email)
    driver.find_element(By.ID, "identifierNext").click()
    
    # 输入密码并点击下一步
    driver.find_element(By.NAME,"Passwd").send_keys(password)
    driver.find_element(By.ID, "passwordNext").click()



@allure.title("Connect_to_website_in_new_tab")
@allure.description("新開分頁測試")
def test_connect_to_website_in_new_tab(driver):
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
    driver.get(PRD)

 

@allure.title("Find Version")
@allure.description("確認版號")
def test_wait_for_text_in_element(driver):  
    
    try:
        # 设置等待条件和超时时间
        wait = WebDriverWait(driver,5)
        
        # 等待指定元素中包含指定的文本
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/p"), Version))
        
        print("Match", Version)
        assert  True 
    except: 
        
        assert False

@allure.title("Confirm_age")
@allure.description("確認18歲彈窗確認與勾選不再提示功能")
def test_confirm_age(driver):   

      

    confirm_age(driver)
    


@allure.title("Google_sign_in")
@allure.description("確認GOOGLK三方登入")
def test_google_sign_in(driver): 

    click_google_sign_in(driver)


@allure.title("Switch_to_appstore")
@allure.description("轉導至Appstore官網")
def test_click_and_switch_to_appstore(driver):  
    
    click_and_switch_to_appstore(driver)
    time.sleep(1)


@allure.title("Nowplay")
@allure.description("立即玩")
def test_click_nowplaybuttons(driver):
    
    click_nowplaybuttons(driver)
    time.sleep(1)


@allure.title("News")
@allure.description("最新消息")
def test_click_news(driver):

    click_news(driver)
    time.sleep(1)


@allure.title("Beginner")
@allure.description("新手必看")
def test_click_Beginner(driver): 

    click_Beginner(driver)
    time.sleep(1)


@allure.title("Rank")
@allure.description("活動排行")
def test_click_Rank(driver):
    
    click_Rank(driver)
    time.sleep(1)
    driver.refresh


@allure.title("Barcode_exchange")
@allure.description("兌換碼兌換流程")
def test_barcode_exchange(driver):

    barcode_exchange(driver)
    time.sleep(1)



@allure.title("ServiceCenter Information")
@allure.description("客服中心-客服資訊")
def test_click_service_center_and_information(driver): 

    click_service_center_and_information(driver)
    time.sleep(1)



@allure.title("ServiceCenter Line")
@allure.description("客服官方LINE")
def test_click_official_line_and_switch_to_new_window(driver): 

    click_official_line_and_switch_to_new_window(driver)
    time.sleep(1)


@allure.title("ServerCenter Information")
@allure.description("客服中心-客服資訊")
def test_click_official_FB_and_switch_to_new_window(driver):  

    click_official_FB_and_switch_to_new_window(driver)
    time.sleep(1)



@allure.title("ServerCenter Question")
@allure.description("客服中心-常見問題")
def test_click_service_center_and_question(driver): 

    click_service_center_and_question(driver)
    time.sleep(1)



@allure.title("ServerCenter list")
@allure.description("客服中心-停權名單")
def test_click_service_center_and_list(driver):  

    click_service_center_and_list(driver)
    time.sleep(1)



@allure.title("ServerCenter document")
@allure.description("客服中心-使用者規章")
def test_service_center_and_document(driver): 

    service_center_and_document(driver)
    time.sleep(1)



@allure.title("ServerCenter ApplicationDocument")
@allure.description("客服中心-申請文件")
def test_service_center_and_ApplicationDocument(driver): 

    service_center_and_ApplicationDocument(driver)
    time.sleep(1)


@allure.title("ServerCenter Memberfile")
@allure.description("會員中心-會員檔案")
def test_navigate_to_member_file(driver):

    navigate_to_member_file(driver)
    time.sleep(1)


@allure.title("VIP memberfile")
@allure.description("會員中心-會員檔案vip")
def test_VIP_member_file(driver):

    VIP_member_file(driver)
    time.sleep(1)


@allure.title("Passbook")
@allure.description("會員中心-我的存摺")
def test_Passbook(driver):

    Passbook(driver)
    time.sleep(1)


@allure.title("Passbook_text")
@allure.description("會員中心-我的存摺文案")
def test_Passbook_text(driver):

    Passbook_text(driver,"藍寶石")
    time.sleep(1)



@allure.title("ServiceCenter Gift")
@allure.description("會員中心-贈禮")
def test_center_and_gift(driver):  

    member_center_and_gift(driver)
    time.sleep(1)
    


@allure.title("ServiceCenter Gifttext")
@allure.description("找贈禮文案")
def test_find_for_gift_in_element(driver): 

    find_for_gift_in_element(driver)
    time.sleep(1)

    





    






