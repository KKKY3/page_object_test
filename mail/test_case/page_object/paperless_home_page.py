#coding:utf-8

from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .base import Base

class Paper_loginpage(Base):
    url = '/'
    login_success_user_loc = (By.CSS_SELECTOR, '.fr')
    menu_meeting_list_loc = (By.LINK_TEXT, "用户列表")


    def login_success_user(self):
        return self.find_element(*self.login_success_user_loc).text

    def meeting_list_loc(self):
        return self.find_element(*self.menu_meeting_list_loc).click()


