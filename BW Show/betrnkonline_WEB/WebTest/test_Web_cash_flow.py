#載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait






def PRD_purchase(driver):#到購點頁面
    try:
        driver.refresh
        time.sleep(1)
        # 点击購點兌換
        BuyCash = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[5]/div/span")
        BuyCash.click()
        time.sleep(1)

        # 点击購點
        Buy = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[5]/ul/li[1]/div")
        Buy.click()
        time.sleep(1)

    except:print("無法點擊購點頁面")
        
        

def PRD_telecombuy(driver):#電信支付
    try:
        telecombuy = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/div[2]/div/div[1]/button[1]") #點擊電信支付
        telecombuy.click()
        
    except:print("電信支付管道異常")


def PRD_elecpay(driver):
    try:
        elecpay = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/div[2]/div/div[1]/button[2]") #點擊電子/行動支付
        elecpay.click()

    except:print("電子/行動支付管道異常")




def PRD_HiNet_100(driver):#中華HiNet配100面額
    driver.execute_script("window.scrollBy(0, 400);")
    try:   
        #點擊中華Hinet
        HiNet = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[1]")
        HiNet.click()
        time.sleep(1)
        

        #點擊100TWD$100
        Buy_100 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/button")
        Buy_100.click()
        time.sleep(1)

        #點擊確認
        Check_100 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/button[2]")
        Check_100.click()
        try:
            #找尋MYCARD100面額
            MYCARD_100  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_100[3]
            # 檢查元素是否包含指定文本
            if '100' in fourth_element.text:
                print('HiNet_100面額流程正確,元素存在且包含 "100 TWD"')
            else:
                print('HiNet_100面額流程正確,元素存在但不包含 "100 TWD"')
        except:
            print('元素不存在')
    
    except:print("HiNet_100面額異常")


def PRD_FET_150(driver):#遠傳FET配150面額
    driver.execute_script("window.scrollBy(0, 400);")
    try:   
        #點擊遠傳FET
        FET = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[2]")
        FET.click()
        time.sleep(1)
        

        #點擊150TWD
        Buy_150 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]/button")
        Buy_150.click()
        time.sleep(1)

        #點擊確認
        Check_150 = driver.find_element(By.CLASS_NAME,"styles_secondaryButton__9LRf_")
        Check_150.click()
        try:
            #找尋MYCARD150面額
            MYCARD_150  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_150[3]
            # 檢查元素是否包含指定文本
            if '150' in fourth_element.text:
                print('FET_100面額流程正確,元素存在且包含 "150 TWD"')
            else:
                print('FET_100面額流程正確，元素存在但不包含 "150 TWD"')
        except:
            print('元素不存在')
    
    except:print("FET_100面額異常")


def PRD_Taiwan_Mobile_300(driver):#台哥大配300面額
    driver.execute_script("window.scrollBy(0, 400);")
    try:   
        #點擊台灣大哥大
        Taiwan_Mobile = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[3]")
        Taiwan_Mobile.click()
        time.sleep(1)
        

        #點擊300TWD
        Buy_300 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[2]/button")
        Buy_300.click()
        time.sleep(1)

        #點擊確認
        Check_300 = driver.find_element(By.CLASS_NAME,"styles_secondaryButton__9LRf_")
        Check_300.click()
        try:
            #找尋MYCARD300面額
            MYCARD_300  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_300[3]
            # 檢查元素是否包含指定文本
            if '300' in fourth_element.text:
                print('台哥大_300面額正確,元素存在且包含 "300 TWD"')
            else:
                print('台哥大_300面額正確,元素存在但不包含 "300 TWD"')
        except:
            print('元素不存在')
    
    except:print("台哥大_300面額異常")


def PRD_chuntelecom_500(driver):#中華小額配500面額
    driver.execute_script("window.scrollBy(0, 700);")
    try:   
        #點擊中華電信小額付款
        chuntelecom = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[4]")
        chuntelecom.click()
        time.sleep(1)
        

        #點擊500TWD
        Buy_500 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[2]/button")
        Buy_500.click()
        time.sleep(1)

        #點擊確認
        Check_500 = driver.find_element(By.CLASS_NAME,"styles_secondaryButton__9LRf_")
        Check_500.click()
        try:
            #找尋MYCARD500面額
            MYCARD_500  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_500[3]
            # 檢查元素是否包含指定文本
            if '500' in fourth_element.text:
                print('中華電信小額_500面額流程正確,元素存在且包含 "500 TWD"')
            else:
                print('中華電信小額_500面額流程正確,元素存在但不包含 "500 TWD"')
        except:
            print('元素不存在')
    
    except:print("中華電信小額_500面額異常")

    


