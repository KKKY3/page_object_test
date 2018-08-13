#coding:utf-8
from selenium import webdriver
import os, time

def insert_image(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace("\\","/")
    base = base_dir.split("/android_project")[0]
    now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    file_path = base + "/android_project/image/"+ now_time + file_name
    print(file_path)
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    insert_image(driver, "test.jpg")
