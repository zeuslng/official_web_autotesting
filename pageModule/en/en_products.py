import time

import allure
import utils.TestTool as tool
from utils.Account import get_account_password
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Product:

    def __init__(self, driver):
        self.driver = driver

    """-----------------------header部分-----------------------"""
    # 头部文案
    header_txt = (By.XPATH, '/html/body/section[1]/div/h3')
    # 头部图片
    header_img = (By.XPATH, '/html/body/section[1]/img')

    def get_header_txt(self):
        """头部文案"""
        return tool.find_element(self.driver, *self.header_txt)

    def get_header_img(self):
        """头部图片"""
        return tool.find_element(self.driver, *self.header_img)

    """-----------------------介绍部分-----------------------"""
    # 标题，定位使用
    title1 = (By.XPATH, '/html/body/section[2]/div[1]/span')
    # 第1行的图片1
    line_1_img1 = (By.XPATH, '/html/body/section[2]/div[2]/div[1]/div[2]/img[1]')
    # 第1行的图片2
    line_1_img2 = (By.XPATH, '/html/body/section[2]/div[2]/div[1]/div[2]/img[2]')
    # 第1行文案
    line_1_txt = (By.XPATH, '/html/body/section[2]/div[2]/div[1]/div[1]/h6')
    # 第2行的图片1
    line_2_img1 = (By.XPATH, '/html/body/section[2]/div[2]/div[2]/div[2]/img[1]')
    # 第2行的图片2
    line_2_img2 = (By.XPATH, '/html/body/section[2]/div[2]/div[2]/div[2]/img[2]')
    # 第2行文案
    line_2_txt = (By.XPATH, '/html/body/section[2]/div[2]/div[2]/div[1]/h6')
    # 第3行的图片
    line_3_img = (By.XPATH, '/html/body/section[2]/div[2]/div[3]/div[3]/img[1]')
    # 第2行文案
    line_3_txt = (By.XPATH, '/html/body/section[2]/div[2]/div[3]/div[1]/h6')

    def scroll_to_title1(self):
        """滚动到产品介绍部分"""
        tool.scroll_to_element(self.driver, tool.find_element(self.driver, *self.title1))

    def get_line_1_img1(self):
        return tool.find_element(self.driver, *self.line_1_img1)

    def get_line_1_img2(self):
        return tool.find_element(self.driver, *self.line_1_img2)

    def get_line_1_txt(self):
        return tool.find_element(self.driver, *self.line_1_txt)

    def get_line_2_img1(self):
        return tool.find_element(self.driver, *self.line_2_img1)

    def get_line_2_img2(self):
        return tool.find_element(self.driver, *self.line_2_img2)

    def get_line_2_txt(self):
        return tool.find_element(self.driver, *self.line_2_txt)

    def get_line_3_txt(self):
        return tool.find_element(self.driver, *self.line_3_txt)

    def get_line_3_img(self):
        return tool.find_element(self.driver, *self.line_3_img)

    """-----------------------多维数据部分-----------------------"""

    # 标题 定位使用
    title2 = (By.XPATH, '/html/body/section[3]/div/div/div[1]/span')
    # 卡片1
    card1 = (By.XPATH, '/html/body/section[3]/div/div/div[2]/div[1]/div/div[16]')
    # 卡片2
    card2 = (By.XPATH, '/html/body/section[3]/div/div/div[2]/div[1]/div/div[10]')

    """-----------------------便捷设备管理部分部分-----------------------"""
    # 标题 定位使用
    title3 = (By.XPATH, '/html/body/section[4]/div/div[1]/span')
    # 设备图片列表
    ep_images = [f'/html/body/section[4]/div/div[2]/div[1]/img[{i}]' for i in range(1, 6)]

    def get_ep_images(self):
        """设备图片列表"""
        return [tool.find_element(self.driver, *(By.XPATH, i)) for i in self.ep_images]

    def scroll_to_title3(self):
        """滚动到产品介绍部分"""
        tool.scroll_to_element(self.driver, tool.find_element(self.driver, *self.title3))

    """-----------------------定制化服务部分部分-----------------------"""

    # 标题 定位使用
    title4 = (By.XPATH, '/html/body/section[5]/div/div[1]/div/div/span')
    # 所有图标
    all_serve_svg = [(By.XPATH, f'/html/body/section[5]/div/div[2]/ul/li[{i}]/img')
                     for i in range(1, 5)]
    # 文案1
    all_serve_txt = [(By.XPATH, f'/html/body/section[5]/div/div[2]/ul/li[{i}]/p[1]')
                     for i in range(1, 5)]

    def scroll_to_title4(self):
        """滚动到产品介绍部分"""
        tool.scroll_to_element(self.driver, tool.find_element(self.driver, *self.title4))

    def get_all_svg(self):
        """所有定制化服务图标"""
        return [tool.find_element(self.driver, *i)
                for i in self.all_serve_svg]

    def get_all_txt(self):
        """所有定制化服务文案"""
        return [tool.find_element(self.driver, *i)
                for i in self.all_serve_txt]

    """-----------------------应用现场实景部分-----------------------"""

    # 标题
    title5 = (By.XPATH, '/html/body/section[6]/div[1]/span')
    # 轮播图父节点
    father = (By.XPATH, '/html/body/section[6]/div[2]/div[1]/div')
    # 下一个按钮
    next_btn = (By.XPATH, '/html/body/section[6]/div[2]/div[3]')
    # 上一个按钮
    per_btn = (By.XPATH, '/html/body/section[6]/div[2]/div[2]')

    def get_all_applications(self):
        father = tool.wait_ele_be_founded(self.driver, 10, *self.father)
        images = father.find_elements(By.TAG_NAME, 'img')
        return images

    def scroll_to_title5(self):
        """滚动到应用现场实景部分-"""
        tool.scroll_to_element(self.driver, tool.wait_ele_be_founded(self.driver, 10, *self.title5))

    def get_next_btn(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.next_btn)

    def get_per_btn(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.per_btn)