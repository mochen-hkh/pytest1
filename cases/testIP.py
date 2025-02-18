import pytest

from lib.IP import *
from cfg.cfg_1 import *

#
@pytest.fixture(scope='module')
def inDeviceModelMgr():
    t.loginAndCheck('admin','QQQ111..')
    yield


def test_testIP001(inDeviceModelMgr):
    poptext = t.changeIP('172.16.16.51')
    assert poptext == 'The address is used.'
    t.wd.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/button/span').click()


def test_testIP002(inDeviceModelMgr):
    poptext = t.changeIP('172.16.16.52')
    assert poptext == 'The address is not used.'

