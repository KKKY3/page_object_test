#coding:utf-8
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .base import Base

#页面对象（PO）登录页面
class LoginPage(Base):
    url = '/'
    login_username_text_loc = (By.NAME, "account")
    login_password_text_loc = (By.NAME,"password")
    login_button_loc = (By.ID, "login")
    login_erro_hint_loc = (By.CLASS_NAME, "mind_top fl")

    #把每一个元素封装成一个方法：
    def login_username(self,text):
        self.find_element(*self.login_username_text_loc).send_key(text)

    def login_password(self,text):
        self.find_element(*self.login_password_text_loc).send_key(text)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def login_error_hint(self):
        return self.find_element(*self.login_erro_hint_loc).text

    def login_action(self,username, password):
        self.login_username(username)
        self.login_password(password)
        self.login_button()
