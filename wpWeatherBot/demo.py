from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
import win32clipboard
import pyautogui
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 




driver = webdriver.Chrome()
driver.get("https://goo.gl/WCS3hC")

wait = WebDriverWait(driver, 600)
driver.maximize_window()

driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get("https://www.google.com.tr/")

wait = WebDriverWait(driver, 600)



name = 'Kullanıcı'
#buraya mesaj alıp göndermek istediğiniz kullanıcı adı veya grup adını giriniz


driver.switch_to.window(driver.window_handles[0])

input('Enter anything after scanning QR code')


user = driver.find_element(By.XPATH, '//span[@title = "{}"]'.format(name))
user.click()

box = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
box.send_keys("Hava durumunu öğrenmek istediğiniz il veya ilçeyi giriniz" + Keys.ENTER)





def hava(x):
    driver.switch_to.window(driver.window_handles[1])
    try:
        user = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        user.send_keys(x," hava durumu"+ Keys.ENTER)
        memleket = driver.find_element(By.XPATH, " //*[@id='wob_loc']").text
        derece = driver.find_element(By.XPATH, "//*[@id='wob_tm']").text
        durum = driver.find_element(By.XPATH, "//*[@id='wob_dc']").text
        driver.switch_to.window(driver.window_handles[0])
        box = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
        box.send_keys(memleket, " : " , derece," derece ve ",durum + Keys.ENTER)
    except:
        user = driver.find_element(By.XPATH, "//*[@id='tsf']/div[1]/div[1]/div[2]/div/div[2]/input")
        user.clear()
        user.send_keys(x," hava durumu"+ Keys.ENTER)
        derece = driver.find_element(By.XPATH, "//*[@id='wob_tm']").text
        durum = driver.find_element(By.XPATH, "//*[@id='wob_dc']").text
        memleket = driver.find_element(By.XPATH, " //*[@id='wob_loc']").text
        driver.switch_to.window(driver.window_handles[0])
        box = driver.find_element(By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
        box.send_keys(memleket, " : " , derece," derece ve ",durum + Keys.ENTER)



def mesajoku():
    global data
    pyautogui.doubleClick(520,665)
    pyautogui.click(520,665)
    pyautogui.hotkey('ctrl', 'c')

    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        hava(data)
    
        
    except TypeError:
        pyautogui.click(1334,663)
        win32clipboard.OpenClipboard()
        win32clipboard.CloseClipboard()



    
x=1
while x < 3:

    time.sleep(5)
    mesajoku()
