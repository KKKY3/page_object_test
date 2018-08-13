#coding:utf-8
from selenium.webdriver.common.by import By
from paperless_project.android_project.test_case.page_object.base import Base
from paperless_project.android_project.test_case.model.driverwait import find_toast
from login_page import LoginPage
from time import sleep


class IPConfigPage(Base):
    ip_address_text_loc = "com.Meeting.itc.paperless:id/edit_ip_address"
    ip_port_text_loc= "com.Meeting.itc.paperless:id/rl_port"
    ip_confirm_btn_loc = "com.Meeting.itc.paperless:id/tv_setting_sure"
    ip_title_loc = "com.Meeting.itc.paperless:id/tv_setting_info"


    def ip_setting_title(self):
        return self.by_id(self.ip_title_loc).text


    def ip_address(self,text):
        sleep(2)
        ip_add = self.by_id(self.ip_address_text_loc)
        ip_add.click()
        sleep(3)
        ip_add.clear()
        ip_add.send_keys(text)


    def ip_port(self):
        self.by_id(self.ip_port_text_loc).send_keys("88")

    def ip_confirm_btn(self):
        self.by_id(self.ip_confirm_btn_loc).click()

    def ipconfig_action(self,ipaddress):
        self.ip_address(ipaddress)
        sleep(3)
        self.ip_confirm_btn()