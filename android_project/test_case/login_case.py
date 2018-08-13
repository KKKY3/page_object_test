#coding:utf-8
from paperless_project.android_project.test_case.model import myunit, driverwait,function
from page_object.login_page import LoginPage
from paperless_project.android_project.test_case.page_object.IP_config_page import IPConfigPage


class LoginTest(myunit.MyTest):

    def test_login_user_null(self):
        '''用户名为空'''
        #配置IP地址
        ipo = IPConfigPage(self.driver)
        lpo = LoginPage(self.driver)
        lpo.click_ip_btn()
        ipo.ipconfig_action("172.16.12.223")
        #配置登录信息
        lpo.login_action("","")
        result = driverwait.find_toast(self.driver, u'账号为空')
        print(u"用户名和密码为空校验结果%s"%result)
        function.insert_image(self.driver, "login_user_null.jpg")


    def test_login_pwd_null(self):
        '''密码为空'''
        # 配置IP地址
        ipo = IPConfigPage(self.driver)
        lpo = LoginPage(self.driver)
        lpo.click_ip_btn()
        ipo.ipconfig_action("172.16.12.223")
        # 配置登录信息
        lpo.login_action("fourf", "")
        result = driverwait.find_toast(self.driver, u'密码')
        print(u"密码为空校验结果：%s" % result)
        function.insert_image(self.driver, "login_pwd_null.jpg")

    def test_login_user_pwd_error(self):
        '''用户名或者密码错误'''
        # 配置IP地址
        ipo = IPConfigPage(self.driver)
        lpo = LoginPage(self.driver)
        lpo.click_ip_btn()
        ipo.ipconfig_action("172.16.12.223")
        # 配置登录信息
        lpo.login_action("fourfd", "145278")
        result = driverwait.find_toast(self.driver, u'账号不存在')
        print(u"密码为空校验结果：%s" % result)
        function.insert_image(self.driver, "login_user_pwd_error.jpg")

    def test_login_sucess(self):
        '''用户名和密码正常'''
        # 配置IP地址
        ipo = IPConfigPage(self.driver)
        lpo = LoginPage(self.driver)
        lpo.click_ip_btn()
        ipo.ipconfig_action("172.16.12.223")
        # 配置登录信息
        lpo.login_action("fourf", "123456")
        result = driverwait.find_toast(self.driver, "会议列表")
        print(u"登录成功：%s"%result)
        function.insert_image(self.driver, "login_success.jpg")


if __name__ == '__main__':
    LoginTest.test_login_user_pwd_error()