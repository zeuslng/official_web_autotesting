import time

import allure
import utils.TestTool as tool
from utils.Account import get_account_password
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class News:

    def __init__(self, driver):
        self.driver = driver

    """---------------------头部banner---------------------"""

    # 头部文案
    header_txt = (By.XPATH, '/html/body/section[1]/div/h1')
    # 头部图片
    header_img = (By.XPATH, '/html/body/section[1]/img')

    def get_header_txt(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.header_txt)

    def get_header_img(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.header_img)

    """---------------------tab栏---------------------"""
    # 全部
    all_btn = (By.XPATH, '/html/body/section[2]/div[1]/ul/li[1]')
    # 企业资讯
    enterprise_btn = (By.XPATH, '/html/body/section[2]/div[1]/ul/li[2]')
    # 新闻动态
    news_btn = (By.XPATH, '/html/body/section[2]/div[1]/ul/li[3]')

    def get_all_btn(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.all_btn)

    def get_enterprise_btn(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.enterprise_btn)

    def get_news_btn(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.news_btn)

    # 新闻卡片
    news_cards = (By.XPATH, '/html/body/section[2]/div[2]/div')
    # 卡片标题
    card_title = (By.XPATH, 'div[2]/h6')

    def get_all_news_cards(self):
        return tool.wait_eles_be_founded(self.driver, 10, *self.news_cards)

    """---------------------分页模块---------------------"""

    # 分页按钮 包含上一页下一页按钮
    page_btn = (By.XPATH, '/html/body/section[2]/div[3]/div[1]/button')
    # 頁碼輸入框
    page_input = (By.XPATH, '/html/body/section[2]/div[3]/div[2]/input')

    def get_per_btn(self):
        return tool.wait_eles_be_founded(self.driver, 10, *self.page_btn)[0]

    def get_next_btn(self):
        return tool.wait_eles_be_founded(self.driver, 10, *self.page_btn)[-1]

    def turn_to_page(self, page):
        tool.wait_ele_be_founded(self.driver, 10, *self.page_input).set_value(page)

    """---------------------新聞詳情---------------------"""

    # 新闻标题
    news_title = (By.XPATH, '/html/body/section/h1')
    # 所有新闻图片
    all_img = (By.TAG_NAME, 'img')

    def get_news_title(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.news_title)

    def get_all_img(self):
        body = tool.wait_ele_be_founded(self.driver, 10, *(By.XPATH, '/html/body/section/div[2]'))
        return body.find_elements(*self.all_img)

    """---------------------新聞推荐---------------------"""

    # 推荐新闻
    recommend_cards = (By.XPATH, '/html/body/section/div[2]/div[2]/div/div')

    def get_recommend_cards(self):
        """所有推荐新闻的列表"""
        return tool.wait_eles_be_founded(self.driver, 10, *self.recommend_cards)

