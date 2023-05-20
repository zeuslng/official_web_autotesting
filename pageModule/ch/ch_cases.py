import time

import allure
import utils.TestTool as tool
from utils.Account import get_account_password
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Cases:

    def __init__(self, driver):
        self.driver = driver

    """-----------------头部banner-----------------"""

    # 头部文案
    header_txt = (By.XPATH, '/html/body/section/div/h1')
    # banner图片
    header_img = (By.XPATH, '/html/body/section/img')

    def get_header_txt(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.header_txt)

    def get_header_img(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.header_img)

    """-----------------案例-----------------"""

    # 侧边按钮
    sides = [(By.XPATH, f'//*[@id="accordion"]/div[{i}]/div[1]/div')
             for i in range(1, 11)]

    # tab页标题
    titles = [(By.XPATH, f'/html/body/div[1]/section/div[2]/div[{i}]/div[1]/h4')
              for i in range(1, 11)]

    # tab页图片
    images = [(By.XPATH, f'/html/body/div[1]/section/div[2]/div[{i}]/div[1]/p[1]/img')
              for i in range(1, 11)]

    # 下一页按钮 前九个才有
    next_btn = [(By.XPATH, f'/html/body/div[1]/section/div[2]/div[{i}]/div[2]/div[2]')
                for i in range(1, 10)]

    # 上一页按钮 后九个才有
    per_btn = [(By.XPATH, f'/html/body/div[1]/section/div[2]/div[{i}]/div[2]/div[1]')
               for i in range(2, 11)]

    # 获取更多
    learn_more = [(By.XPATH, f'/html/body/div[1]/section/div[2]/div[{i}]/div[1]/span')
                  for i in range(1, 11)]

    def get_all_sides(self):
        """所有侧边按钮"""
        return [tool.wait_ele_be_founded(self.driver, 10, *i) for i in self.sides]

    def get_all_titles(self):
        """所有tab标题"""
        return [tool.wait_ele_be_founded(self.driver, 10, *i) for i in self.titles]

    def get_all_images(self):
        """所有tab图片"""
        return [tool.wait_ele_be_founded(self.driver, 10, *i) for i in self.images]

    def get_all_next(self):
        """所有下一页按钮"""
        return [tool.wait_ele_be_founded(self.driver, 10, *i) for i in self.next_btn]

    def get_all_per(self):
        """所有上一页按钮"""
        return [tool.wait_ele_be_founded(self.driver, 10, *i) for i in self.per_btn]

    def get_learn_more(self):
        """所有获取更多按钮"""
        return [tool.wait_ele_be_founded(self.driver, 10, *i) for i in self.learn_more]
