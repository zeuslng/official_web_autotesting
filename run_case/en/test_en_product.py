"""
公共模块测试用例（特别关注、异常报警等）
"""
import sys
import os
import time

import allure
import pytest
import utils.TestTool as tool
import pageModule.en.en_products as product

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)
product_url = 'https://www.sucheon.com/en/product.html'
myskip = pytest.mark.skip


@myskip
class TestProduct(object):

    feature = '产品介绍-英文'

    def setup_class(self) -> None:
        self.driver = tool.get_driver()
        self.product = product.Product(self.driver)
        self.driver.get(product_url)
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
        txt = self.product.get_header_txt()
        img = self.product.get_header_img()
        visible = tool.wait_until_true(tool.is_element_visible, 10, img)
        if txt.text is None or not visible or tool.wait_until_true(tool.is_img_loaded, 5, self.driver, img) is False:
            tool.raise_and_screen(self.driver, '疑似头部banner文字或者图片未加载')

    """-----------------产品架构-----------------"""

    @allure.feature(feature)
    @allure.story('产品架构')  # 用例模块
    @allure.description('查看产品架构图片文字是否显示')  # 用例描述
    @allure.title('产品架构显示测试')  # 用例标题
    def test_framework_1(self):
        """第一行图片"""
        self.product.scroll_to_title1()
        txt1 = self.product.get_line_1_txt()
        img1 = self.product.get_line_1_img1()
        img2 = self.product.get_line_1_img2()
        visible1 = tool.wait_until_true(tool.is_element_visible, 10, img1)
        visible2 = tool.wait_until_true(tool.is_element_visible, 10, img2)
        load1 = tool.wait_until_true(tool.is_img_loaded, 5, self.driver, img1)
        load2 = tool.wait_until_true(tool.is_img_loaded, 5, self.driver, img2)
        if txt1.text is None or not visible1 or not visible2 or not load1 or not load2:
            tool.raise_and_screen(self.driver, '疑似文字或者图片未加载')

        """第二行图片"""
        tool.scroll_to_element(self.driver, self.product.get_line_2_img1())
        txt2 = self.product.get_line_2_txt()
        img3 = self.product.get_line_2_img1()
        img4 = self.product.get_line_2_img2()
        visible3 = tool.wait_until_true(tool.is_element_visible, 10, img3)
        visible4 = tool.wait_until_true(tool.is_element_visible, 10, img4)
        load3 = tool.wait_until_true(tool.is_img_loaded, 5, self.driver, img3)
        load4 = tool.wait_until_true(tool.is_img_loaded, 5, self.driver, img4)
        if txt2.text is None or not visible3 or not visible4 or not load3 or not load4:
            tool.raise_and_screen(self.driver, '疑似文字或者图片未加载')

        """第三行图片"""
        txt3 = self.product.get_line_3_txt()
        img5 = self.product.get_line_3_img()
        visible5 = tool.wait_until_true(tool.is_element_visible, 10, img5)
        load5 = tool.wait_until_true(tool.is_img_loaded, 5, self.driver, img5)
        if txt3.text is None or not visible5 or not load5:
            tool.raise_and_screen(self.driver, '疑似文字或者图片未加载')

    """-----------------多维数据-----------------"""

    """-----------------便捷设备管理-----------------"""

    @allure.feature(feature)
    @allure.story('便捷设备管理')  # 用例模块
    @allure.description('查看设备图片文字是否显示')  # 用例描述
    @allure.title('设备图片显示测试')  # 用例标题
    def test_ep_1(self):
        self.product.scroll_to_title3()
        images = self.product.get_ep_images()
        for i in images:
            visible = tool.wait_until_true(tool.is_element_visible, 10, i)
            if not tool.wait_until_true(tool.is_img_loaded, 5, self.driver, i) or not visible:
                tool.raise_and_screen(self.driver, '疑似存在图片未加载')

    """-----------------定制化服务-----------------"""

    @allure.feature(feature)
    @allure.story('定制化服务')  # 用例模块
    @allure.description('查看图片文字是否显示')  # 用例描述
    @allure.title('图片显示测试')  # 用例标题
    def test_serve_1(self):
        self.product.scroll_to_title4()
        images = self.product.get_all_svg()
        texts = self.product.get_all_txt()
        for i in images:
            visible = tool.wait_until_true(tool.is_element_visible, 10, i)
            if not tool.wait_until_true(tool.is_img_loaded, 5, self.driver, i) or not visible:
                raise Exception('疑似存在图片未加载')
        for t in texts:
            if t.text is None or tool.wait_until_true(tool.is_element_visible, 10, t) is False:
                tool.raise_and_screen(self.driver, '疑似存在文案未加载')

    """-----------------应用现场实景-----------------"""

    @allure.feature(feature)
    @allure.story('应用现场实景')  # 用例模块
    @allure.description('查看图片文字是否显示')  # 用例描述
    @allure.title('图片显示测试')  # 用例标题
    def test_apply_1(self):
        self.product.scroll_to_title5()
        images = self.product.get_all_applications()
        count = 0
        for img in images:
            flag = tool.wait_until_true(tool.is_img_loaded, 5, self.driver, img)
            if not flag:
                tool.raise_and_screen(self.driver, '疑似图片加载失败')
            if img.is_displayed():
                count += 1
        if count != 5:
            tool.raise_and_screen(self.driver, '疑似存在图片未加载')
        print('可见图片数量为%s' % count)


if __name__ == '__main__':
    # 使用pytest执行用例，并获取allure执行结果
    pytest.main(['-s', './test_ch_product.py', '--alluredir', '../allure-results'])
    # 使用命令生成测试报告 注:在终端中使用命令时要cd 进入当前文件夹之前命令 否则文件夹的相对路径会错误
    # os.system('allure generate ../allure-results -o ../allure-report --clean')
