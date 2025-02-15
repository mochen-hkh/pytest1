import pytest
from lib.webUI import *
def test_testIP():
    poptext = ChangeIP('admin','QQQ111..','172.16.16.51','172.16.16.52')
    assert poptext == 'The address is not used.'









