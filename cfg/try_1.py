from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class clss:
    def __init__(self,option):
        self.option =option
class SMP_UI:
    def _init__(self,):
        options = webdriver.chromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.wd = webdriver.Chrome(service=Service('F:/py脚本/pythonProject/chromedriver-win64/chromedriver-win64/chromedriver.exe'))
        self.wd.implicitly_wait(10)
SMP_UI = SMP_UI()