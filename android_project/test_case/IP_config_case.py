#coding:utf-8
from page_object.IP_config_page import IPConfigPage
from model import myunit,driverwait, function
from page_object.login_page import LoginPage
import time,sys
sys.path.append('./model')
sys.path.append('./page_obj')

class IPConfigTest(myunit.MyTest):


    def test_ip_address_null(self):
        '''ip地址为空保存'''
        ipo = IPConfigPage(self.driver)
        ipo.open()
        LoginPage(self.driver).click_ip_btn()
        ipo.ipconfig_action(" ")
        self.assertEqual(ipo.ip_setting_title(),u"配置信息",msg= u"失败原因:校验元素失败")
        print(u"IP配置失败")
        function.insert_image(self.driver,"ip_address_null.jpg")

    def test_ip_address_error(self):
        '''ip地址格式错误'''
        ipo = IPConfigPage(self.driver)
        LoginPage(self.driver).click_ip_btn()
        ipo.open()
        ipo.ipconfig_action("172.16.12.22a")
        self.assertEqual(ipo.ip_setting_title(), u"配置信息", msg=u"失败原因:校验元素失败")
        print(u"IP配置失败")
        function.insert_image(self.driver,"ip_address_error.jpg")

    def test_ip_address_success(self):
        '''ip地址格式正确'''
        ipo = IPConfigPage(self.driver)
        lpo = LoginPage(self.driver)
        lpo.click_ip_btn()
        ipo.ipconfig_action("172.16.12.223")
        # print(lpo.login_title())
        # self.assertEqual(lpo.login_title(), u"帐号登录", msg=u"失败原因:校验元素失败")
        # print(u"IP配置成功")
        result= driverwait.find_toast(self.driver, "保存成功")
        print(u"配置IP信息结果为：%s" % result)
        function.insert_image(self.driver, "ip_address_success.jpg")


if __name__ == '__main__':
    IPConfigTest().test_ip_address_success()