def PRD_GT_1000(driver):#亞太配1000面額
    driver.execute_script("window.scrollBy(0, 700);")
    try:   
        #點擊亞太
        GT = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[5]")
        GT.click()
        time.sleep(1)
        

        #點擊1000TWD
        Buy_1000 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[2]/button")
        Buy_1000.click()
        time.sleep(1)

        #點擊確認
        Check_1000 = driver.find_element(By.CLASS_NAME,"styles_secondaryButton__9LRf_")
        Check_1000.click()
        try:
            #找尋MYCARD1000面額
            MYCARD_1000  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_1000[3]
            # 檢查元素是否包含指定文本
            if '1000' in fourth_element.text:
                print('亞太_1000面額流程正確,元素存在且包含 "1000 TWD"')
            else:
                print('亞太_1000面額流程正確,元素存在但不包含 "1000 TWD"')
        except:
            print('元素不存在')
    
    except:print("亞太_1000面額異常")
        


def PRD_T_STAR_2000(driver):#台灣之星配2000面額
    driver.execute_script("window.scrollBy(0, 800);")
    try:   
        #點擊台灣之星
        GT = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[6]")
        GT.click()
        time.sleep(1)
        

        #點擊2000TWD
        Buy_2000 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[6]/td[2]/button")
        Buy_2000.click()
        time.sleep(1)

        #點擊確認
        Check_1000 = driver.find_element(By.CLASS_NAME,"styles_secondaryButton__9LRf_")
        Check_1000.click()
        try:
            #找尋MYCARD2000面額
            MYCARD_1000  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_1000[3]
            # 檢查元素是否包含指定文本
            if '2000' in fourth_element.text:
                print('元素存在且包含 "2000 TWD"')
            else:
                print('元素存在但不包含 "2000 TWD"')
        except:
            print('台灣之星服務已暫停')
    
    except:print("台灣之星_2000面額異常")
        


def PRD_telephone_100(driver):#中華市話配100面額
    driver.execute_script("window.scrollBy(0, 800);")
    try:   
        #點擊中華市話
        HiNet = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[7]")
        HiNet.click()
        time.sleep(1)
        

        #點擊100TWD$100
        Buy_100 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/button")
        Buy_100.click()
        time.sleep(1)

        #點擊確認
        Check_100 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/button[2]")
        Check_100.click()
        try:
            #找尋MYCARD100面額
            MYCARD_100  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_100[3]
            # 檢查元素是否包含指定文本
            if '100' in fourth_element.text:
                print('中華市話_100面額流程正確,元素存在且包含 "100 TWD"')
            else:
                print('中華市話_100面額流程正確,元素存在但不包含 "100 TWD"')
        except:
            print('元素不存在')
    
    except:print("中華市話_100面額異常")



def PRD_ezpay_150(driver):#ezpay配150面額
    driver.execute_script("window.scrollBy(0, 500);")
    try:   
        #點擊ezpay
        ezpay_150 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[1]")
        ezpay_150.click()
        time.sleep(1)
        

        #點擊TWD$150
        Buy_150 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/button")
        Buy_150.click()
        time.sleep(1)

        #點擊確認
        Check_150 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/button[2]")
        Check_150.click()
        #點擊關閉
        close_botton = driver.find_element(By.XPATH,"/html/body/div[6]/button")
        close_botton.click()
        time.sleep(1)
        try:
            #找尋MYCARD150面額
            MYCARD_150  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_150[3]
            # 檢查元素是否包含指定文本
            if '150' in fourth_element.text:
                print('ezpay_150面額流程正確,元素存在且包含 "150 TWD"')
            else:
                print('ezpay_150面額流程正確,元素存在但不包含 "150 TWD"')
        except:
            print('元素不存在')
    
    except:print("ezpay_150面額異常")


