import pytest
from lib.webUI import LoginAndCheck

class Test_登录:
    def test_UI_0001(self):
        popText = LoginAndCheck('admin','123456')
        assert popText == '当前密码过于简单，请修改密码!'


    def test_UI_0002(self):
        popText = LoginAndCheck(None,'123456')
        assert popText == '请输入用户名'

    def test_UI_0003(self):
        popText = LoginAndCheck('admin', None)
        assert popText == '请输入密码'

    def test_UI_0004(self):
        popText = LoginAndCheck('admi', '123456')
        assert popText == '用户名或密码不正确'

    def test_UI_0005(self):
        popText = LoginAndCheck('admin', '12345')
        assert popText == '用户名或密码不正确'

    def test_UI_0006(self):
        popText = LoginAndCheck('ad', '12gfdg')
        assert popText == '用户名或密码不正确'