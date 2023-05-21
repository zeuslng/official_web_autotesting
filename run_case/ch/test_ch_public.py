import sys
import os
import time
import allure
import pytest

import utils.TestTool as tool
import pageModule.ch.ch_public as public

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)


home_url = 'https://www.sucheon.com/index.html'


class TestPublic(object):

    feature = '公共部分-中文'

    def setup_class(self) -> None:
        self.driver = tool.get_driver()
        self.public = public.Public(self.driver)
        self.driver.get(home_url)
        self.driver.maximize_window()

    def teardown_class(self):
        print('"====有异常抛出也会结束进程关掉driver====')
        self.driver.quit()

    """-----------------底部信息栏-----------------"""

    @allure.feature(feature)
    @allure.story('底部信息栏')  # 用例模块
    @allure.description('查看底部公司信息是否显示正确')  # 用例描述
    @allure.title('公司信息显示测试')  # 用例标题
    def test_bottom_1(self):
        time.sleep(5)
        # 悬浮按钮
        side_btn = self.public.get_side_btn()
        serve_phone = self.public.get_serve_phone()
        to_top_btn = self.public.get_to_top_btn()

        with allure.step('滚动到底部之前先判断返回顶部按钮有没有显示'):
            if to_top_btn.is_displayed():
                tool.raise_and_screen(self.driver, '疑似返回顶部按钮在顶部显示异常')

        tool.scroll_to_bottom(self.driver)
        tool.wait_element_be_found(self.driver, self.public.phone[1], 5)

        with allure.step('滚动到底部后判断返回顶部按钮是否显示'):
            if not to_top_btn.is_displayed():
                tool.raise_and_screen(self.driver, '疑似返回顶部按钮在底部显示异常')

        phone = self.public.get_phone().text
        company_email = self.public.get_company_email().text
        hr_email = self.public.get_hr_email().text
        xm_addr = self.public.get_xm_addr().text
        sh_addr = self.public.get_sh_addr().text
        sc_img = self.public.get_sc_img()

        if phone != '0592-5222938' or phone is None:
            tool.raise_and_screen(self.driver, '疑似电话号码错误')

        if company_email != 'info@sucheon.com' or company_email is None:
            tool.raise_and_screen(self.driver, '疑似公司邮箱错误')

        if hr_email != 'hr@sucheon.com' or hr_email is None:
            tool.raise_and_screen(self.driver, '疑似简历邮箱错误')

        if xm_addr != '厦门市软件园三期诚毅北大街63号1401单元' or xm_addr is None:
            tool.raise_and_screen(self.driver, '疑似公司地址错误')

        if sh_addr != '上海市虹口区广纪路838号A棟1层122室' or sh_addr is None:
            tool.raise_and_screen(self.driver, '疑似上海地址错误')

        if not tool.is_img_loaded(self.driver, sc_img):
            tool.raise_and_screen(self.driver, '疑似公众号二维码失效')

        tool.move_to_element_or_click(self.driver, side_btn)
        tool.wait_element_clickable(self.driver, *self.public.serve_img)

        with allure.step('点击悬浮按钮'):
            tool.move_to_element_or_click(self.driver, side_btn)
            serve_img = tool.wait_element_clickable(self.driver, *self.public.serve_img)
            visible = tool.wait_until_true(tool.is_element_visible, 10, serve_img)
            if not visible or not tool.wait_until_true(tool.is_img_loaded, 10, self.driver, serve_img):
                tool.raise_and_screen(self.driver, '客服二维码疑似显示异常')
            if serve_phone.text != '0592-5222938' or not serve_phone.is_displayed:
                tool.raise_and_screen(self.driver, '客服电话疑似显示异常或错误')

        with allure.step('点击二维码放大'):
            # 点击二维码放大
            serve_img.click()
            big_img = self.public.get_big_serve_img()
            close_btn = self.public.get_close_btn()
            visible_img = tool.wait_until_true(tool.is_element_visible, 10, big_img)
            if not visible_img or not tool.wait_until_true(tool.is_img_loaded, 5, self.driver, big_img):
                tool.raise_and_screen(self.driver, '疑似点击二维码后没有放大')
            # 点击关闭按钮
            close_btn.click()
            visible_img = tool.wait_until_false(tool.is_element_visible, 10, big_img)
            if visible_img:
                tool.raise_and_screen(self.driver, '疑似关闭按钮失效，二维码无法关闭')


if __name__ == '__main__':
    # 使用pytest执行用例，并获取allure执行结果
    pytest.main(['-s', './test_ch_product.py', '--alluredir', '../allure-results'])
    # 使用命令生成测试报告 注:在终端中使用命令时要cd 进入当前文件夹之前命令 否则文件夹的相对路径会错误
    # os.system('allure generate ../allure-results -o ../allure-report --clean')
