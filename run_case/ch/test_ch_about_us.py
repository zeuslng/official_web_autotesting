"""
公共模块测试用例（特别关注、异常报警等）
"""

import sys
import time
import allure
import pytest
from selenium.webdriver.common.by import By
from test_generate_report import env
import pageModule.ch.ch_about_us as about
import utils.TestTool as tool
if str(env) == 'ot':
    about_url = 'https://ot-www.sucheon.com/about.html'
else:
    about_url = 'https://www.sucheon.com/about.html'


class TestAbout(object):

    feature = '关于我们-中文'

    def setup_class(self) -> None:
        self.driver = tool.get_driver()
        self.about = about.About(self.driver)
        self.driver.get(about_url)
        self.driver.maximize_window()

    def teardown_class(self):
        print('"====有异常抛出也会结束进程关掉driver====')
        self.driver.quit()

    """-----------------头部banner-----------------"""

    @allure.feature(feature)
    @allure.story('头部banner')  # 用例模块
    @allure.description('查看头部banner图片文字是否显示')  # 用例描述
    @allure.title('头部banner显示测试')  # 用例标题
    def test_header_1(self):
        txt = self.about.get_header_txt()
        img = self.about.get_header_img()
        if txt.text is None or tool.is_img_loaded(self.driver, img) is False:
            tool.raise_and_screen(self.driver, '疑似头部banner文字或者图片未加载')

    """-----------------公司介绍-----------------"""

    @allure.feature(feature)
    @allure.story('公司介绍')  # 用例模块
    @allure.description('查看公司图片和介绍文字是否显示正常')  # 用例描述
    @allure.title('公司介绍显示测试')  # 用例标题
    def test_introduce_1(self):
        self.about.scroll_to_title1()
        txt1 = self.about.get_introduce_txt()
        img1 = self.about.get_introduce_img()
        res = tool.wait_until_true(tool.is_img_loaded, 10, self.driver, img1)
        if txt1.text is None or res is False:
            tool.raise_and_screen(self.driver, '疑似公司图片或介绍文字未加载')

    """-----------------发展历程-----------------"""

    @allure.feature(feature)
    @allure.story('发展历程')  # 用例模块
    @allure.description('鼠标移动至年份按钮，测试上方tab页是否正常跳转')  # 用例描述
    @allure.title('年份切换测试')  # 用例标题
    def test_develop_1(self):
        self.about.scroll_to_title2()
        btns = self.about.get_years_btn()
        texts = self.about.get_years_txt()
        for i in range(len(btns)):
            btn = btns[i]
            tool.move_to_element_or_click(self.driver, btn)
            time.sleep(1)
            btn_txt = btn.text
            txt = texts[i].text
            if btn_txt != txt or not texts[i].is_displayed():
                tool.raise_and_screen(self.driver, '%s年份切换疑似存在异常' % btn_txt)
            time.sleep(1)

    """-----------------管理团队-----------------"""

    @allure.feature(feature)
    @allure.story('管理团队')  # 用例模块
    @allure.description('点击团队成员头像，测试tab页是否切换')  # 用例描述
    @allure.title('成员切换测试')  # 用例标题
    def test_team_1(self):
        self.about.scroll_title3()
        btns = self.about.get_manager_btn()
        images = self.about.get_manager_img()
        for i in range(len(btns)):
            btn = btns[i]
            # 点击头像
            btn.click()
            time.sleep(1)
            # 判断第i个人物头像大图是否可见和加载
            visible = tool.wait_until_true(tool.is_element_visible, 5, images[i])
            loaded = tool.wait_until_true(tool.is_img_loaded, 10, self.driver, images[i])
            if not visible or not loaded:
                tool.raise_and_screen(self.driver, '点击头像后tab页疑似未切换')

    """-----------------荣誉资质-----------------"""

    @allure.feature(feature)
    @allure.story('荣誉资质')  # 用例模块
    @allure.description('点击荣誉资质，测试图片是否切换')  # 用例描述
    @allure.title('荣誉资质切换测试')  # 用例标题
    def test_honor_1(self):
        self.about.scroll_title4()
        time.sleep(1)
        honors = self.about.get_honor()
        img_url = ''
        a = 1
        for i in range(len(honors)):
            if honors[i].is_displayed() and a <= 5:
                if i <= len(honors) - 1:
                    tool.move_to_element_or_click(self.driver, honors[i+1])
                    time.sleep(0.4)
                    # aft_url = self.about.get_honor_img().get_attribute('src')
                    # if img_url == aft_url:
                    #     raise Exception('疑似图片未切换')
                    # img_url = aft_url
                a += 1

    """-----------------加入硕橙-----------------"""

    @allure.feature(feature)
    @allure.story('加入硕橙')  # 用例模块
    @allure.description('滚动到加入硕橙模块，查看图片是否加载正常')  # 用例描述
    @allure.title('图片加载测试')  # 用例标题
    def test_join_1(self):
        self.about.scroll_title5()
        time.sleep(1)
        images1 = self.about.get_active_img1s()
        images2 = self.about.get_active_img2s()
        for i in images1 + images2:
            if not tool.is_img_loaded(self.driver, i):
                tool.raise_and_screen(self.driver, '疑似存在图片未加载')

    """-----------------招聘详情-----------------"""

    @allure.feature(feature)
    @allure.story('招聘详情')  # 用例模块
    @allure.description('点击查看详情，测试卡片是否有展开')  # 用例描述
    @allure.title('招聘详情展开测试')  # 用例标题
    def test_employ_1(self):
        self.about.scroll_title6()
        time.sleep(1)
        employees = self.about.get_all_employees()
        i = 0
        for e in employees:
            if i > 2:
                tool.scroll_to_element(self.driver, employees[i - 1])
            detail_btn = e.find_element(*(By.XPATH, 'div[1]/div[3]/a'))
            detail = e.find_element(*(By.XPATH, f'//*[@id="collapseExample{i}"]'))
            bef = detail.is_displayed()
            # 点击前应该不可见
            if bef:
                raise Exception('疑似点击查看详情前卡片就已经展开')
            # 展开详情
            detail_btn.click()
            aft = tool.wait_until_true(tool.is_element_visible, 5, detail)
            # 点击后应该可见
            if not aft:
                tool.raise_and_screen(self.driver, '疑似点击查看详情后卡片未展开')

            # # 获取该招聘的岗位详情
            # details = len(self.about.get_emp_details(i))
            # # 判断招聘内容行数
            # if details <= 4:
            #     tool.raise_and_screen(self.driver, '疑似招聘详情内容有缺失')
            # 关闭详情

            detail_btn = e.find_element(*(By.XPATH, 'div[1]/div[3]/a'))
            time.sleep(1)
            detail_btn.click()
            aft_close = tool.wait_until_false(tool.is_element_visible, 5, detail)
            if aft_close:
                tool.raise_and_screen(self.driver, '疑似详情卡片无法关闭')
            i += 1


if __name__ == '__main__':
    # 使用pytest执行用例，并获取allure执行结果
    pytest.main(['-s', './test_ch_product.py', '--alluredir', '../allure-results'])
    # 使用命令生成测试报告 注:在终端中使用命令时要cd 进入当前文件夹之前命令 否则文件夹的相对路径会错误
    # os.system('allure generate ../allure-results -o ../allure-report --clean')
