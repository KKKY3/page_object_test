#coding:utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def find_toast(driver, message):
    try:
        toast_loc = ("xpath",".//*[contains(@text, message)]")
        WebDriverWait(driver, 5, 0.1).until(EC.presence_of_element_located(toast_loc))
        return True

    except:
        return False
