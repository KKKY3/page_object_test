#coding:utf-8

from .base import Base
from selenium.webdriver.common.by import By

#页面对象（po）会议管理
class MtMenuPage(Base):
    mt_menu_agenda_loc = (By.LINK_TEXT,"会议议程")


    def mt_menu_agenda(self):
        return self.find_element(*self.mt_menu_agenda_loc).click()

    def click_mt_agenda(self):
        MtMenuPage().mt_menu_agenda()

