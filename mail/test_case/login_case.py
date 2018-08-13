#coding:utf-8

from time import sleep
import unittest,random,sys
from model import  myunit,function
from page_object.paperless_menu_page import Paperless_menu_page
from page_object.login_Page import LoginPage
sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):


    def test_login_user_pwd_null(self):
        '''用户名，密码为空登录'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action("", "")
        sleep(2)
        print(po.login_error_hint())
        self.assertEqual(po.login_error_hint(),"请输入帐号！")
        function.insert_img(self.driver, "user_pwd_null.jpg")

    def test_login_pwd_null(self):
        '''密码为空登录'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action("admin","")
        sleep(2)
        print(po.login_error_hint())
        self.assertEqual(po.login_error_hint(),"请输入密码！")

        function.insert_img(self.driver,"pwd_null.jpg")

    def test_login_user_pwd_error(self):
        '''用户名或者密码错误'''
        po = LoginPage(self.driver)
        po.open()
        charactor = random.choice("zxcvbnmasdfghjklqwertyuiop")
        username = "test" + charactor
        po.login_action(username,"2222")
        sleep(2)
        print(po.login_error_hint())
        self.assertEqual(po.login_error_hint(),"帐号不存在!")
        function.insert_img(self.driver, "user_pwd_error.jpg")


    def test_login_success(self):
        '''用户名，密码正确，登录成功'''
        po = LoginPage(self.driver)
        po.open()

        user = "admin"
        po.login_action(user, "admin")
        sleep(2)
        po2 = Paperless_menu_page(self.driver)
        print(po2.login_success_user())
        self.assertEqual(po2.login_success_user(),"管理员")
        function.insert_img(self.driver, "success.jpg")