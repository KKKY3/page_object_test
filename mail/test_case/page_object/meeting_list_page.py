#coding:utf-8
from time import sleep
from .base import Base
from selenium.webdriver.common.by import By


class MeetingList(Base):

    mt_name_loc = (By.XPATH, ".//*[@id='datagrid-row-r1-1-0']/td[3]/div")

    def mt_name(self):
        return self.find_elements(*self.mt_name_loc)[0].click()

    def click_mt_name(self):
        MeetingList(self.driver).mt_name()