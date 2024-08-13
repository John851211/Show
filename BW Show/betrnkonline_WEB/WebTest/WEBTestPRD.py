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
import test_Websystem_main
import test_Web_cash_flow


# 設置編碼
sys.stdout.reconfigure(encoding='utf-8')



#環境網頁URL
QAT = ""
PRD = ""


#設置環境網頁URL
URL = PRD

#設置版本
Version = "24.08.07"


driver = test_Websystem_main.setup_driver_backstage("")

test_Websystem_main.maximize_window(driver)

test_Websystem_main.backstage_login(driver,"","")

bpm=test_Websystem_main.player_manage(driver,"","/html/body/div[1]/div/div/main/div[2]/div/div/div/div[4]/div/div[1]/table/tbody/tr/td[7]/div/div/div[1]/span","/html/body/div[1]/div/div/main/div[2]/div/div/div/div[4]/div/div[1]/table/tbody/tr/td[7]/div/div/div[2]/span","/html/body/div[1]/div/div/main/div[2]/div/div/div/div[4]/div/div[1]/table/tbody/tr/td[7]/div/div/div[3]/span")


driver = test_Websystem_main.setup_driver()


test_Websystem_main.maximize_window(driver)


test_Websystem_main.google_login(driver,"", "")



test_Websystem_main.connect_to_website_in_new_tab(driver,URL)


#找版號
test_Websystem_main.test_wait_for_text_in_element(driver,Version)

#勾選18歲彈窗
test_Websystem_main.confirm_age(driver)

#立即登入
test_Websystem_main.click_google_sign_in(driver)


#前台取得點數、日金、寶石文本
opm =test_Websystem_main.off_player_manage(driver)


test_Websystem_main.compare_values(bpm, opm)

# Appstore轉導
test_Websystem_main.click_and_switch_to_appstore(driver)

#立即玩
test_Websystem_main.click_nowplaybuttons(driver)

#最新消息
test_Websystem_main.click_news(driver)

#遊戲攻略
test_Websystem_main.click_Beginner(driver)

#特色遊戲
test_Websystem_main.special_game(driver)

#VIP說明
test_Websystem_main.VIP_directions(driver)

#贈禮說明
test_Websystem_main.gift_directions(driver)


#活動排行
test_Websystem_main.click_Rank(driver)


# 購點流程

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_telecombuy(driver)

test_Web_cash_flow.PRD_HiNet_100(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_telecombuy(driver)

test_Web_cash_flow.PRD_FET_150(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_telecombuy(driver)

test_Web_cash_flow.PRD_Taiwan_Mobile_300(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_chuntelecom_500(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_GT_1000(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_T_STAR_2000(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_telephone_100(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_elecpay(driver)

test_Web_cash_flow.PRD_ezpay_150(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_elecpay(driver)

test_Web_cash_flow.PRD_Taiwanpay_300(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_elecpay(driver)

test_Web_cash_flow.PRD_yoyopay_500(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_elecpay(driver)

test_Web_cash_flow.PRD_All_of_pay_1000(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_elecpay(driver)

test_Web_cash_flow.PRD_icash_pay_2000(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_elecpay(driver)

test_Web_cash_flow.PRD_line_pay_3000(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_elecpay(driver)

test_Web_cash_flow.PRD_apple_pay_150(driver)

driver.back()

driver.refresh

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRR_ATM(driver)

test_Web_cash_flow.PRD_FirstBank(driver)

test_Web_cash_flow.PRD_FirstBank_pay(driver)

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRR_ATM(driver)

test_Web_cash_flow.PRD_CTBC(driver)

test_Web_cash_flow.PRD_CTBC_pay(driver)

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_Creditpay(driver)

test_Web_cash_flow.PRD_FunPoint(driver)

test_Web_cash_flow.PRD_FunPoint_Pay(driver)

test_Web_cash_flow.PRD_purchase(driver)

test_Web_cash_flow.PRD_Mycard_Topup(driver)

test_Web_cash_flow.PRD_Mycard_Topup_pay(driver)

test_Web_cash_flow.PRD_Mycard_reduce_point(driver)

test_Web_cash_flow.PRD_Mycard_reduce_point_pay(driver)

test_Web_cash_flow.PRD_Mycard_free_discount(driver)

test_Web_cash_flow.PRD_Mycard_free_discount_pay(driver)

test_Web_cash_flow.PRD_Mycard_free_discount_pay_Action(driver)

driver.back()

driver.refresh


#兌換碼兌換流程
test_Websystem_main.barcode_exchange(driver)


#客服中心-客服資訊
test_Websystem_main.click_service_center_and_information(driver)


#點擊客服官方LINE
test_Websystem_main.click_official_line_and_switch_to_new_window(driver)

#點擊客服官方FB
test_Websystem_main.click_official_FB_and_switch_to_new_window(driver)

#客服中心-常見問題
test_Websystem_main.click_service_center_and_question(driver)

time.sleep(1)

#客服中心-停權名單
test_Websystem_main.click_service_center_and_list(driver)

time.sleep(1)

#客服中心-使用者規章
test_Websystem_main.service_center_and_document(driver)

time.sleep(1)

#客服中心-申請文件
test_Websystem_main.service_center_and_ApplicationDocument(driver)

#會員中心-會員檔案
test_Websystem_main.navigate_to_member_file(driver)
driver.refresh
test_Websystem_main.VIP_member_file(driver,"藍寶石")

#會員中心-我的存摺
test_Websystem_main.Passbook(driver)
test_Websystem_main.Passbook_text(driver)


#會員中心-贈禮
test_Websystem_main.member_center_and_gift(driver)
test_Websystem_main.find_for_gift_in_element(driver)


#聊天室
test_Websystem_main.chatroom(driver)











