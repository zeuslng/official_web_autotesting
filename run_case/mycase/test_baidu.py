import os
import sys

from selenium import webdriver

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)
import time


class Test1:
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    time.sleep(10)
    driver.find_element_by_id('kw').send_keys('python')
    time.sleep(10)
    driver.find_element_by_id('su').click()
    time.sleep(10)
    driver.quit()










