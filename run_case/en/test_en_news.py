
import sys
import os
import time

import allure
import pytest
from selenium.webdriver.common.by import By
import utils.TestTool as tool
import pageModule.en.en_news as news

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)
news_url = 'https://www.sucheon.com/en/news.html'
myskip = pytest.mark.skip


@myskip
class TestNews(object):

    feature = '最新动态-英文'

    def setup_class(self) -> None:
        self.driver = tool.get_driver()
        self.news = news.News(self.driver)
        self.driver.get(news_url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        print('"====有异常抛出也会结束进程关掉driver====')
        self.driver.quit()

    def setup(self):
        # 每个用例运行时都重新打开页面 避免被上一个失败用例影响
        self.driver.get(news_url)

    """-----------------头部banner-----------------"""

    @allure.feature(feature)
    @allure.story('头部banner')  # 用例模块
    @allure.description('查看头部banner图片文字是否显示')  # 用例描述
    @allure.title('头部banner显示测试')  # 用例标题
    def test_header_1(self):
        txt = self.news.get_header_txt()
        img = self.news.get_header_img()
        if txt.text is None or tool.is_img_loaded(self.driver, img) is False:
            tool.raise_and_screen(self.driver, '疑似头部banner文字或者图片未加载')

    """-----------------info-----------------"""

    @allure.feature(feature)
    @allure.story('info')  # 用例模块
    @allure.description('查看info页的新闻是否显示正常')  # 用例描述
    @allure.title('info测试')  # 用例标题
    def test_info_1(self):
        # 重新跳转到最新动态页
        self.driver.get(news_url)
        # 先滚动到底部 让新闻全部加载完成
        tool.scroll_to_bottom(self.driver)
        time.sleep(5)
        tool.scroll_to_top(self.driver)
        # 遍历新闻卡片
        all_news = len(self.news.get_all_news_cards())
        for n in range(all_news):
            # 获取卡片
            card = tool.find_element(self.driver, *(By.XPATH, self.news.news_cards[1]+f'[{n+1}]'))
            tool.scroll_to_element(self.driver, card)
            time.sleep(0.5)
            # 获取卡片标题
            card_title = card.find_element(*self.news.card_title).text
            if card_title is None:
                tool.raise_and_screen(self.driver, '疑似新闻标题为空')
            # 点击新闻卡片进入详情页
            card.click()
            # 获取详情页标题判断是否一直
            title = tool.wait_element_be_found(self.driver, self.news.news_title[1], 5).text
            if title != card_title:
                tool.raise_and_screen(self.driver, '跳转后标题与卡片不一致')
            # 进入新闻详情后直接滚动到底部让所有内容先加载
            tool.scroll_to_bottom(self.driver)
            time.sleep(5)
            # 获取当前页所有图片
            all_img = self.news.get_all_img()
            if tool.test_fail_img_nums(self.driver, all_img) > 0:
                tool.raise_and_screen(self.driver, '疑似存在图片未加载')
            self.driver.back()

    # 英文版只有一页新闻 暂时跳过
    @pytest.mark.skip
    @allure.feature(feature)
    @allure.story('全部新闻')  # 用例模块
    @allure.description('点击上一页下一页按钮测试切换分页是否正常')  # 用例描述
    @allure.title('分页切换测试')  # 用例标题
    def test_all_news_2(self):
        # 重新跳转到最新动态页
        tool.scroll_to_bottom(self.driver)
        btns = tool.wait_element_be_found(self.driver, self.news.page_btn[1][:-7], 5)
        # 点击跳转到第二页
        page_2 = btns.find_elements(By.XPATH, 'button')[2]
        page_2.click()
        tool.scroll_to_bottom(self.driver)
        """跳转到新页面后 相同的元素无法重复使用 需要重新定位"""
        btns = tool.wait_element_be_found(self.driver, self.news.page_btn[1][:-7], 5)
        page_2 = btns.find_elements(By.XPATH, 'button')[2]
        # 查看第二页按钮是否高亮
        if page_2.get_attribute('class') != 'active':
            tool.raise_and_screen(self.driver, '疑似点击页码切换失败')
        # 上一页按钮
        per_btn = btns.find_elements(By.XPATH, 'button')[0]
        # 点击切换到上一页
        per_btn.click()
        tool.scroll_to_bottom(self.driver)
        btns = tool.wait_element_be_found(self.driver, self.news.page_btn[1][:-7], 5)
        # 查看此时第一页页码是否高亮
        page_1 = btns.find_elements(By.XPATH, 'button')[1]
        if page_1.get_attribute('class') != 'active':
            tool.raise_and_screen(self.driver, '疑似点击页码切换失败')
        # 再点击下一页
        next_btn = btns.find_elements(By.XPATH, 'button')[-1]
        next_btn.click()
        # 查看此时第二页页码是否高亮
        tool.scroll_to_bottom(self.driver)
        btns = tool.wait_element_be_found(self.driver, self.news.page_btn[1][:-7], 5)
        page_2 = btns.find_elements(By.XPATH, 'button')[2]
        if page_2.get_attribute('class') != 'active':
            raise tool.raise_and_screen(self.driver, '疑似点击页码切换失败')


if __name__ == '__main__':
    # 使用pytest执行用例，并获取allure执行结果
    pytest.main(['-s', './test_en_news.py', '--alluredir', '../allure-results'])
    # 使用命令生成测试报告 注:在终端中使用命令时要cd 进入当前文件夹之前命令 否则文件夹的相对路径会错误
    # os.system('allure generate ../allure-results -o ../allure-report --clean')