def PRD_Taiwanpay_300(driver):#台灣pay配300面額
    driver.execute_script("window.scrollBy(0, 500);")
    try:   
        #點擊台灣pay
        Taiwanpay_300 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[2]")
        Taiwanpay_300.click()
        time.sleep(1)
        

        #點擊TWD$300
        Buy_300 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]/button")
        Buy_300.click()
        time.sleep(1)

        #點擊確認
        Check_150 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/button[2]")
        Check_150.click()
        
        try:
            #找尋MYCARD300面額
            MYCARD_150  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_150[3]
            # 檢查元素是否包含指定文本
            if '300' in fourth_element.text:
                print('台灣pay_300面額流程正確,元素存在且包含 "300 TWD"')
            else:
                print('台灣pay_300面額流程正確,元素存在但不包含 "300 TWD"')
        except:
            print('元素不存在')
    
    except:print("台灣pay_300面額異常")



def PRD_yoyopay_500(driver):#悠遊pay配500面額
    driver.execute_script("window.scrollBy(0, 500);")
    try:   
        #點擊悠遊pay
        yoyopay_500 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[3]")
        yoyopay_500.click()
        time.sleep(1)
        

        #點擊TWD$500
        Buy_500 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[2]/button")
        Buy_500.click()
        time.sleep(1)

        #點擊確認
        Check_500 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/button[2]")
        Check_500.click()
        
        try:
            #找尋MYCARD500面額
            MYCARD_150  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_150[3]
            # 檢查元素是否包含指定文本
            if '500' in fourth_element.text:
                print('悠遊pay_500面額流程正確,元素存在且包含 "500 TWD"')
            else:
                print('悠遊pay_500面額流程正確,元素存在但不包含 "500 TWD"')
        except:
            print('元素不存在')
    
    except:print("悠遊pay_500面額異常")



def PRD_All_of_pay_1000(driver):#全支付pay配1000面額
    driver.execute_script("window.scrollBy(0, 500);")
    try:   
        #點擊全支付pay
        All_of_pay_1000 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[4]")
        All_of_pay_1000.click()
        time.sleep(1)
        

        #點擊TWD$1000
        Buy_1000 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[2]/button")
        Buy_1000.click()
        time.sleep(1)

        #點擊確認
        Check_500 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/button[2]")
        Check_500.click()
        
        try:
            #找尋MYCARD1000面額
            MYCARD_150  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_150[3]
            # 檢查元素是否包含指定文本
            if '1000' in fourth_element.text:
                print('全支付pay_1000面額流程正確,元素存在且包含 "1000 TWD"')
            else:
                print('全支付pay_1000面額流程正確,元素存在但不包含 "1000 TWD"')
        except:
            print('元素不存在')
    
    except:print("全支付pay_1000面額異常")


def PRD_icash_pay_2000(driver):#icashpay配2000面額
    driver.execute_script("window.scrollBy(0, 500);")
    try:   
        #點擊icashpay
        icash_pay_2000 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[5]")
        icash_pay_2000.click()
        time.sleep(1)
        

        #點擊TWD$2000
        Buy_2000 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[2]/button")
        Buy_2000.click()
        time.sleep(1)

        #點擊確認
        Check_500 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/button[2]")
        Check_500.click()
        
        try:
            #找尋MYCARD2000面額
            MYCARD_150  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_150[3]
            # 檢查元素是否包含指定文本
            if '2000' in fourth_element.text:
                print('icash_pay_2000面額流程正確,元素存在且包含 "2000 TWD"')
            else:
                print('icash_pay_2000面額流程正確,元素存在但不包含 "2000 TWD"')
        except:
            print('元素不存在')
    
    except:print("icash_pay_2000面額異常")



