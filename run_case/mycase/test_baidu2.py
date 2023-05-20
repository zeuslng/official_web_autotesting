import os
import sys

from selenium import webdriver

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)
import time


class Test2:
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    time.sleep(10)
    driver.find_element_by_id('kw').send_keys('java')
    time.sleep(10)
    driver.find_element_by_id('su').click()
    time.sleep(10)
    driver.quit()











