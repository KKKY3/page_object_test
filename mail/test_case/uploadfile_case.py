#coding:utf-8
from time import sleep
import sys
from page_object.upload_file_page import UplaodFile
from page_object.paperless_menu_page import Paperless_menu_page
from page_object.meeting_list_page import MeetingList
from page_object.meeting_menu_page import MtMenuPage
from model import function,myunit
from page_object.login_Page import LoginPage
sys.path.append('./model')
sys.path.append('./page_obj')

class UploadFileTest(myunit.MyTest):

    def test_upload_file(self):
        '''会议议程上传文件'''
        file_url = ur"F:\测试文档\小学必背古诗80首 带拼音.pdf"
        #登录账号
        po = LoginPage(self.driver)
        po.open()

        user = "admin"
        po.login_action(user, "admin")
        sleep(2)
        #进入会议列表
        po2 = Paperless_menu_page(self.driver)
        po2.meeting_list_loc()
        #进入会议
        sleep(2)
        MeetingList(self.driver).click_mt_name()
        #进入会议议程
        sleep(2)
        MtMenuPage(self.driver).mt_menu_agenda()
        #上传文件
        UplaodFile(self.driver).uplaod_file(file_url)
        function.insert_img(self.driver, "uplaod_file.jpg")









