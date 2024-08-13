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

# 設置編碼
sys.stdout.reconfigure(encoding='utf-8')



def setup_driver():
    
    # 創建一個 Chrome WebDriver 實例
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # 设置隐式等待时间
    driver.get("https://www.google.com.tw/?hl=zh_TW")
    return driver

def setup_driver_backstage(BSURL): #連線到後台
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # 设置隐式等待时间
    driver.get(BSURL)
    return driver


def backstage_login(driver,baccount,bpassword): # 後台登入流程

    time.sleep(2)
    account = driver.find_element(By.XPATH,"/html/body/div/div/div/div/form/div[1]/div/input")
    
    account.send_keys(baccount)
   
    password = driver.find_element(By.XPATH,"/html/body/div/div/div/div/form/div[2]/div/input")
    
    password.send_keys(bpassword)
   
    driver.find_element(By.XPATH,"/html/body/div/div/div/div/form/button").click()


def player_manage(driver,playername1,QATX1,QATX2,QATX3): #後台取得玩家點數、日金、寶石資料
    accountmanage = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/ul[1]/div[6]/div[1]/div[2]/span")
    accountmanage.click()
    playerinformation = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div/ul[1]/div[6]/div[2]/div/div/ul/div[1]/div[2]/div/span")
    playerinformation.click()
    playername = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div/div/div[3]/form/div[2]/div[1]/div[2]/div[2]/div/div/input")
    playername.send_keys(playername1)
    findbotton = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/main/div[2]/div/div/div/div[3]/form/div[2]/div[2]/button[1]")
    findbotton.click()
    #滑動到指定元素
    element = driver.find_element(By.CSS_SELECTOR, ".MuiTableCell-root .MuiBox-root div:nth-of-type(1)")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    # 初始化變數
    point1 = None
    money1 = None
    stone1 = None
    #取得點數、日金、寶石文本
    try:
        # 等待點數元素存在
        point_location = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, QATX1))
        )
        
        # 获取元素的文本内容
        point1 = point_location.text
        # print(point1)

    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        # 等待日金元素存在
        moneylocation = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, QATX2))
        )
        
        # 获取元素的文本内容
        money1 = moneylocation.text
        # print(money1)

    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        # 等待寶石元素存在
        stonelocation = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, QATX3))
        )
        
        # 获取元素的文本内容
        stone1 = stonelocation.text
        stone1 = float(stone1.replace(',', ''))
        stone1 = round(stone1,2)
        stone1 = f"{stone1:,.2f}"
        # print(f"{stone1}")
        driver.quit
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit
    return point1,money1,stone1
   

def off_player_manage(driver): #前台取得點數、日金、寶石文本
        # 初始化變數
    point2 = None
    money2 = None
    stone2 = None
    try:
        # 等待點數元素存在
        point_location = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "signInFloat_userBagItemPoint__D_m6y"))
        )
        
        # 获取元素的文本内容
        point2 = point_location.text
        # print(point2)

    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        # 等待日金元素存在
        moneylocation = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "signInFloat_userBagItemCoin__RvGZH"))
        )
        
        # 获取元素的文本内容
        money2 = moneylocation.text
        # print(money2)

    except Exception as e:
        print(f"An error occurred: {e}")
    try:
        # 等待寶石元素存在
        stonelocation = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "signInFloat_userBagItemGem__13WS0"))
        )
        
        # 获取元素的文本内容
        stone2 = stonelocation.text
        # print(stone2)

    except Exception as e:
        print(f"An error occurred: {e}")
    return point2,money2,stone2


def compare_values(bpm, opm):
    labels = ["點數", "日金", "寶石"]

    for i in range(3):
        if bpm[i] == opm[i]:
            print(f"{labels[i]}前後台吻合")
        else:
            print(f"{labels[i]}不吻合")



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




def test_wait_for_text_in_element(driver,Version):#找版號
    
    try:
        # 设置等待条件和超时时间
        wait = WebDriverWait(driver,5)
        
        # 等待指定元素中包含指定的文本
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/p"), Version))
        
        print("Match", Version)
       
    except: 
            print("版號錯誤")




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
    # 找到立即登录按钮并点击
    sign_in_button = driver.find_element(By.CLASS_NAME, "signInFloat_signInButton___h228")
    sign_in_button.click()
    
    # 找到 Google 三方登录按钮
    login_btn_google = driver.find_element(By.CLASS_NAME, "signIModal_loginBtnGoogle__bFsCU")
    
    # 创建 ActionChains 对象
    actions = ActionChains(driver)
    
    # 将鼠标移动到按钮上并点击
    actions.move_to_element(login_btn_google).click(login_btn_google).perform()
    time.sleep(5)





