import utils.TestTool as tool
from selenium.webdriver.common.by import By

"""
首页中文版页面元素及部分操作封装
"""


class Home:

    def __init__(self, driver):
        self.driver = driver

    """""-------------------头部banner元素""-------------------"""
    # banner父节点
    banner_header = (By.XPATH, '/html/body/section[1]/div/div')

    # 第1个banner的文字
    banner_1 = (By.XPATH, '/html/body/section[1]/div/div/div[2]/div/p[1]')
    # 第2个banner的文字
    banner_2 = (By.XPATH, '/html/body/section[1]/div/div/div[3]/div/p')
    # 第3个banner的文字
    banner_3 = (By.XPATH, '/html/body/section[1]/div/div/div[4]/div[2]/p')

    # 第1个banner的按钮
    banner_1_btn = (By.XPATH, '/html/body/section[1]/div/div/div[2]/div/a')
    # 第2个banner的按钮
    banner_2_btn = (By.XPATH, '/html/body/section[1]/div/div/div[3]/div/div[2]')
    # 第3个banner的按钮
    banner_3_btn = (By.XPATH, '/html/body/section[1]/div/div/div[4]/div[2]/a')

    # 第1个banner的切换按钮
    banner_1_line = (By.XPATH, '/html/body/section[1]/div/div/div[5]/span[1]')
    # 第2个banner的切换按钮
    banner_2_line = (By.XPATH, '/html/body/section[1]/div/div/div[5]/span[2]')
    # 第3个banner的切换按钮
    banner_3_line = (By.XPATH, '/html/body/section[1]/div/div/div[5]/span[3]')
    # 视频
    video = (By.XPATH, '//*[@id="video"]')
    # 视频关闭按钮
    video_close = (By.XPATH, '/html/body/div[2]/img')

    def get_video_close(self):
        """视频关闭按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.video_close)

    def get_banner_1_line(self):
        """第1个banner的切换按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.banner_1_line)

    def get_banner_2_line(self):
        """第2个banner的切换按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.banner_2_line)

    def get_banner_3_line(self):
        """第3个banner的切换按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.banner_3_line)

    def get_video(self):
        """视频"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.video)

    def get_banner_1_txt(self):
        """头部banner1文字"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.banner_1)

    def get_banner_2_txt(self):
        """头部banner2文字"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.banner_2)

    def get_banner_3_txt(self):
        """头部banner2文字"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.banner_3)

    def get_banner_1_btn(self):
        """了解更多按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.banner_1_btn)

    def get_banner_2_btn(self):
        """观看视频按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.banner_2_btn)

    def get_banner_3_btn(self):
        """加入我们按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.banner_3_btn)

    """""-------------------产品功能部分banner""-------------------"""
    # 标题文案 定位使用
    title1 = (By.XPATH, '/html/body/div[3]/span')

    # 按钮父节点
    function = (By.XPATH, '/html/body/div[4]/div')
    # 预测性维护
    function_1 = (By.XPATH, '/html/body/div[4]/div/div[1]/div/div[1]')
    # 产品自动化质检
    function_2 = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]')
    # 环境异常报警
    function_3 = (By.XPATH, '/html/body/div[4]/div/div[3]/div/div[1]')
    # 设备远程监控
    function_4 = (By.XPATH, '/html/body/div[4]/div/div[4]/div/div[1]')
    # 产线实时监测
    function_5 = (By.XPATH, '/html/body/div[4]/div/div[5]/div/div[1]')

    def scroll_to_title1(self):
        """滚动到产品功能部分"""
        tool.scroll_to_element(self.driver, tool.wait_ele_be_founded(self.driver, 10, *self.title1))

    def get_function_1(self):
        """预测性维护按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.function_1)

    def get_function_2(self):
        """产品自动化质检按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.function_2)

    def get_function_3(self):
        """环境异常报警按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.function_3)

    def get_function_4(self):
        """设备远程监控按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.function_4)

    def get_function_5(self):
        """产线实时监测按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.function_5)

    # 轮播图父节点
    banner_function = (By.XPATH, '/html/body/section[2]/div/div')
    # 第1个轮播图文案
    function_1_txt = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/p[1]')
    # 第2个轮播图文案
    function_2_txt = (By.XPATH, '/html/body/section[2]/div/div/div[3]/div/p[1]')
    # 第3个轮播图文案
    function_3_txt = (By.XPATH, '/html/body/section[2]/div/div/div[4]/div/p[1]')
    # 第4个轮播图文案
    function_4_txt = (By.XPATH, '/html/body/section[2]/div/div/div[5]/div/p[1]')
    # 第5个轮播图文案
    function_5_txt = (By.XPATH, '/html/body/section[2]/div/div/div[6]/div/p[1]')

    def get_function_1_txt(self):
        """预测性维护文案"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.function_1_txt)

    def get_function_2_txt(self):
        """产品自动化质检文案"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.function_2_txt)

    def get_function_3_txt(self):
        """环境异常报警文案"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.function_3_txt)

    def get_function_4_txt(self):
        """设备远程监控文案"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.function_4_txt)

    def get_function_5_txt(self):
        """产线实时监测文案"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.function_5_txt)

    """-------------------产品特点部分""-------------------"""
    # 标题文案 定位使用
    title2 = (By.XPATH, '/html/body/section[3]/div[1]/div/span')
    # 轮播图父节点
    banner_special = (By.XPATH, '/html/body/section[3]')
    # 左滑按钮
    btn_l = (By.XPATH, '/html/body/section[3]/div[3]/img[1]')
    # 右滑按钮
    btn_r = (By.XPATH, '/html/body/section[3]/div[3]/img[2]')
    # 第1个轮播图数字
    special_1 = (By.XPATH, '/html/body/section[3]/div[2]/div/div/div[7]/div[3]')
    # 第2个轮播图数字
    special_2 = (By.XPATH, '/html/body/section[3]/div[2]/div/div/div[8]/div[3]')
    # 第3个轮播图数字
    special_3 = (By.XPATH, '/html/body/section[3]/div[2]/div/div/div[9]/div[3]')
    # 第4个轮播图数字
    special_4 = (By.XPATH, '/html/body/section[3]/div[2]/div/div/div[10]/div[3]')
    # 第5个轮播图数字
    special_5 = (By.XPATH, '/html/body/section[3]/div[2]/div/div/div[11]/div[3]')
    # 第6个轮播图数字
    special_6 = (By.XPATH, '/html/body/section[3]/div[2]/div/div/div[12]/div[3]')

    def scroll_to_title2(self):
        """滚动到产品特点部分"""
        tool.scroll_to_element(self.driver, tool.wait_ele_be_founded(self.driver, 10, *self.title2))

    def get_btn_l(self):
        """向左切换按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.btn_l)

    def get_btn_r(self):
        """向右切换按钮"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.btn_r)

    def get_special_1(self):
        """第1个轮播图数字"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.special_1)

    def get_special_2(self):
        """第2个轮播图数字"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.special_2)

    def get_special_3(self):
        """第3个轮播图数字"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.special_3)

    def get_special_4(self):
        """第4个轮播图数字"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.special_4)

    def get_special_5(self):
        """第5个轮播图数字"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.special_5)

    def get_special_6(self):
        """第6个轮播图数字"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.special_6)

    def get_all_special(self):
        """获取所有特点介绍卡片"""
        res = [self.get_special_1(), self.get_special_2(),
               self.get_special_3(), self.get_special_4(),
               self.get_special_5(), self.get_special_6()]
        return res

    def check_high_light(self):
        """判断产品特点轮播图当前是第几张卡片高亮"""
        high = 0
        for i in self.get_all_special():
            high += 1
            if i.value_of_css_property('color') == 'rgba(255, 128, 0, 1)':
                break
        return high

    """""-------------------客户部分""-------------------"""
    # 标题文案 定位使用
    title3 = (By.XPATH, '/html/body/div[5]/div[3]/p[1]')
    # 客户数量
    customer_num = (By.XPATH, '//*[@id="thank-num"]')
    # 客户行业 共十个
    customer_types = [f'/html/body/div[5]/div[4]/div[{i}]/a' for i in range(1, 11)]
    # 华为云logo 最外层的logo 判断最后透明度是否为1
    hw_logo = (By.XPATH, '/html/body/div[5]/img[4]')

    def scroll_to_title3(self):
        """滚动到客户部分"""
        tool.scroll_to_element(self.driver, tool.wait_ele_be_founded(self.driver, 10, *self.title3))

    def get_customer_num(self):
        """客户数量"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.customer_num)

    def get_hw_logo(self):
        """华为logo"""
        return tool.wait_ele_be_founded(self.driver, 10, *self.hw_logo)

    def get_customer_types(self):
        """客户类型 返回所有类型的名称集合<a>标签"""
        res = [tool.wait_ele_be_founded(self.driver, 10, *(By.XPATH, i)) for i in self.customer_types]
        return res

    """""-------------------合作伙伴部分""-------------------"""
    title4 = (By.XPATH, '/html/body/section[4]/div/span')
    # 合作伙伴logo 判断图片是否加载
    coop_logos_path = [f'/html/body/section[4]/section/div/div[{i}]/img' for i in range(1, 11)]

    def scroll_to_title4(self):
        """滚动到合作伙伴部分"""
        tool.scroll_to_element(self.driver, tool.wait_ele_be_founded(self.driver, 10, *self.title4))

    def get_coop_logos(self):
        """获取所有合作伙伴图片 返回img类型列表"""
        res = [tool.wait_ele_be_founded(self.driver, 10, *(By.XPATH, i)) for i in self.coop_logos_path]
        return res
