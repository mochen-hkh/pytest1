from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

from cfg.cfg_1 import WEB_ADDRESS


# wd = webdriver.Chrome(service=Service('F:/py脚本/pythonProject/chromedriver-win64/chromedriver-win64/chromedriver.exe'))
# wd.implicitly_wait(10)
# wd.get('http://172.16.16.51')
# wd.maximize_window()
# wd.find_element(By.XPATH, '//*[@id="uiSelect"]/span').click()
# wd.find_element(By.XPATH, '//*[@id="uiSelect"]/div/div/ul/li[1]').click()
# time.sleep(1)
#
# wd.find_element(By.XPATH, '//*[@id="userName"]').send_keys('admin')
#
# wd.find_element(By.XPATH, '//*[@id="pwd"]').send_keys('admin123')
# elemnet = wd.find_element(By.XPATH, '//*[@id="loginDlg"]/div[3]/i[2]')
# actions = ActionChains(wd)
# actions.click(elemnet).perform()
# time.sleep(0.5)
# actions.click(elemnet).perform()
# time.sleep(1)
# answer1 = '通过'
# answer2 = '不通过'
# answer = input("是否看到密文及明文显示,请输入YES/NO")
# if answer == 'YES':
#     print(answer1)
#
# if answer == "NO":
#     print(answer2)
# assert answer == 'YES'
#
# wd.quit()
class Trww:
    def __init__(self):

        self.wd = webdriver.Chrome(
            service=Service('F:/py脚本/pythonProject/chromedriver-win64/chromedriver-win64/chromedriver.exe'))
        self.wd.implicitly_wait(10)

    def loginAndCheck(self,username,password):

        self.wd.get(WEB_ADDRESS)
        self.wd.maximize_window()
        # self.wd.find_element(By.XPATH,'//*[@id="uiSelect"]/span').click()
        # self.wd.find_element(By.XPATH,'//*[@id="uiSelect"]/div/div/ul/li[1]').click()
        time.sleep(1)
        if username is not None:
            self.wd.find_element(By.XPATH,'//*[@id="userName"]').send_keys(username)
        if password is not None:
            self.wd.find_element(By.XPATH, '//*[@id="pwd"]').send_keys(password)
        self.wd.find_element(By.XPATH, '//*[@id="loginDlg"]/div[5]/button').click()

    def changeIP(self,ipv4):

        # self.wd.find_element(By.XPATH, '//*[@id="loginDlg"]/div[5]/button').click()
        time.sleep(2)
        self.wd.find_element(By.XPATH, '//*[@id="options"]/a').click()
        time.sleep(1)
        self.wd.find_element(By.XPATH, '//*[@id="optMenu"]/dl/dt[3]/a').click()
        time.sleep(1)
        input_box = self.wd.find_element(By.XPATH, '//*[@id="ip"]')
        input_box.clear()
        input_box.send_keys(ipv4)
        self.wd.find_element(By.XPATH, '//*[@id="ipTest"]').click()
        time.sleep(12)
        text = self.wd.find_element(By.XPATH, '//*[@id="alertBlock"]/div').text
        # self.wd.quit()
        return text
t = Trww()
