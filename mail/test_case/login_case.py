#coding:utf-8

from time import sleep
import unittest,random,sys
from model import  myunit,function
from page_object.paperless_login_page import Paper_loginpage
sys.path.append('./model')
sys.path.append('./page_obj')

class LoginTest(myunit.MyTest):

    def test_login_user_pwd_null(self):
        '''用户名，密码为空登录'''
        po = Paper_loginpage(self,driver)
        po.open()
        po.login_action(",")
        sleep(2)
        self.assertEqual(po.login_error_hint(),"请输入账号")
        function.insert_img(self.driver, "user_pwd_null.jpg")

    def test_login_pwd_null(self):
        '''密码为空登录'''
        po = Paper_loginpage(self.driver)
        po.open()
        po.login_action("admin","")
        sleep(2)
        self.assertEqual(po.login_error_himt(),"请输入密码")
        function.insert_img(self.driver,"pwd_null.jpg")

    def test_login_user_pwd_erroe(self):
        '''用户名或者密码错误'''
        po = Paper_loginpage(self.driver)
        po.open()
        charactor = random.choice("zxcvbnmasdfghjklqwertyuiop")
        username = "test" + charactor
        po.login_action(username,"$#%#")
        sleep(2)
        #print(po.login_error_hint())
        self.assertEqual(po.login_errow_hint(),"帐号或者密码不正确")
        function.insert_img(self.driver, "user_pwd_error.jpg")

    def test_login_success(self):
        '''用户名，密码正确，登录成功'''
        po = Paper_loginpage(self.driver)
        po.open()
        user = "admin"
        po.login_action(user, "admin")
        sleep(2)
        po2 = Paper_loginpage(self.driver)
        #print(po2.login_success_user())
        self.assertEqual(po2.login_success_user(),user+"@163.com")
        function.insert_img(self.driver, "success.jpg")