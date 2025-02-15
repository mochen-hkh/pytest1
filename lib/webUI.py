from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from cfg.cfg_1 import *
import time



def LoginAndCheck(username,password):
    wd = webdriver.Chrome(service=Service('F:/py脚本/pythonProject/chromedriver-win64/chromedriver-win64/chromedriver.exe'))
    wd.implicitly_wait(10)
    wd.get(WEB_ADDRESS)
    # ac = ActionChains(wd)
    wd.maximize_window()
    wd.find_element(By.XPATH,'//*[@id="uiSelect"]/span').click()
    wd.find_element(By.XPATH,'//*[@id="uiSelect"]/div/div/ul/li[1]').click()
    time.sleep(1)
    if username is not None:
        wd.find_element(By.XPATH,'//*[@id="userName"]').send_keys(username)
    if password is not None:
        wd.find_element(By.XPATH, '//*[@id="pwd"]').send_keys(password)
    # wd.find_element(By.XPATH,'//*[@id="loginDlg"]/div[3]/i[2]').click()
    # time.sleep(1)
    wd.find_element(By.XPATH, '//*[@id="loginDlg"]/div[5]/button').click()
    time.sleep(1)
    try:
        popText = wd.find_element(By.XPATH, '//*[@id="tipEdit"]/div[2]').text
    except:
        print(1)
    if popText != '':
        wd.quit()
        return popText
    try:
        popText = wd.find_element(By.XPATH, '//*[@id="alertBlock"]/div').text
    except:
        print(2)
    if popText != '':
        wd.quit()
        return popText
    wd.quit()
    return

def ChangeIP(username,password,ipv4,ipv4_1):
    # subnet_mask, default_gateway, dns_server
    wd = webdriver.Chrome(
        service=Service('F:/py脚本/pythonProject/chromedriver-win64/chromedriver-win64/chromedriver.exe'))
    wd.implicitly_wait(10)
    wd.get(WEB_ADDRESS)
    # ac = ActionChains(wd)
    wd.maximize_window()
    # wd.find_element(By.XPATH, '//*[@id="uiSelect"]/span').click()
    # wd.find_element(By.XPATH, '//*[@id="uiSelect"]/div/div/ul/li[1]').click()
    time.sleep(1)
    if username is not None:
        wd.find_element(By.XPATH, '//*[@id="userName"]').send_keys(username)
    if password is not None:
        wd.find_element(By.XPATH, '//*[@id="pwd"]').send_keys(password)
    wd.find_element(By.XPATH, '//*[@id="loginDlg"]/div[5]/button').click()
    time.sleep(2)
    wd.find_element(By.XPATH, '//*[@id="options"]/a').click()
    time.sleep(1)
    wd.find_element(By.XPATH, '//*[@id="optMenu"]/dl/dt[3]/a').click()
    time.sleep(1)
    input_box = wd.find_element(By.XPATH, '//*[@id="ip"]')
    input_box.clear()
    input_box.send_keys(ipv4)
    # wd.find_element(By.XPATH, '//*[@id="ipTest"]').click()
    # time.sleep(8)
    # text = wd.find_element(By.XPATH, '//*[@id="alertBlock"]/div').text
    while True:
        wd.find_element(By.XPATH, '//*[@id="ipTest"]').click()
        time.sleep(12)
        text = wd.find_element(By.XPATH, '//*[@id="alertBlock"]/div').text
        if text == 'The address is used.':
            wd.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/button').click()
            input_box = wd.find_element(By.XPATH, '//*[@id="ip"]')
            input_box.clear()
            input_box.send_keys(ipv4_1)
        else:
            break
    wd.quit()
    return text










