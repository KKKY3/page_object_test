#coding:utf-8
import unittest
from time import sleep

class Base(object):
    def __init__(self,driver):
        self.driver =driver
        self.activity = 'com.meeting.itc.paperless.activity.LoginActivity'
        self.timeout = 30

    def open(self):
        sleep(3)
        #com.meeting.itc.paperless.activity.LoginActivity
        #assert self.driver.current_activity == self.activity,"Did not open on %s" %self.activity

    #参数个数不是固定的（By.ID,"kw"）
    def by_id(self,loc):
        return self.driver.find_element_by_id(loc)

    def by_class_name(self,loc):
        return self.driver.find_elements_by_class_name(loc)

    def by_ids(self,*loc):
        return self.driver.finde_lements_by_id(*loc)