import pytest

from lib.test import Trww


@pytest.fixture(scope='module')
def inDeviceModelMgr():
    Trww.loginAndCheck('','admin','QQQ111..')

def test_testIP():
    poptext = Trww.changeIP('uu','172.16.16.51')
    assert poptext == 'The address is not used.'