def click_and_switch_to_appstore(driver):#轉導至APPSTORE後再回官網
    try:
        # 點擊 App Store
        appstore = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div[2]/div/a[1]/picture/img")
        appstore.click()
        original_handle = driver.current_window_handle
        time.sleep(1.5)
        
        # 获取所有窗口句柄
        handles = driver.window_handles
        
        # 切换到新开的浏览器窗口
        new_handle = [handle for handle in handles if handle != original_handle][-1]
        driver.switch_to.window(new_handle)
    
        
        # # 明確等待新窗口的標題出現
        # WebDriverWait(driver, 10).until(EC.title_contains("在 App Store 上的「日不落城」"))
        
        # 获取新窗口的标题
        
        window_title = driver.title
        print("Window Title:", window_title)
        

        # 切換回原始窗口
        driver.switch_to.window(original_handle)

    except:
        print("AppStore轉導失敗:")
        driver.switch_to.window(original_handle)


def click_nowplaybuttons(driver):  #立即玩
    try:
        # 点击立即玩按钮
        button1 = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[1]")
        button1.click()
        time.sleep(1)

        # 点击我的最爱
        my_love = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/ul/li[2]")
        my_love.click()
        time.sleep(1)

        # 点击老虎机
        slot = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/ul/li[3]")
        slot.click()
        time.sleep(1)

        # 点击真人
        live = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/ul/li[4]")
        live.click()
        time.sleep(1)

        # 点击捕鱼
        fish = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/ul/li[5]")
        fish.click()
        time.sleep(1)

        # 点击全部游戏
        all_game = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/ul/li[1]")
        all_game.click()
        time.sleep(1)

        # 点击日不落
        sunrise = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/div[1]/div[2]")
        sunrise.click()
        time.sleep(1)

        # 点击BNG
        bng = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/div[1]/div[3]")
        bng.click()
        time.sleep(1)

        # 点击皇家电子
        rsg = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/div[1]/div[4]")
        rsg.click()
        time.sleep(1)
        
        #點擊ATG
        ATG = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[1]/div[5]")
        ATG.click()
        time.sleep(1)
    
        print("立即完流程正確") 
    except:print("立即完失敗")


def click_news(driver):  #最新消息
    try:
        #點擊最新消息
        news = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/nav/ul/li[2]")
        news.click()
        time.sleep(1)
        #點擊活動
        activity = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/ul/li[2]")
        activity.click()
        time.sleep(1)
        #點擊維護
        repair = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/ul/li[3]")
        repair.click()
        time.sleep(1)
        #點擊其他
        other = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/ul/li[4]")
        other.click()
        time.sleep(1)
        #點擊全部
        All = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/ul/li[1]")
        All.click()
        time.sleep(1)
        #點擊全部-活動
        AllActivity = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div/div/div[1]/span[1]")
        AllActivity.click()
        time.sleep(1)
        #點擊關閉
        close = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div[3]/div/div/button[1]")
        close.send_keys(Keys.ENTER)
        time.sleep(1)
        print("最新消息流程正確")
        time.sleep(1)
    except:print("最新消息流程異常")

  
            
def click_Beginner(driver):  #新手必看-遊戲攻略
    try:
        #點擊新手必看
        BeginnerLook = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/nav/ul/li[3]/div/span")
        BeginnerLook.click()
        time.sleep(1)
        #點擊攻略
        Stategy = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/nav/ul/li[3]/ul/li/div")
        time.sleep(1)
        Stategy.click()
        time.sleep(1)
        #點擊文章
        Papper = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div/a[1]")
        Papper.click()
        time.sleep(3)
        driver.back()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        print("新手必看流程正確")
        time.sleep(1)
    except:print("遊戲攻略流程失敗")


def special_game(driver): #新手必看-特色遊戲
    try:
        #點擊新手必看
        BeginnerLook = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/nav/ul/li[3]/div/span")
        BeginnerLook.click()
        time.sleep(1)
        #點擊特色遊戲
        special_game_btn = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/nav/ul/li[3]/ul/li[2]") 
        special_game_btn.click()
        time.sleep(1)
        #點擊發大財
        game10001 = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div/div/div[1]")
        game10001.click()
        time.sleep(1)
        #點擊開始遊戲
        startgame = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/article/picture/img")
        startgame.click()
        # 设置等待条件和超时时间
        wait = WebDriverWait(driver,5)
        # 找到請點擊下方按鈕
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,"download_title__kLsaG"), "請點擊下方按鈕"))
        print("特色遊戲流程正確","Match", "請點擊下方按鈕")
    except:print("特色遊戲流程失敗")
        
    