def PRD_line_pay_3000(driver):#linepay配3000面額
    driver.execute_script("window.scrollBy(0, 500);")
    try:   
        #點擊linepay
        line_pay_3000 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[7]")
        line_pay_3000.click()
        time.sleep(1)
        

        #點擊TWD$3000
        Buy_3000 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[6]/td[2]/button")
        Buy_3000.click()
        time.sleep(1)

        #點擊確認
        Check_500 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/button[2]")
        Check_500.click()
        
        try:
            #找尋MYCARD3000面額
            MYCARD_150  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_150[3]
            # 檢查元素是否包含指定文本
            if '3000' in fourth_element.text:
                print('line_pay_3000面額流程正確,元素存在且包含 "3000 TWD"')
            else:
                print('line_pay_3000面額流程正確,元素存在但不包含 "3000 TWD"')
        except:
            print('元素不存在')
    
    except:print("line_pay_3000面額異常")


def PRD_apple_pay_150(driver):#applepay配150面額
    driver.execute_script("window.scrollBy(0, 500);")
    try:   
        #點擊applepay
        apple_pay_150 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[8]")
        apple_pay_150.click()
        time.sleep(1)
        

        #點擊TWD$150
        Buy_150 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/button")
        Buy_150.click()
        time.sleep(1)

        #點擊確認
        Check_500 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/button[2]")
        Check_500.click()
        
        try:
            #找尋MYCARD150面額
            MYCARD_150  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_150[3]
            # 檢查元素是否包含指定文本
            if '150' in fourth_element.text:
                print('Apple_pay_150面額正確,元素存在且包含 "150 TWD"')
            else:
                print('元素存在但不包含 "150 TWD"')
        except:
            print('不支援APPLEPAY管道')
    
    except:print("Apple_pay_150面額異常")

def PRR_ATM(driver):
    driver.execute_script("window.scrollBy(0, 500);")
    try:
        #點擊ATM
        ATM = driver.find_elements(By.CLASS_NAME,"pay_gateWayButton__nr0_6")
        ATM2 = ATM[2]
        ATM2.click()
    except:print("ATM轉帳按鈕無法點擊")

def PRD_FirstBank(driver):
    try:
        #點擊第一銀行
        firstbank = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[1]")
        firstbank.click()
    except:print("第一銀行無法點擊")

def PRD_FirstBank_pay(driver):
    try:
        #找到$150面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/button"),"$150"))
        print("Match", "找到第一銀行150$面額")
        #找到$300面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]/button"),"$300"))
        print("Match", "找到第一銀行300$面額")
        #找到$500面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[2]/button"),"$500"))
        print("Match", "找到第一銀行500$面額")
        #找到$1000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[2]/button"),"$1,000"))
        print("Match", "找到第一銀行1000$面額")
        #找到$1500面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[2]/button"),"$1,500"))
        print("Match", "找到第一銀行1500$面額")
        #找到$2000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[6]/td[2]/button"),"$2,000"))
        print("Match", "找到第一銀行2000$面額")
        #找到$3000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[7]/td[2]/button"),"$3,000"))
        print("Match", "找到第一銀行3000$面額")
        #找到$5000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[8]/td[2]/button"),"$5,000"))
        print("Match", "找到第一銀行5000$面額")
        #找到$10000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[9]/td[2]/button"),"$10,000"))
        print("Match", "找到第一銀行10000$面額")
        #找到$20000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[10]/td[2]/button"),"$20,000"))
        print("Match", "找到第一銀行20000$面額")

    except:print("找無第一銀行面額有誤")

def PRD_CTBC(driver):
    try:
        #點擊中國信託
        CTBC = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button[2]")
        CTBC.click()
    except:print("中國信託無法點擊")

def PRD_CTBC_pay(driver):
    try:
        #找到$150面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/button"),"$150"))
        print("Match", "找到中國信託150$面額")
        #找到$300面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]/button"),"$300"))
        print("Match", "找到中國信託300$面額")
        #找到$500面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[2]/button"),"$500"))
        print("Match", "找到中國信託500$面額")
        #找到$1000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[2]/button"),"$1,000"))
        print("Match", "找到中國信託1000$面額")
        #找到$1500面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[2]/button"),"$1,500"))
        print("Match", "找到中國信託1500$面額")
        #找到$2000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[6]/td[2]/button"),"$2,000"))
        print("Match", "找到中國信託2000$面額")
        #找到$3000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[7]/td[2]/button"),"$3,000"))
        print("Match", "找到中國信託3000$面額")
        #找到$5000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[8]/td[2]/button"),"$5,000"))
        print("Match", "找到中國信託5000$面額")
        #找到$10000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[9]/td[2]/button"),"$10,000"))
        print("Match", "找到中國信託10000$面額")
        #找到$20000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[10]/td[2]/button"),"$20,000"))
        print("Match", "找到中國信託20000$面額")

    except:print("中國信託面額有誤")

