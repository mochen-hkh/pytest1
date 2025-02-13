import pytest
from lib.webUI import *

from selenium.webdriver.common.by import By


@pytest.fixture(scope='module')
def inFit():
    LoginAndCheck('admin','QQQ111..')

def test_fit_network(inFit):
    webDriver().find_element(By.XPATH,'//*[@id="options"]/a').click()
    webDriver().find_element(By.XPATH,'//*[@id="optMenu"]/dl/dt[3]/a').click()
    webDriver().find_element(By.XPATH,'//*[@id="ip"]').send_keys('172.16.16.53')
    webDriver().find_element(By.XPATH,'//*[@id="subNetMask"]').send_keys('255.255.252.0')
    webDriver().find_element(By.XPATH,'//*[@id="gateway"]').send_keys('172.16.19.254')
    webDriver().find_element(By.XPATH,'//*[@id="dns1Ip"]').send_keys('114.114.114.114')
    webDriver().find_element(By.XPATH, '//*[@id="ipTest"]').click()
    time.sleep(15)
    poptext = webDriver().find_element(By.XPATH,'//*[@id="alertBlock"]/div').text
    print(poptext)
    assert poptext == '改地址尚未被使用'
webui.LoginAndCheck