def VIP_directions(driver):  #新手必看-VIP說明
    try:
        #點擊新手必看
        BeginnerLook = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/nav/ul/li[3]/div/span")
        BeginnerLook.click()
        time.sleep(1)
        #點擊VIP說明
        VIP_directions_btn = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/nav/ul/li[3]/ul/li[3]")
        VIP_directions_btn.click()
        time.sleep(1)
        #找到金卡首儲文案
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/div/div/table/tbody/tr[1]/td[4]"),"首儲"))
        print("Match", "找到VIP說明金卡首儲文案")
    except:print("VIP說明文案異常")


def gift_directions(driver):  #新手必看-贈禮說明
    try:
        #點擊新手必看
        BeginnerLook = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/nav/ul/li[3]/div/span")
        BeginnerLook.click()
        time.sleep(1)
        #點擊贈禮說明
        gift_directions_btn = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/nav/ul/li[3]/ul/li[4]")
        gift_directions_btn.click()
        time.sleep(1)
        #找到文案
        wait = WebDriverWait(driver,5)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,"/html/body/div/div/div/div[4]/ol/li[1]"),"綁定門號：可收禮"))
        print("Match", "找到贈禮說明文案")
    except:print("贈禮說明文案異常")    





def click_Rank(driver):  #活動排行
    try:
        #點擊活動排行
        Rank = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[4]")
        Rank.click()
        time.sleep(1)
        #點擊富豪榜
        RicherRank = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[4]/ul/li/div")
        RicherRank.click()
        time.sleep(1)
        print("活動排行流程正確")
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
    except:print("活動排行流程異常")

 


def mycard_purchase(driver, mycard_account, mycard_password, pay_password):#測試環境購點流程
    try:
        driver.refresh
        time.sleep(1)
        # 点击購點兌換
        BuyCash = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[5]")
        BuyCash.click()
        time.sleep(1)

        # 点击購點
        Buy = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[5]/ul/li[1]")
        Buy.click()
        time.sleep(1)

        # 点击Mycard線上扣點
        MyCardBuy = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/div[2]/div/div[1]/button[6]")
        MyCardBuy.click()
        time.sleep(1)

        # 点击S150面額
        TWD150 = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[2]/button")
        TWD150.click()
        time.sleep(1)

        # 点击確認
        BuyButton = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/div[2]/div/div[2]/div[2]/div/div/div[3]/button[2]")
        BuyButton.click()
        time.sleep(1)

        # 输入mycard帳號
        MyCardAccount = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/form/div[3]/ul/li[1]/div/div/input[1]")
        MyCardAccount.send_keys(mycard_account)
        time.sleep(1)

        # 输入mycard密碼
        MyCardPassword = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/form/div[3]/ul/li[2]/div/input")
        MyCardPassword.send_keys(mycard_password)
        time.sleep(1)

        # 点击mycard確認
        MyCardlogin = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/form/div[3]/div")
        MyCardlogin.click()
        time.sleep(5)

        # 输入支付密碼
        PayPassword = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/form/ul/li[3]/input")
        PayPassword.send_keys(pay_password)
        time.sleep(2)

        # 点击確認
        MycardOK = driver.find_element(By.CLASS_NAME,"btn")
        MycardOK.send_keys(Keys.ENTER)
        time.sleep(1)

        # 点击購點成功確認
        SuccessBuy = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[3]/button[2]")
        SuccessBuy.click()
        time.sleep(1)

        print("購點流程正確") 
        driver.refresh()
    except:
        print("購點流程失敗")
        driver.refresh()

    
def point_exchange(driver, exchangepoint): #測試環境購點兌換 
    try:
        # 點擊購點兌換
        BuyExchange = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/nav/ul/li[5]/div")
        BuyExchange.click()
        time.sleep(1)

        # 點擊點數兌換
        PointExchange = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/nav/ul/li[5]/ul/li[2]")
        PointExchange.click()
        time.sleep(1)

        # 輸入兌換點數
        ExchangePoint = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/div[1]/div/input")
        ExchangePoint.send_keys(exchangepoint)
        time.sleep(1)

        # 點擊確認
        ExchangeButton = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/div[2]/div/button")
        ExchangeButton.click()
        time.sleep(1)

        # 再次點擊確認
        DubleConfirm = driver.find_element(By.CLASS_NAME,"styles_secondaryButton__9LRf_")
        DubleConfirm.click()
        time.sleep(1)

        # 點擊兌換成功確定
        SuccessConfirm = driver.find_element(By.CLASS_NAME,"styles_secondaryButton__9LRf_")
        SuccessConfirm.click()
        time.sleep(1)
        print("兌換流程正確")
        driver.refresh()
    except:
        print("兌換失敗:")
        driver.refresh()


