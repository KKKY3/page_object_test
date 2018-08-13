#coding:utf-8
from .base import Base
from selenium.webdriver.common.by import By
import time

class UplaodFile(Base):
    mt_agenda_upload_loc = (By.CLASS_NAME, "Agenda_file")
    upload_choice_file_btn_loc = (By.NAME, "file")
    upload_choice_user_btn_loc = (By.CLASS_NAME, "all-chose")
    uplaod_submit_but_loc = (By.CLASS_NAME,"submit-file")


    def mt_agenda_upload_file(self):
        return self.find_element(*self.mt_agenda_upload_loc).click()

    def upload_choice_file(self,file_url):
        return self.find_element(*self.upload_choice_file_btn_loc).send_keys(file_url)

    def upload_choice_user(self):
        return self.find_element(*self.upload_choice_user_btn_loc).click()

    def uplaod_submit_but(self):
        return self.find_element(*self.uplaod_submit_but_loc).click()

    def uplaod_file(self,file_url):
        self.mt_agenda_upload_file()
        self.upload_choice_file(file_url)
        self.upload_choice_user()
        time.sleep(10)
        self.uplaod_submit_but()