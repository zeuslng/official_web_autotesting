"""
公共模块测试用例（特别关注、异常报警等）
"""
import sys
import os
import time

import allure
import pytest
from selenium.webdriver.common.by import By

import test_generate_report
import utils.TestTool as tool
import pageModule.ch.ch_home as home

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)

if test_generate_report.env == "ot":
    product_url = 'https://ot-www.sucheon.com/product.html'
    home_url = 'https://ot-www.sucheon.com/index.html'
    about_url = 'https://ot-www.sucheon.com/about.html'
    application_url = 'https://ot-www.sucheon.com/application.html'
else:
    product_url = 'https://www.sucheon.com/product.html'
    home_url = 'https://www.sucheon.com/index.html'
    about_url = 'https://www.sucheon.com/about.html'
    application_url = 'https://www.sucheon.com/application.html'


class TestHome(object):

    feature = '首页-中文'

    def setup_class(self) -> None:
        self.driver = tool.get_driver()
        self.home = home.Home(self.driver)
        self.driver.get(home_url)
        self.driver.maximize_window()

    def teardown_class(self):
        print('"====有异常抛出也会结束进程关掉driver====')
        self.driver.quit()

    @allure.feature(feature)
    @allure.story('导航栏')  # 用例模块
    @allure.description('首页中点击产品介绍模块，测试是否正常跳转')  # 用例描述
    @allure.title('产品介绍跳转测试')  # 用例标题
    def test_header_1(self):
        # 产品介绍模块按钮
        btn = tool.find_element(self.driver, *(By.XPATH, '/html/body/header/div/ul/li[2]/a'))
        # 点击跳转
        btn.click()
        url = self.driver.current_url
        if url != product_url:
            tool.raise_and_screen(self.driver, '疑似点击产品介绍跳转失败')

    """-----------------头部banner-----------------"""

    @allure.feature(feature)
    @allure.story('头部banner')  # 用例模块
    @allure.description('点击了解更多按钮，测试是否正常跳转')  # 用例描述
    @allure.title('了解更多跳转测试')  # 用例标题
    def test_header_2(self):
        self.driver.get(home_url)
        # 点击切换到第一个轮播图
        self.home.get_banner_1_line().click()
        time.sleep(1)
        # 点击了解更多按钮
        self.home.get_banner_1_btn().click()
        url = self.driver.current_url
        if url != product_url:
            tool.raise_and_screen(self.driver, '疑似点击了解更多按钮跳转异常')
        self.driver.back()

    @allure.feature(feature)
    @allure.story('头部banner')  # 用例模块
    @allure.description('点击观看视频按钮，测试是否正常跳转')  # 用例描述
    @allure.title('观看视频按钮点击跳转测试')  # 用例标题
    def test_header_3(self):
        # 点击切换到第2个轮播图
        self.home.get_banner_2_line().click()
        # 点击播放前判断视频状态
        video = tool.wait_until_false(tool.is_element_visible, 5, self.home.get_video())
        if video:
            tool.raise_and_screen(self.driver, '点击播放前视频显示异常')
        self.home.get_banner_2_btn().click()
        time.sleep(5)
        # 点击播放后判断视频状态
        video2 = tool.wait_until_true(tool.is_element_visible, 5, self.home.get_video())
        if not video2:
            tool.raise_and_screen(self.driver, '疑似点击后视频未播放')
        # 点击关闭视频
        self.home.get_video_close().click()
        # 判断关闭后是否可见
        video3 = tool.wait_until_false(tool.is_element_visible, 5, self.home.get_video())
        if video3:
            tool.raise_and_screen(self.driver, '疑似视频无法关闭')

    @allure.feature(feature)
    @allure.story('头部banner')  # 用例模块
    @allure.description('点击加入我们按钮，测试是否正常跳转')  # 用例描述
    @allure.title('加入我们钮点击跳转测试')  # 用例标题
    def test_header_4(self):
        # 点击切换到第3个轮播图
        self.home.get_banner_3_line().click()
        # 点击加入我们
        self.home.get_banner_3_btn().click()
        # 跳转后应该能看到招聘详情
        employ = tool.wait_until_true(tool.find_element, 10, self.driver, *(By.XPATH, '//*[@id="recruitment"]/div/div[1]/span'))
        flag = tool.wait_until_true(tool.is_element_visible, 10, employ)
        if not flag:
            tool.raise_and_screen(self.driver, '疑似点击加入我们后未跳转到招聘详情部分')
        self.driver.back()

    """-----------------产品功能-----------------"""

    @allure.feature(feature)
    @allure.story('产品功能')  # 用例模块
    @allure.description('点击预测性维护按钮，测试轮播图是否正常跳转')  # 用例描述
    @allure.title('预测性维护钮点击跳转测试')  # 用例标题
    def test_realize_1(self):
        self.home.scroll_to_title1()
        self.home.get_function_1().click()
        time.sleep(1)
        if self.home.get_function_1_txt().text != '预测性维护' and self.home.get_function_1_txt().is_displayed() is not True:
            tool.get_allure_screen_shoot(self.driver, '预测性维护异常')
            tool.raise_and_screen(self.driver, '疑似点击按钮banner未切换')

    @allure.feature(feature)
    @allure.story('产品功能')  # 用例模块
    @allure.description('点击产品自动化质检按钮，测试轮播图是否正常跳转')  # 用例描述
    @allure.title('产品自动化质检按钮点击跳转测试')  # 用例标题
    def test_realize_2(self):
        self.home.scroll_to_title1()
        self.home.get_function_2().click()
        time.sleep(1)
        if self.home.get_function_1_txt().text != '产品自动化质检' and self.home.get_function_2_txt().is_displayed() is not True:
            tool.get_allure_screen_shoot(self.driver, '产品自动化质检异常')
            tool.raise_and_screen(self.driver, '疑似点击按钮banner未切换')

    @allure.feature(feature)
    @allure.story('产品功能')  # 用例模块x
    @allure.description('点击环境异常报警按钮，测试轮播图是否正常跳转')  # 用例描述
    @allure.title('环境异常报警按钮点击跳转测试')  # 用例标题
    def test_realize_3(self):
        self.home.scroll_to_title1()
        self.home.get_function_3().click()
        time.sleep(1)
        if self.home.get_function_1_txt().text != '环境异常报警' and self.home.get_function_3_txt().is_displayed() is not True:
            tool.get_allure_screen_shoot(self.driver, '环境异常报警异常')
            tool.raise_and_screen(self.driver, '疑似点击按钮banner未切换')

    @allure.feature(feature)
    @allure.story('产品功能')  # 用例模块
    @allure.description('点击设备远程监控按钮，测试轮播图是否正常跳转')  # 用例描述
    @allure.title('设备远程监控按钮点击跳转测试')  # 用例标题
    def test_realize_4(self):
        self.home.scroll_to_title1()
        self.home.get_function_4().click()
        time.sleep(1)
        if self.home.get_function_1_txt().text != '设备远程监控' and self.home.get_function_4_txt().is_displayed() is not True:
            tool.get_allure_screen_shoot(self.driver, '设备远程监控异常')
            tool.raise_and_screen(self.driver, '疑似点击按钮banner未切换')

    @allure.feature(feature)
    @allure.story('产品功能')  # 用例模块
    @allure.description('点击产线实时健侧按钮，测试轮播图是否正常跳转')  # 用例描述
    @allure.title('产线实时监测按钮点击跳转测试')  # 用例标题
    def test_realize_5(self):
        self.home.scroll_to_title1()
        self.home.get_function_5().click()
        time.sleep(1)
        if self.home.get_function_1_txt().text != '产线实时监测' and self.home.get_function_5_txt().is_displayed() is not True:
            tool.get_allure_screen_shoot(self.driver, '产线实时监测异常')
            tool.raise_and_screen(self.driver, '疑似点击按钮banner未切换')

    """-----------------产品特点-----------------"""

    @allure.feature(feature)
    @allure.story('产品特点')  # 用例模块
    @allure.description('点击向右切换按钮，测试切换卡片是否正常')  # 用例描述
    @allure.title('向右切换按钮测试')  # 用例标题
    def test_special_1(self):
        self.home.scroll_to_title2()
        # 先判断当前是哪个图片高亮
        high = self.home.check_high_light()
        print('当前第%s张高亮' % high)
        # 点击向右切换按钮
        self.home.get_btn_r().click()
        time.sleep(2)
        # 若当前未第n张图高亮 则点击2秒后应该是第n+1张图高亮
        high_2 = self.home.check_high_light()
        print('当前第%s张高亮' % high_2)
        if int(high) == 6:
            if int(high_2) != 1:
                tool.raise_and_screen(self.driver, '疑似向右切换按钮失效')
        if int(high_2) != int(high) + 1:
            tool.raise_and_screen(self.driver, '疑似向右切换按钮失效')

    @allure.feature(feature)
    @allure.story('产品特点')  # 用例模块
    @allure.description('点击向左切换按钮，测试切换卡片是否正常')  # 用例描述
    @allure.title('向左切换按钮测试')  # 用例标题
    def test_special_2(self):
        self.home.scroll_to_title2()
        # 先判断当前是哪个图片高亮
        high = self.home.check_high_light()
        print('当前第%s张高亮' % high)
        # 点击向左切换按钮
        self.home.get_btn_l().click()
        time.sleep(2)
        # 若当前未第n张图高亮 则点击2秒后应该是第n+1张图高亮
        high_2 = self.home.check_high_light()
        print('当前第%s张高亮' % high_2)
        if int(high) == 1:
            if int(high_2) != 6:
                tool.raise_and_screen(self.driver, '疑似向右切换按钮失效')
        elif int(high_2) != int(high) - 1:
            tool.raise_and_screen(self.driver, '疑似向左切换按钮失效')

    """-----------------客户部分-----------------"""

    @allure.feature(feature)
    @allure.story('客户')  # 用例模块
    @allure.description('滑动到客户部分，查看客户数量是否变为100+')  # 用例描述
    @allure.title('客户数量测试')  # 用例标题
    def test_customer_1(self):
        self.home.scroll_to_title3()
        time.sleep(2)
        # 等待两秒后获取客户数量
        num = int(self.home.get_customer_num().text)
        print('当前客户数量未%s' % num)
        if num == 0:
            tool.raise_and_screen(self.driver, '客户数量疑似未变化')

    @allure.feature(feature)
    @allure.story('客户')  # 用例模块
    @allure.description('滑动到客户部分，查看客户logo是否全部显示')  # 用例描述
    @allure.title('客户logo测试')  # 用例标题
    def test_customer_2(self):
        self.home.scroll_to_title3()
        time.sleep(5)
        # 等待5秒后查看华为云logo透明度（华为云logo在最外层）若显示了 透明度为1
        opacity = self.home.get_hw_logo().value_of_css_property('opacity')
        if int(opacity) < 1:
            tool.raise_and_screen(self.driver, '客户logo疑似未加载完成')

    @allure.feature(feature)
    @allure.story('客户')  # 用例模块
    @allure.description('点击客户类型，测试是否能够跳转至应用案例对应行业')  # 用例描述
    @allure.title('客户类型跳转测试')  # 用例标题
    def test_customer_3(self):
        self.home.scroll_to_title3()
        # 获取所有客户类型
        paths = self.home.customer_types
        i = 1
        for xpath in paths:
            btn = tool.find_element(self.driver, *(By.XPATH, xpath))
            print('跳转至%s' % btn.text)
            btn.click()
            if self.driver.current_url.split('?')[0] != application_url:
                tool.raise_and_screen(self.driver, '疑似链接跳转错误')
            flag = tool.find_element(self.driver, *(By.XPATH, f'/html/body/div[1]/section/div[2]/div[{i}]/div[1]/h4')).is_displayed()
            i += 1
            if flag is not True:
                tool.raise_and_screen(self.driver, '疑似跳转过后的客户类型显示错误')
            self.driver.back()
            self.home.scroll_to_title3()

    """-----------------合作伙伴部分""-----------------"""

    @allure.feature(feature)
    @allure.story('合作伙伴')  # 用例模块
    @allure.description('滑动至合作伙伴模块，查看图片是否加载正常')  # 用例描述
    @allure.title('合作伙伴logo加载测试')  # 用例标题
    def test_coop_3(self):
        self.driver.get(home_url)
        self.home.scroll_to_title4()
        images = self.home.get_coop_logos()
        for img in images:
            flag = tool.wait_until_true(tool.is_img_loaded, 10, self.driver, img)
            if not flag:
                tool.raise_and_screen(self.driver, '疑似存在合作伙伴logo图片失效')


if __name__ == '__main__':
    # 使用pytest执行用例，并获取allure执行结果
    pytest.main(['-s', './test_ch_home.py', '--alluredir', './allure-results'])
    # 使用命令生成测试报告 注:在终端中使用命令时要cd 进入当前文件夹之前命令 否则文件夹的相对路径会错误
    # os.system('allure generate ../allure-results -o ../allure-report --clean')
