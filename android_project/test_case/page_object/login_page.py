#coding:utf-8
from time import sleep

from paperless_project.android_project.test_case.page_object.base import Base
from selenium.webdriver.common.by import By


class LoginPage(Base):
    login_ip_config_btn = "com.Meeting.itc.paperless:id/text_ip_setting"
    login_title_loc = "com.Meeting.itc.paperless:id/tv_account_login"
    login_user_loc = "com.Meeting.itc.paperless:id/edit_account"
    login_pwd_loc = "com.Meeting.itc.paperless:id/edit_password"
    login_confirm_btn_loc = "com.Meeting.itc.paperless:id/btn_login"

    #IP设置定位
    def click_ip_config_btn(self):
        self.by_id(self.login_ip_config_btn).click()

    #定位登录页面校验元素
    def login_title(self):
        return self.by_id(self.login_title_loc).text

    #点击设置按钮；
    def click_ip_btn(self):
        self.click_ip_config_btn()

    #用户民出入框定位
    def login_input_username(self,text):
        user_loc = self.by_id(self.login_user_loc)
        sleep(2)
        user_loc.clear()
        user_loc.send_keys(text)

    #密码输入框
    def login_input_pwd(self,text):
        pwd_loc = self.by_id(self.login_pwd_loc)
        sleep(2)
        pwd_loc.clear()
        pwd_loc.send_keys(text)

    #确认按钮
    def login_confrim_btn(self):
        self.by_id(self.login_confirm_btn_loc).click()

    #登录
    def login_action(self,user, pwd):
        self.login_input_username(user)
        sleep(1)
        self.login_input_pwd(pwd)
        sleep(1)
        self.login_confrim_btn()


