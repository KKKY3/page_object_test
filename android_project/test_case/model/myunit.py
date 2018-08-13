#coding:utf-8

import unittest
from paperless_project.android_project.test_case.driver.driver import browser

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)


    def tearDown(self):
        self.driver.quit()