def PRD_Creditpay(driver):
    try:
        #點擊信用卡支付
        credit = driver.find_elements(By.CLASS_NAME,"pay_gateWayButton__nr0_6")
        credit2 =credit[3]
        credit2.click()
    except:print("信用卡支付無法點擊")

def PRD_FunPoint(driver):
    try:
        #點擊FunPoint
        FunPoint = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[1]/button")
        FunPoint.click()
    except:print("信用卡付款-FunPoint無法點擊")

def PRD_FunPoint_Pay(driver):
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(1)
    try:
        #找到$150面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/button"),"$150"))
        print("Match", "找到FunPoint 150$面額")
        #找到$300面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]/button"),"$300"))
        print("Match", "找到FunPoint 300$面額")
        #找到$500面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[3]/td[2]/button"),"$500"))
        print("Match", "找到FunPoint 500$面額")
        #找到$1000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[2]/button"),"$1,000"))
        print("Match", "找到FunPoint 1000$面額")
        #找到$2000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[2]/button"),"$2,000"))
        print("Match", "找到FunPoint 2000$面額")
        #找到$3000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[6]/td[2]/button"),"$3,000"))
        print("Match", "找到FunPoint 3000$面額")
        #找到$5000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[7]/td[2]/button"),"$5,000"))
        print("Match", "找到FunPoint 5000$面額")
        #找到$10000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[8]/td[2]/button"),"$10,000"))
        print("Match", "找到FunPoint 10000$面額")
    except:print("信用卡支付面額有誤")


def PRD_Mycard_Topup(driver):
    driver.execute_script("window.scrollBy(0, 500);")
    try:
        Mycard_Topup = driver.find_elements(By.CLASS_NAME,"pay_gateWayButton__nr0_6")
        Mycard_Topup1 =Mycard_Topup[4]
        Mycard_Topup1.click()
    except:print("Mycard序號儲值無法點擊")

def PRD_Mycard_Topup_pay(driver):
    try:
        #找到$30面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/button"),"$30"))
        print("Match", "找到Mycard序號儲值 30$面額")
        #找到$50面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/button"),"$50"))
        print("Match", "找到Mycard序號儲值 50$面額")
        #找到$90面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/button"),"$90"))
        print("Match", "找到Mycard序號儲值 90$面額")
        #找到$150面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[2]/button"),"$150"))
        print("Match", "找到Mycard序號儲值 150$面額")
        #找到$170面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[5]/td[2]/button"),"$170"))
        print("Match", "找到Mycard序號儲值 170$面額")
        #找到$300面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[6]/td[2]/button"),"$300"))
        print("Match", "找到Mycard序號儲值 300$面額")
        #找到$350面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[7]/td[2]/button"),"$350"))
        print("Match", "找到Mycard序號儲值 350$面額")
        #找到$400面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[8]/td[2]/button"),"$400"))
        print("Match", "找到Mycard序號儲值 400$面額")
        #找到$450面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[9]/td[2]/button"),"$450"))
        print("Match", "找到Mycard序號儲值 450$面額")
        #找到$500面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[10]/td[2]/button"),"$500"))
        print("Match", "找到Mycard序號儲值 500$面額")
        #找到$750面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[11]/td[2]/button"),"$750"))
        print("Match", "找到Mycard序號儲值 750$面額")
        #找到$1000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[12]/td[2]/button"),"$1,000"))
        print("Match", "找到Mycard序號儲值 1000$面額")
        #找到$1150面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[13]/td[2]/button"),"$1,150"))
        print("Match", "找到Mycard序號儲值 1150$面額")
        #找到$1490面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[14]/td[2]/button"),"$1,490"))
        print("Match", "找到Mycard序號儲值 1490$面額")
        #找到$1690面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[15]/td[2]/button"),"$1,690"))
        print("Match", "找到Mycard序號儲值 1690$面額")
        #找到$2000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[16]/td[2]/button"),"$2,000"))
        print("Match", "找到Mycard序號儲值 2000$面額")
        #找到$2500面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[17]/td[2]/button"),"$2,500"))
        print("Match", "找到Mycard序號儲值 2500$面額")
        #找到$3000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[18]/td[2]/button"),"$3,000"))
        print("Match", "找到Mycard序號儲值 3000$面額")
        #找到$3290面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[19]/td[2]/button"),"$3,290"))
        print("Match", "找到Mycard序號儲值 3290$面額")
    except:print("Mycard序號儲值面額異常")

