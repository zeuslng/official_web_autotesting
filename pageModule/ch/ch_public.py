
import utils.TestTool as tool
from selenium.webdriver.common.by import By


class Public:

    def __init__(self, driver):
        self.driver = driver

    """-------------------底部信息栏-------------------"""

    # 电话
    phone = (By.XPATH, '/html/body/footer/div[1]/div/div[1]/p[1]/span[2]')
    # 公司邮箱
    company_email = (By.XPATH, '/html/body/footer/div[1]/div/div[1]/p[2]/span[2]')
    # HR邮箱
    HR_email = (By.XPATH, '/html/body/footer/div[1]/div/div[2]/p/span[2]')
    # 厦门地址
    xm_addr = (By.XPATH, '/html/body/footer/div[1]/div/div[3]/p[1]/span[2]')
    # 上海地址
    sh_addr = (By.XPATH, '/html/body/footer/div[1]/div/div[3]/p[2]/span[2]')
    # 公众号二维码
    sc_img = (By.XPATH, '/html/body/footer/div[1]/div/div[4]/img')

    """-------------------悬浮按钮-------------------"""

    # 悬浮按钮
    side_btn = (By.XPATH, '/html/body/div[9]/div/div[1]')
    # 客服微信
    serve_img = (By.XPATH, '/html/body/div[9]/div/div[1]/div[3]/div/img')
    # 客服电话
    serve_phone = (By.XPATH, '/html/body/div[9]/div/div[1]/div[3]/div/p')
    # 返回顶端按钮
    to_top_btn = (By.XPATH, '/html/body/div[9]/div/div[2]/div/div')
    # 放大后的二维码
    big_serve_img = (By.XPATH, '/html/body/div[8]/div/div/img')
    # 关闭按钮
    close_btn = (By.XPATH, '/html/body/div[8]/div/img')

    def get_big_serve_img(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.big_serve_img)

    def get_close_btn(self):
        return tool.wait_ele_be_founded(self.driver, 10, *self.close_btn)

    def get_phone(self):
        return tool.find_element(self.driver, *self.phone)

    def get_company_email(self):
        return tool.find_element(self.driver, *self.company_email)

    def get_hr_email(self):
        return tool.find_element(self.driver, *self.HR_email)

    def get_xm_addr(self):
        return tool.find_element(self.driver, *self.xm_addr)

    def get_sh_addr(self):
        return tool.find_element(self.driver, *self.sh_addr)

    def get_sc_img(self):
        return tool.find_element(self.driver, *self.sc_img)

    def get_side_btn(self):
        return tool.find_element(self.driver, *self.side_btn)

    def get_serve_img(self):
        return tool.find_element(self.driver, *self.serve_img)

    def get_serve_phone(self):
        return tool.find_element(self.driver, *self.serve_phone)

    def get_to_top_btn(self):
        return tool.find_element(self.driver, *self.to_top_btn)