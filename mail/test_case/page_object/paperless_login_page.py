#coding:utf-8

from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .base import Base

class Paper_loginpage(Base):
    url = '/'
    login_success_user_loc = (By.CSS_SELECTOR, '.fr')

    def login_success_user(self):
        return  self.find_element(*self.login_success_user_loc).text