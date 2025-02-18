from lib.email import *
import pytest
@pytest.fixture(scope='module')
def inDeviceModelMgr_1():
    t.loginAndCheck_1('admin','QQQ111..')
    yield

def test_email001(inDeviceModelMgr_1):
    t.emailTestALL('2891310023@qq.com','SMP.qq.com')
    poptext = t.emailTest01('2891310023@qq.com','qazQAZ132^','qazQAZ132^','huangkaihuilongse@dingtalk.com')
    assert poptext == 'Testing failed.'