def barcode_exchange(driver):  #兌換碼兌換流程
    try:
        # 點擊購點兌換
        BuyExchange = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/nav/ul/li[5]")
        BuyExchange.click()
        time.sleep(1)

        # 點擊兌換碼兌換
        BarcodeExchange = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/nav/ul/li[5]/ul/li[3]")
        BarcodeExchange.click()
        print("兌換碼兌換流程正確")
        driver.refresh()
    except:print("兌換碼兌換流程異常")



def click_service_center_and_information(driver):  #客服中心-客服資訊
    try:
        # 點擊客服中心
        ServiceCenter = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[6]")
        ServiceCenter.click()
        time.sleep(1)

        # 點擊客服資訊
        ServiceInformation = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[6]/ul/li[1]")
        ServiceInformation.click()
        time.sleep(1)
    except:print("客服資訊流程異常")

    



def click_official_line_and_switch_to_new_window(driver):  #點擊客服官方LINE
    try:
        # 點擊官方Line
        OffficalFB = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/div/div/div[2]/a[1]")
        OffficalFB.click()
        
        # 获取当前窗口句柄
        original_handle = driver.current_window_handle
        
        
        # 切換到新開的瀏覽器窗口
        handles = driver.window_handles
        new_handle = [handle for handle in handles if handle != original_handle][-1]
        driver.switch_to.window(new_handle)


        # 获取新窗口的标题
        window_title = driver.title
        print("Window Title:", window_title)
        
        # 切換回原始窗口
        driver.switch_to.window(original_handle)
    except:
        print("客服Line官網失敗")
        driver.switch_to.window(original_handle)


def click_official_FB_and_switch_to_new_window(driver):  #點擊客服官方FB
    try:
        # 點擊官方FB
        OffficalFB = driver.find_element(By.XPATH, "/html/body/div/div/div/div[4]/div/div/div[2]/a[2]/div")
        OffficalFB.click()
        
        # 获取当前窗口句柄
        original_handle = driver.current_window_handle
    
        # 获取所有窗口句柄
        handles = driver.window_handles
        
        # 切换到新开的浏览器窗口
        new_handle = [handle for handle in handles if handle != original_handle][-1]
        driver.switch_to.window(new_handle)
        
        # 获取新窗口的标题
        window_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//title"))).get_attribute("innerText")
        print("Window Title:", window_title)
        
        # 切換回原始窗口
        driver.switch_to.window(original_handle) 
    except Exception as e:
        print("Error:", e)
        print("客服FB官網失敗")
        driver.switch_to.window(original_handle)



def click_service_center_and_question(driver): #客服中心-常見問題
    try:
        # 點擊客服中心
        ServiceCenter = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[6]")
        ServiceCenter.click()
        time.sleep(1)
        
        # 點擊常見問題
        question = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[6]/ul/li[2]")
        question.click()
        time.sleep(1)

        #點擊防詐騙
        FQA = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/ul/li[2]")
        FQA.click()
        print("客服中心-常見問題流程正確")
    except:
        print("客服中心-常見問題失敗")




def click_service_center_and_list(driver):  #客服中心-停權名單
    try:
        # 點擊客服中心
        ServiceCenter = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[6]")
        ServiceCenter.click()
        time.sleep(1)
        
        # 點擊停權名單
        List = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[6]/ul/li[3]")
        List.click()
        time.sleep(1)
        print("客服中心-停權名單流程正確")
    except:
        print("客服中心-停權名單失敗")





def service_center_and_document(driver):  #客服中心-使用者規章
    try:
        # 點擊客服中心
        ServiceCenter = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[6]")
        ServiceCenter.click()
        time.sleep(1)
        
        # 點擊使用者規章
        Document = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[6]/ul/li[4]")
        Document.click()
        time.sleep(1)

        #點擊遊戲規章
        Gamedocument = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/ul/li[2]")
        Gamedocument.click()
        time.sleep(1)
        #點擊隱私條款
        Privacy = driver.find_element(By.XPATH,"/html/body/div/div/div/div[4]/ul/li[3]")
        Privacy.click()
        print("客服中心-使用者規章流程正確")   
    except:
        print("客服中心-使用者規章失敗") 




