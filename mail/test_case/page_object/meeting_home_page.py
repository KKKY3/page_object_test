#coding:utf-8

from .base import Base
from selenium.webdriver.common.by import By

#页面对象（po）会议管理
class MeetingManagerPage(Base):
    mt_menu_agenda_loc = (By.LINK_TEXT,"会议议程")

    mt_agenda_upload_loc = (By.CLASS_NAME,"Agenda_file")
    upload_choice_file_btn_loc = (By.NAME, "file")
    upload_choice_user_btn_loc = (By.CLASS_NAME, "all-chose")


    def mt_menu_agenda(self):
        return self.find_element(*self.mt_menu_agenda_loc).click()

    def mt_agenda_upload_file(self):
        return self.find_element(*self.mt_agenda_upload_loc).click()

    def upload_choice_file(self,file_url):
        return self.find_element(*self.upload_choice_file_btn_loc).send_keys(file_url)

    def upload_choice_user(self):
        return self.find_element(*self.upload_choice_user_btn_loc).click()


