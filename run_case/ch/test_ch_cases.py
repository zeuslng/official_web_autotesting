"""
公共模块测试用例（特别关注、异常报警等）
"""
import sys
import os
import time

import allure
import pytest
import utils.TestTool as tool
import pageModule.ch.ch_cases as case

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)
cases_url = 'https://www.sucheon.com/application.html'
myskip = pytest.mark.skip


# @myskip
class TestCases(object):

    feature = '应用案例-中文'

    def setup_class(self) -> None:
        self.driver = tool.get_driver()
        self.case = case.Cases(self.driver)
        self.driver.get(cases_url)
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
        time.sleep(50)
        img = self.case.get_header_img()
        txt = self.case.get_header_txt()
        if not tool.wait_until_true(tool.is_img_loaded, 10, self.driver, img) or txt.text is None:
            tool.raise_and_screen(self.driver, '疑似图片或者文案未显示')
        else:
            tool.get_allure_screen_shoot(self.driver, '验证截图')

    """-----------------tab页部分-----------------"""

    @allure.feature(feature)
    @allure.story('tab页部分')  # 用例模块
    @allure.description('点击侧边栏测试tab页切换是否正常')  # 用例描述
    @allure.title('侧边栏切换测试1')  # 用例标题
    def test_side_1(self):
        btn1 = tool.find_element(self.driver, *self.case.sides[0])
        btn1.click()
        btn_txt = btn1.text
        card_txt = tool.find_element(self.driver, *self.case.titles[0]).text
        if btn_txt != card_txt:
            tool.raise_and_screen(self.driver, 'tab页切换疑似错误')
        img = tool.find_element(self.driver, *self.case.images[0])
        if not tool.wait_until_true(tool.is_img_loaded, 10, self.driver, img):
            tool.raise_and_screen(self.driver, '疑似图片未加载成功')
        else:
            tool.get_allure_screen_shoot(self.driver, '验证截图')

    @allure.feature(feature)
    @allure.story('tab页部分')  # 用例模块
    @allure.description('点击侧边栏测试tab页切换是否正常')  # 用例描述
    @allure.title('侧边栏切换测试2')  # 用例标题
    def test_side_2(self):
        btn1 = tool.find_element(self.driver, *self.case.sides[1])
        btn1.click()
        btn_txt = btn1.text
        card_txt = tool.find_element(self.driver, *self.case.titles[1]).text
        if btn_txt != card_txt:
            tool.raise_and_screen(self.driver, 'tab页切换疑似错误')
        img = tool.find_element(self.driver, *self.case.images[1])
        if not tool.wait_until_true(tool.is_img_loaded, 10, self.driver, img):
            tool.raise_and_screen(self.driver, '疑似图片未加载成功')
        else:
            tool.get_allure_screen_shoot(self.driver, '验证截图')

    @allure.feature(feature)
    @allure.story('tab页部分')  # 用例模块
    @allure.description('点击侧边栏测试tab页切换是否正常')  # 用例描述
    @allure.title('侧边栏切换测试3')  # 用例标题
    def test_side_3(self):
        btn1 = tool.find_element(self.driver, *self.case.sides[2])
        btn1.click()
        btn_txt = btn1.text
        card_txt = tool.find_element(self.driver, *self.case.titles[2]).text
        if btn_txt != card_txt:
            tool.raise_and_screen(self.driver, 'tab页切换疑似错误')
        img = tool.find_element(self.driver, *self.case.images[2])
        if not tool.wait_until_true(tool.is_img_loaded, 10, self.driver, img):
            tool.raise_and_screen(self.driver, '疑似图片未加载成功')
        else:
            tool.get_allure_screen_shoot(self.driver, '验证截图')

    @allure.feature(feature)
    @allure.story('tab页部分')  # 用例模块
    @allure.description('点击侧边栏测试tab页切换是否正常')  # 用例描述
    @allure.title('侧边栏切换测试4')  # 用例标题
    def test_side_4(self):
        # 滚动条下拉600px
        js = "document.documentElement.scrollTop = 600"
        self.driver.execute_script(js)
        btn1 = tool.find_element(self.driver, *self.case.sides[3])
        btn1.click()
        btn_txt = btn1.text
        card_txt = tool.find_element(self.driver, *self.case.titles[3]).text
        if btn_txt != card_txt:
            tool.raise_and_screen(self.driver, 'tab页切换疑似错误')
        img = tool.find_element(self.driver, *self.case.images[3])
        if not tool.wait_until_true(tool.is_img_loaded, 10, self.driver, img):
            tool.raise_and_screen(self.driver, '疑似图片未加载成功')
        else:
            tool.get_allure_screen_shoot(self.driver, '验证截图')

    @allure.feature(feature)
    @allure.story('tab页部分')  # 用例模块
    @allure.description('点击侧边栏测试tab页切换是否正常')  # 用例描述
    @allure.title('侧边栏切换测试5')  # 用例标题
    def test_side_5(self):
        btn1 = tool.find_element(self.driver, *self.case.sides[4])
        btn1.click()
        btn_txt = btn1.text
        card_txt = tool.find_element(self.driver, *self.case.titles[4]).text
        if btn_txt != card_txt:
            tool.raise_and_screen(self.driver, 'tab页切换疑似错误')
        img = tool.find_element(self.driver, *self.case.images[4])
        if not tool.wait_until_true(tool.is_img_loaded, 10, self.driver, img):
            tool.raise_and_screen(self.driver, '疑似图片未加载成功')
        else:
            tool.get_allure_screen_shoot(self.driver, '验证截图')

    @allure.feature(feature)
    @allure.story('tab页部分')  # 用例模块
    @allure.description('点击侧边栏测试tab页切换是否正常')  # 用例描述
    @allure.title('侧边栏切换测试6')  # 用例标题
    def test_side_6(self):
        btn1 = tool.find_element(self.driver, *self.case.sides[5])
        btn1.click()
        btn_txt = btn1.text
        card_txt = tool.find_element(self.driver, *self.case.titles[5]).text
        if btn_txt != card_txt:
            tool.raise_and_screen(self.driver, 'tab页切换疑似错误')
        img = tool.find_element(self.driver, *self.case.images[5])
        if not tool.wait_until_true(tool.is_img_loaded, 10, self.driver, img):
            tool.raise_and_screen(self.driver, '疑似图片未加载成功')
        else:
            tool.get_allure_screen_shoot(self.driver, '验证截图')

    @allure.feature(feature)
    @allure.story('tab页部分')  # 用例模块
    @allure.description('点击侧边栏测试tab页切换是否正常')  # 用例描述
    @allure.title('侧边栏切换测试7')  # 用例标题
    def test_side_7(self):
        btn1 = tool.find_element(self.driver, *self.case.sides[6])
        btn1.click()
        btn_txt = btn1.text
        card_txt = tool.find_element(self.driver, *self.case.titles[6]).text
        if btn_txt != card_txt:
            tool.raise_and_screen(self.driver, 'tab页切换疑似错误')
        img = tool.find_element(self.driver, *self.case.images[6])
        if not tool.wait_until_true(tool.is_img_loaded, 10, self.driver, img):
            tool.raise_and_screen(self.driver, '疑似图片未加载成功')
        else:
            tool.get_allure_screen_shoot(self.driver, '验证截图')

    @allure.feature(feature)
    @allure.story('tab页部分')  # 用例模块
    @allure.description('点击侧边栏测试tab页切换是否正常')  # 用例描述
    @allure.title('侧边栏切换测试8')  # 用例标题
    def test_side_8(self):
        btn1 = tool.find_element(self.driver, *self.case.sides[7])
        btn1.click()
        btn_txt = btn1.text
        card_txt = tool.find_element(self.driver, *self.case.titles[7]).text
        if btn_txt != card_txt:
            tool.raise_and_screen(self.driver, 'tab页切换疑似错误')
        img = tool.find_element(self.driver, *self.case.images[7])
        if not tool.wait_until_true(tool.is_img_loaded, 10, self.driver, img):
            tool.raise_and_screen(self.driver, '疑似图片未加载成功')
        else:
            tool.get_allure_screen_shoot(self.driver, '验证截图')

    @allure.feature(feature)
    @allure.story('tab页部分')  # 用例模块
    @allure.description('点击侧边栏测试tab页切换是否正常')  # 用例描述
    @allure.title('侧边栏切换测试9')  # 用例标题
    def test_side_9(self):
        btn1 = tool.find_element(self.driver, *self.case.sides[8])
        btn1.click()
        btn_txt = btn1.text
        card_txt = tool.find_element(self.driver, *self.case.titles[8]).text
        if btn_txt != card_txt:
            tool.raise_and_screen(self.driver, 'tab页切换疑似错误')
        img = tool.find_element(self.driver, *self.case.images[8])
        if not tool.wait_until_true(tool.is_img_loaded, 10, self.driver, img):
            tool.raise_and_screen(self.driver, '疑似图片未加载成功')
        else:
            tool.get_allure_screen_shoot(self.driver, '验证截图')

    @allure.feature(feature)
    @allure.story('tab页部分')  # 用例模块
    @allure.description('点击侧边栏测试tab页切换是否正常')  # 用例描述
    @allure.title('侧边栏切换测试10')  # 用例标题
    def test_side_10(self):
        btn1 = tool.find_element(self.driver, *self.case.sides[9])
        btn1.click()
        btn_txt = btn1.text
        card_txt = tool.find_element(self.driver, *self.case.titles[9]).text
        if btn_txt != card_txt:
            tool.raise_and_screen(self.driver, 'tab页切换疑似错误')
        img = tool.find_element(self.driver, *self.case.images[9])
        if not tool.wait_until_true(tool.is_img_loaded, 10, self.driver, img):
            tool.raise_and_screen(self.driver, '疑似图片未加载成功')
        else:
            tool.get_allure_screen_shoot(self.driver, '验证截图')


if __name__ == '__main__':
    # 使用pytest执行用例，并获取allure执行结果
    pytest.main(['-s', './test_ch_cases.py', '--alluredir', '../allure-results'])
    # 使用命令生成测试报告 注:在终端中使用命令时要cd 进入当前文件夹之前命令 否则文件夹的相对路径会错误
    # os.system('allure generate ../allure-results -o ../allure-report --clean')
