import time

import allure
import utils.TestTool as tool
from utils.Account import get_account_password
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class About:

    def __init__(self, driver):
        self.driver = driver

    """---------------------头部banner---------------------"""

    # 头部文案
    header_txt = (By.XPATH, '/html/body/section[1]/div/h3')
    # 头部图片
    header_img = (By.XPATH, '/html/body/section[1]/img')

    def get_header_txt(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.header_txt)

    def get_header_img(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.header_img)

    """---------------------公司介绍---------------------"""

    # 模块标题
    title1 = (By.XPATH, '/html/body/section[2]/div[1]/span')
    # 公司图片
    introduce_img = (By.XPATH, '/html/body/section[2]/div[2]/div[1]/img')
    # 介绍文案
    introduce_txt = (By.XPATH, '/html/body/section[2]/div[2]/div[2]/p[1]')

    def scroll_to_title1(self):
        tool.scroll_to_element(self.driver, tool.wait_ele_be_founded(self.driver, 10, *self.title1))

    def get_introduce_img(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.introduce_img)

    def get_introduce_txt(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.introduce_txt)

    """---------------------发展历程---------------------"""

    # 模块标题
    title2 = (By.XPATH, '/html/body/section[3]/div/div[1]/span')
    # 年份按钮
    years_btn = [(By.XPATH, f'/html/body/section[3]/div/div[2]/div[3]/div[2]/div[{i}]')
                 for i in range(1, 7)]
    # 年份文案
    years_txt = [(By.XPATH, f'/html/body/section[3]/div/div[2]/div[2]/div[{i}]/h2')
                 for i in range(1, 7)]

    def scroll_to_title2(self):
        tool.scroll_to_element(self.driver, tool.wait_ele_be_founded(self.driver, 10, *self.title2))

    def get_years_btn(self):
        return [tool.wait_ele_be_founded(self.driver, 10, *i) for i in self.years_btn]

    def get_years_txt(self):
        return [tool.wait_ele_be_founded(self.driver, 10, *i) for i in self.years_txt]

    """---------------------发展历程---------------------"""

    # 模块标题
    title3 = (By.XPATH, '/html/body/section[4]/div/div[1]/span')
    # 团队成员按钮
    managers_btn = [(By.XPATH, f'/html/body/section[4]/div/div[2]/div/div[2]/div/div/div[{i}]')
                    for i in range(1, 8)]
    # 团队成员照片
    managers_img = [(By.XPATH, f'/html/body/section[4]/div/div[2]/div/div[1]/div/div[{i}]/div/img')
                    for i in range(1, 8)]

    def scroll_title3(self):
        tool.scroll_to_element(self.driver, tool.wait_ele_be_founded(self.driver, 10, *self.title3))

    def get_manager_btn(self):
        return [tool.wait_ele_be_founded(self.driver, 10, *i) for i in self.managers_btn]

    def get_manager_img(self):
        return [tool.wait_ele_be_founded(self.driver, 10, *i) for i in self.managers_img]

    """---------------------荣誉资质---------------------"""

    # 模块标题
    title4 = (By.XPATH, '/html/body/section[5]/div/div[1]/span')
    # 荣誉事件
    honor = [(By.XPATH, f'/html/body/section[5]/div/div[2]/div[1]/div/div[{i}]')
             for i in range(3, 21)]
    # 荣誉图片
    honor_img = (By.XPATH, '/html/body/section[5]/div/div[2]/div[4]/div/img')

    def scroll_title4(self):
        tool.scroll_to_element(self.driver, tool.wait_ele_be_founded(self.driver, 10, *self.title4))

    def get_honor(self):
        return tool.wait_eles_be_founded(self.driver, 10, *(By.XPATH, '/html/body/section[5]/div/div[2]/div[1]/div/div'))[2:]

    def get_honor_img(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.honor_img)

    """---------------------加入硕橙---------------------"""

    # 模块标题
    title5 = (By.XPATH, '/html/body/section[6]/div/div[1]/span')
    # 活动图片1 三张
    active_img1s = (By.XPATH, '/html/body/section[6]/div/div[3]/img')
    # 活动图片2 三张
    active_img2s = (By.XPATH, '/html/body/section[6]/div/div[4]/img')

    def scroll_title5(self):
        tool.scroll_to_element(self.driver, tool.wait_ele_be_founded(self.driver, 10, *self.title5))

    def get_active_img1s(self):
        return tool.wait_eles_be_founded(self.driver, 10, *self.active_img1s)

    def get_active_img2s(self):
        return tool.wait_eles_be_founded(self.driver, 10, *self.active_img1s)

    """---------------------加入硕橙---------------------"""

    # 模块标题
    title6 = (By.XPATH, '//*[@id="recruitment"]/div/div[1]/span')
    # 所有招聘信息栏
    employees = (By.XPATH, '//*[@id="recruitment"]/div/div[2]/div')

    def scroll_title6(self):
        tool.scroll_to_element(self.driver, tool.wait_ele_be_founded(self.driver, 10, *self.title6))

    def get_all_employees(self):
        """所有招聘信息栏 去掉结果集的第一个 因为第一个div不是招聘信息"""
        return tool.wait_eles_be_founded(self.driver, 10, *self.employees)[1:]

    def get_emp_details(self, i):
        """
        获取卡片内的岗位详情中p标签的数量
        若标签数量小于4 则有可能是招聘内容有异常
        :param i 第几个卡片，从0开始
        """
        return tool.wait_eles_be_founded(self.driver, 10, *(By.XPATH, f'//*[@id="collapseExample{i}"]/div/div[1]/p'))