def PRD_Mycard_reduce_point(driver):
    try:
        Mycard_Topup = driver.find_elements(By.CLASS_NAME,"pay_gateWayButton__nr0_6")
        Mycard_Topup1 =Mycard_Topup[5]
        Mycard_Topup1.click()
    except:print("Mycard線上扣點無法點擊")

def PRD_Mycard_reduce_point_pay(driver):
    try:
        #找到$50面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/button"),"$50"))
        print("Match", "找到Mycard線上扣點 50$面額")
        #找到$150面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/button"),"$150"))
        print("Match", "找到Mycard線上扣點 150$面額")
        #找到$300面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/button"),"$300"))
        print("Match", "找到Mycard線上扣點 300$面額")
        #找到$500面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[2]/button"),"$500"))
        print("Match", "找到Mycard線上扣點 500$面額")
        #找到$1000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[5]/td[2]/button"),"1,000"))
        print("Match", "找到Mycard線上扣點 1000$面額")
        #找到$1490面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[6]/td[2]/button"),"1,490"))
        print("Match", "找到Mycard線上扣點 1490$面額")
        #找到$2000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[7]/td[2]/button"),"2,000"))
        print("Match", "找到Mycard線上扣點 2000$面額")
        #找到$3000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[8]/td[2]/button"),"3,000"))
        print("Match", "找到Mycard線上扣點 3000$面額")
    except:print("Mycard線上扣點面額異常")


def PRD_Mycard_free_discount(driver):
    try:
        #點擊Mycarc免費折扣
        mycard_free_discount = driver.find_elements(By.CLASS_NAME,"pay_gateWayButton__nr0_6")
        mycard_free_discount2 = mycard_free_discount[6]
        mycard_free_discount2.click()
    except:print("Mycard免費折扣無法點擊")


def PRD_Mycard_free_discount_pay(driver):
    try:
        #找到$50面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/button"),"$50"))
        print("Match", "找到Mycard免費折扣 50$面額")
        #找到$150面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/button"),"$150"))
        print("Match", "找到Mycard免費折扣 150$面額")
        #找到$300面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/button"),"$300"))
        print("Match", "找到Mycard免費折扣 300$面額")
        #找到$500面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[2]/button"),"$500"))
        print("Match", "找到Mycard免費折扣 500$面額")
        #找到$1000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[5]/td[2]/button"),"1,000"))
        print("Match", "找到Mycard免費折扣 1000$面額")
        #找到$1490面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[6]/td[2]/button"),"$1,490"))
        print("Match", "找到Mycard免費折扣 1490$面額")
        #找到$2000面額
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[7]/td[2]/button"),"2,000"))
        print("Match", "找到Mycard免費折扣 2000$面額")
    except:print("Mycard免費折扣面額有誤")


def PRD_Mycard_free_discount_pay_Action(driver):
    try:
        #點擊$2000面額
        pay_2000 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[7]/td[2]/button")
        pay_2000.click()
        check_button = driver.find_element(By.CLASS_NAME,"styles_secondaryButton__9LRf_")
        check_button.click()
        try:
            #找尋MYCARD2000面額
            MYCARD_2000  = driver.find_elements(By.CSS_SELECTOR, '.lock_textbox.lock_pic')
            fourth_element = MYCARD_2000[3]
            # 檢查元素是否包含指定文本
            if '2000' in fourth_element.text:
                print('Mycard免費折扣購點流程正確,元素存在且包含 "2000 TWD"')
            else:
                print('元素存在但不包含 "2000 TWD"')
        except:
            print('找不到2000 TWD')
    except:print("Mycard免費折扣購點流程異常")