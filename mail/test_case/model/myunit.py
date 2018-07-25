#coding:utf-8

import unittest
from paperless_project.mail.test_case.driver.driver import browser

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()