def service_center_and_ApplicationDocument(driver):  #客服中心-申請文件
    try:
        # 點擊客服中心
        ServiceCenter = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[6]")
        ServiceCenter.click()
        time.sleep(1)
        
        # 點擊申請文件
        ApplicationDocument = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[6]/ul/li[5]")
        ApplicationDocument.click()
        time.sleep(1)
        print("客服中心-申請文件流程正確")
    except:
        print("客服中心-申請文件失敗")   




def navigate_to_member_file(driver): #會員中心-會員檔案
    try:
        # 點擊會員中心
        membercenter = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[7]")
        membercenter.click()
        time.sleep(1)

        # 點擊會員檔案
        memberfile = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[7]/ul/li[1]")
        memberfile.click()
        time.sleep(1)
        
        print("點擊會員檔案流程正確")
    except Exception as e:
        print("Error:", e)




def VIP_member_file(driver,text): #會員中心-會員檔案vip
    try:
        # 设置等待条件和超时时间
        wait = WebDriverWait(driver, 10)
        time.sleep(1)  # 可选的等待时间
        
        # 等待指定元素中包含指定的文本
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div/div/div/div[4]/div/div/div/div/div/div[4]/div[2]"), text))
        time.sleep(1)  # 可选的等待时间                          
        print("找到會員VIP等級", text)
    except Exception as e:
        print("Error:", e)



def Passbook(driver):#會員中心-我的存摺

    try:
        # 點擊會員中心
        membercenter = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[7]")
        membercenter.click()
        time.sleep(1)

        # 點擊我的存摺
        Mypassbook = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[7]/ul/li[2]")
        Mypassbook.click()
        time.sleep(1)
        
        print("點擊我的存摺流程正確")
    except Exception as e:
        print("Error:", e)


def  Passbook_text(driver):#會員中心-我的存摺文案
    try:
        # 设置等待条件和超时时间
        wait = WebDriverWait(driver, 5)
        time.sleep(1)  # 可选的等待时间
        
        # 等待指定元素中包含指定的文本
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div/div/div/div[4]/div/div"), "僅顯示最近14日紀錄"))
        time.sleep(1)  # 可选的等待时间
        
        print("找到存摺文案","僅顯示最近14日紀錄")
    except Exception as e:
        print("Error:", e)



def member_center_and_gift(driver):  #會員中心-贈禮
    try:
        # 點擊會員中心
        membercenter = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[7]")
        membercenter.click()
        time.sleep(1)
        
        # 點擊贈禮
        give = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[7]/ul/li[3]")
        give.click()
        time.sleep(1)
    
        print("成功點擊會員中心和贈禮")
    
    except:
            try:
                #點擊立即下載
                nowdownload = driver.find_element(By.CLASS_NAME,"downloadInfo_btnBox__3_uTQ")
                nowdownload.click()
                
                time.sleep(1)

                # 點擊贈禮
                give = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/nav/ul/li[7]/ul/li[3]")
                give.click()
                time.sleep(1)
                print("成功點擊會員中心和贈禮")

            except Exception as e:
                print("Error:", e)



def find_for_gift_in_element(driver): #找贈禮文案
    try:
        # 设置等待条件和超时时间
        wait = WebDriverWait(driver, 5)
        time.sleep(1)  # 可选的等待时间
        
        # 等待指定元素中包含指定的文本
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div/div/div/div[4]/div/div/div/div[1]/div[1]"), "贈禮說明"))
        time.sleep(1)  # 可选的等待时间
        

        print("找到贈禮文案", "贈禮說明")

    except Exception as e:
        print("Error:", e)


def chatroom(driver): #聊天室
    #回首頁
    front_page = driver.find_element(By.CLASS_NAME,"navBar_logoBox__0qiY9")
    front_page.click()
    time.sleep(1)
    #點擊聊天室
    chatroom_btn = driver.find_element(By.CLASS_NAME,"chatFloat_chatTitle__V4ITL")
    chatroom_btn.click()
    time.sleep(1)
    #點擊私訊聊天
    private_message = driver.find_element(By.XPATH,"/html/body/div/div/div/div[10]/div[2]/div[2]/div[2]")
    private_message.click()
    time.sleep(1)
    #點擊收起
    close = driver.find_element(By.CSS_SELECTOR,"svg[data-testid='FormatIndentIncreaseIcon']")
    close.click()
    time.sleep(1)
    #點擊向下
    down = driver.find_element(By.CSS_SELECTOR,"svg[data-testid='ExpandMoreIcon']")
    down.click()
    time.sleep(1)
    print("聊天室功能正常")



    



















        







