#coding:utf-8
from selenium import webdriver
import os,time


def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    #print(base_dir)
    base_dir = str(base_dir)
    #print(base_dir)
    base_dir = base_dir.replace('\\','/')
    #print(base_dir)
    base = base_dir.split('/mail')[0]
    #print(base)
    now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    file_path = base + '/mail/image/'+ now_time + file_name
    print(file_path)
    #print(now_time)
    driver.get_screenshot_as_file(file_path)



if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    insert_img(driver,"baidu.jpg")
    driver.quit()