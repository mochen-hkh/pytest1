from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def LoginAndCheck(username,password):
    wd = webdriver.Chrome(service=Service('F:/py脚本/pythonProject/chromedriver-win64/chromedriver-win64/chromedriver.exe'))
    wd.implicitly_wait(10)
    wd.get('http://172.16.16.51')
    # ac = ActionChains(wd)
    wd.maximize_window()
    wd.find_element(By.XPATH,'//*[@id="uiSelect"]/span').click()
    wd.find_element(By.XPATH,'//*[@id="uiSelect"]/div/div/ul/li[1]').click()
    time.sleep(1)
    if username is not None:
        wd.find_element(By.XPATH,'//*[@id="userName"]').send_keys(username)
    if password is not None:
        wd.find_element(By.XPATH, '//*[@id="pwd"]').send_keys(password)
    wd.find_element(By.XPATH,'//*[@id="loginDlg"]/div[3]/i[2]').click()
    time.sleep(1)
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

LoginAndCheck('admin','123456')



