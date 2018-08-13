#coding:utf-8
from appium import webdriver
import time
def browser():

    desired_caps = {
        'platformName':'Android',
        'deviceName': '1f94808b',
        'platformVersion':"5.1",
        'appPackage':'com.Meeting.itc.paperless',
        'appActivity':'com.meeting.itc.paperless.activity.LoginActivity',
        'unicodeKeyboard': True,
        'resetKeyBoard': True,
        "automationName":"uiautomator2"

    }


    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    time.sleep(10)
    # d = driver.current_activity
    # print(d)

    return driver


if __name__ == '__main__':
    browser()

