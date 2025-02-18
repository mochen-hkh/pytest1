from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from cfg.cfg_1 import WEB_ADDRESS,DIVER_URL

class Trww:
    def __init__(self):

        self.wd = webdriver.Chrome(
            service=Service(DIVER_URL))
        self.wd.implicitly_wait(10)

    def loginAndCheck_1(self,username,password):

        self.wd.get(WEB_ADDRESS)
        self.wd.maximize_window()
        time.sleep(1)
        if username is not None:
            self.wd.find_element(By.XPATH,'//*[@id="userName"]').send_keys(username)
        if password is not None:
            self.wd.find_element(By.XPATH, '//*[@id="pwd"]').send_keys(password)
        self.wd.find_element(By.XPATH, '//*[@id="loginDlg"]/div[5]/button').click()
        time.sleep(2)
        self.wd.find_element(By.XPATH, '//*[@id="options"]/a').click()
        time.sleep(1)
        self.wd.find_element(By.XPATH, '//*[@id="optMenu"]/dl/dt[3]/a').click()
        time.sleep(1)
        self.wd.find_element(By.XPATH, '//*[@id="localNet-email"]/a').click()
        time.sleep(2)

    def emailTestALL(self,Sender_Address,Server_Address):

        ele = self.wd.find_element(By.XPATH, '//*[@id="iptSmtpSender"]')
        ele.clear()
        ele.send_keys(Sender_Address)
        ele = self.wd.find_element(By.XPATH, '//*[@id="iptSmtpSvr"]')
        ele.clear()
        ele.send_keys(Server_Address)
        time.sleep(2)
    def emailTest01(self,User_Name,User_Password,Confirm,Receiver_Address1):
        select = Select(self.wd.find_element(By.ID,'selSmtpUpload'))
        select.select_by_visible_text('MESSAGE')
        select = Select(self.wd.find_element(By.ID, 'smtpEncryptionType'))
        select.select_by_visible_text('NONE')
        ele = self.wd.find_element(By.XPATH, '//*[@id="iptSmtpUser"]')
        ele.clear()
        ele.send_keys(User_Name)
        ele = self.wd.find_element(By.XPATH, '//*[@id="iptSmtpPwd"]')
        ele.clear()
        ele.send_keys(User_Password)
        ele = self.wd.find_element(By.XPATH, '//*[@id="iptSmtpPwd2"]')
        ele.clear()
        ele.send_keys(Confirm)
        ele = self.wd.find_element(By.XPATH, '//*[@id="iptSmtpRecv1"]')
        ele.clear()
        ele.send_keys(Receiver_Address1)
        self.wd.find_element(By.XPATH, '//*[@id="advSmtp"]/div[10]/span[3]/button').click()
        time.sleep(7)
        self.wd.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/button/span').click()
t = Trww()








