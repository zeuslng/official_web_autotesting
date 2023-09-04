import datetime
import os
import platform
import time
import allure
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException, \
    WebDriverException, StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# import run_case.test_run_case as trc
from utils.RetryCase import replay_case_fail

# 打印当前时间
current_time = time.strftime("%m-%d-%H_%M", time.localtime(time.time()))
current_time1 = time.strftime("%Y-%m-%d", time.localtime(time.time()))


def get_driver():

    # 无界面运行时打开----------------------
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # driver = webdriver.Chrome(options=chrome_options)
    # # 无界面模式下默认不是全屏，所以需要设置一下分辨率
    # driver.set_window_size(1920, 937)
    # 无界面运行时打开----------------------

    if platform.system().lower() == 'windows':
        print("======windows======")
        cap = {
            "browserName": "chrome",
        }
        # driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', cap)
        driver = webdriver.Remote('http://192.168.1.7:4444/wd/hub', cap)
        # driver = webdriver.Chrome()
        driver.implicitly_wait(10.0)
        return driver
    elif platform.system().lower() == 'linux':
        print("======linux======")
        cap = {
            "browserName": "chrome",
        }
        driver = webdriver.Remote('http://192.168.1.7:4444/wd/hub', cap)
        driver.implicitly_wait(10.0)
        return driver


def wait_ele_be_founded(driver, timeout=10, *locator):
    """
    《新方法》
    等待一定时间直到单个元素被查找到
    :param driver: 驱动
    :param timeout: 超时时间
    :param locator: 定位器元组——》（By.Xpath, 'xxxx'）
    :return: 找到则返回元素，未找到则抛异常
    """
    ele = wait_until_true(find_element, timeout, driver, *locator)
    if not ele:
        raise_and_screen(driver, '该元素在%s秒内未在页面上找到，请通过截图检查' % timeout)
    return ele


def wait_eles_be_founded(driver, timeout=10, *locator):
    """
    《新方法》
    等待一定时间直到多个元素被查找到
    :param driver: 驱动
    :param timeout: 超时时间
    :param locator: 定位器元组——》（By.Xpath, 'xxxx'）
    :return: 找到则返回元素，未找到则抛异常
    """
    ele = wait_until_true(find_elements, timeout, driver, *locator)
    if not ele:
        raise_and_screen(driver, '该元素在%s秒内未在页面上找到，请通过截图检查' % timeout)
    return ele


def is_element_visible(element):
    """
    返回该元素是否可见
    :param element:
    :return:
    """
    return element.is_displayed()


def is_element_clickable(element):
    """
    返回该元素是否可见
    :param element:
    :return:
    """
    return element.is_enabled()


def wait_until_true(method, timeout=10, *args, **kwargs):
    """
    执行传入的方法直到该方法返回值为true，超时返回false
    :param method: 需要判断的方法
    :param timeout: 超时时长
    :return:
    """
    end_time = time.time() + timeout
    while True:
        try:
            if hasattr(method, '__call__'):
                value = method(*args, **kwargs)
                if value:
                    return value
        except Exception:
            pass
        time.sleep(0.5)
        if time.time() > end_time:
            break
    return False


def wait_until_false(method, timeout=10, *args, **kwargs):
    """
    执行传入的方法直到该方法返回值为false，超时返回true
    :param method: 需要判断的方法
    :param timeout: 超时时长
    :return:
    """
    end_time = time.time() + timeout
    while True:
        try:
            value = method(*args, **kwargs)
            if not value:
                return value
        except Exception:
            pass
        time.sleep(0.5)
        if time.time() > end_time:
            break
    return True


def raise_and_screen(driver, msg):
    """
    抛出异常并截图
    :param driver: 驱动
    :param msg: 异常信息
    :return:
    """
    get_allure_screen_shoot(driver, '异常截图')
    raise Exception(msg)


def get_css_property(ele, css):
    """获取元素是css样式属性"""
    return ele.value_of_css_property(css)


def check_exception(func, ele_name, driver, *args, **kwargs):
    """
    :param func:为需要进行异常捕获的方法
    :param ele_name: 元素名
    :param driver: 驱动
    :param **args：func函数的参数
    :param **kwargs：func函数的参数
    封装异常类 对元素操作步骤方法抛出的异常信息进行简化， 便于确定异常原因
    使用方法 在测试用例中调用该方法:check_exception(func, '元素名：ele_name‘, arg, arg, ...)
    """
    try:
        result = func(*args, **kwargs)
        return result
    except ElementClickInterceptedException as e:
        get_allure_screen_shoot(driver, '元素："' + ele_name + '"' + '是否可点击待确认截图')
        raise Exception('元素：' + ele_name + ' 无法点击，可能由于网速原因未加载，请查看测试步骤截图确认元素是否出现！'
                                           '若存在，请忽略该异常！')
    except StaleElementReferenceException as e:
        get_allure_screen_shoot(driver, '元素："' + ele_name + '"' + '是否存在待确认截图')
        raise Exception('元素：' + ele_name + ' 无法定位到该元素，可能由于网络原因未加载，请查看测试步骤截图确认元素是否出现！'
                                           '若存在，请忽略该异常！')
    except NoSuchElementException as e:
        get_allure_screen_shoot(driver, '元素："' + ele_name + '"' + '是否存在待确认截图')
        raise Exception('元素：' + ele_name + ' 无法定位到该元素，可能由于网络原因未加载，请查看测试步骤截图确认元素是否出现！'
                                           '若存在，请忽略该异常！')
    except IndexError as e:
        raise Exception('数组下标越界！')
    except TimeoutException as e:
        get_allure_screen_shoot(driver, '元素："' + ele_name + '"' + '是否存在待确认截图')
        raise Exception('元素：' + ele_name + ' 查找元素超时，可能由于网络原因未加载，或者查看测试步骤截图确认元素是否出现！'
                                           '若存在，请忽略该异常！')
    except ElementNotInteractableException as e:
        get_allure_screen_shoot(driver, '元素："' + ele_name + '"' + '是否存在待确认截图')
        raise Exception('元素：' + ele_name + ' 元素无法交互，可能由于网络原因未加载，或者查看测试步骤截图确认元素是否出现！'
                                           '若存在，请忽略该异常！')
    except WebDriverException as e:
        raise Exception('浏览器驱动异常！可能由于测试节点被占用导致无法进行测试，该异常并非界面UI异常！请重新测试！')


def click_ele(ele_name, driver, ele):
    """
    点击元素
    """
    # if ele_name != '':
    #     get_allure_screen_shoot(driver, '点击"' + ele_name + '"前')
    time.sleep(0.5)
    ele.click()
    time.sleep(0.5)
    if ele_name != '':
        get_allure_screen_shoot(driver, '点击"' + ele_name + '"')


def wait_element_clickable(driver, *locator, time_out=10):
    """
    等待一定时间至元素可点击，超时则报错
    :param driver: 驱动
    :param locator: 定位器 :（By.xpath, 'xxxxxxxxx'）
    :param time_out: 超时时间 默认10秒
    """
    wait = WebDriverWait(driver, time_out, 0.3)
    value = wait.until(EC.element_to_be_clickable(locator))
    return value


def wait_element_not_clickable(driver, *locator, time_out=10):
    """
    等待一定时间至元素不可点击，超时则报错
    :param driver: 驱动
    :param locator: 定位器 :（By.xpath, 'xxxxxxxxx'）
    :param time_out: 超时时间 默认10秒
    """
    try:
        wait = WebDriverWait(driver, time_out, 0.3)
        value = wait.until_not(EC.element_to_be_clickable(locator))
        return value
    except Exception as e:
        get_allure_screen_shoot(driver, '可点击异常截图')
        raise Exception(e)


def find_element(driver, *locator):
    """
    定位元素
    :param driver: 驱动
    :param locator: 定位器 :（By.xpath, 'xxxxxxxxx'）
    :return: 定位的元素
    """
    ele = driver.find_element(*locator)
    return ele


def find_elements(driver, *locator):
    """
    获取元素集合
    :param driver: 驱动
    :param locator: 定位器 :（By.xpath, 'xxxxxxxxx'）
    :return: 定位的元素的list
    """
    elements = driver.find_elements(*locator)
    return elements


def clear_input(driver, *locator):
    """
    清空输入框
    :param driver: 驱动
    :param locator: 定位器 例：（By.XPATH, 'path'）
    """
    input_btn = driver.find_element(*locator)
    input_btn.clear()


def get_different_tag_element(driver, text, target_tag_name):
    """
    该方法使用场景：根据文本查询元素时会查询到多个包含相同文本但是tag不同的元素，且目标元素为其中一个与其他tag不同的元素，
    此时可通过此方法过了掉其他元素，获取目标tag元素
    :param driver: 驱动
    :param text: 查找元素的文本，需要完全匹配
    :param target_tag_name: 目标tag（div,li,ul等等）
    :return: target_element:返回目标目标元素
    """
    target_element = None
    elements = driver.find_elements_by_xpath(get_xpath_with_text_all(text))
    if len(elements) == 0:
        raise Exception('没有找到包含对应文本的元素！请确定输入的内容！')
    for ele in elements:
        print(ele.tag_name)
        if ele.tag_name == target_tag_name:
            target_element = ele
            return target_element
    return target_element


def wait_element_clickable_until(driver, *ele_path):
    """
    等待元素可点击直到设定的超时时间
    :param driver:驱动
    :param time_out: 判断的超时时间
    :param ele_path: 元素xpath
    :return ele 返回该元素
    """
    wait = WebDriverWait(driver, 10, 0.3)
    ele = wait.until(EC.element_to_be_clickable(ele_path))
    return ele


def get_xpath_with_text_all(text):
    """
    将传入的文字转换成根据完全匹配的文本查询元素的xpath
    :param text:文本
    :return: 转换后的文本 如："//*[text()='传入的文本']"
    """
    path = "//*[text()='%s']" % text
    return path


def get_xpath_with_text_contains(text):
    """
    将传入的文字转换成根据部分匹配的文本查询元素的xpath
    :param text:文本
    :return: 转换后的文本 如："//*[contains(text(),'***传入的文本**')]"
    """
    path = "//*[contains(text(),'%s')]" % text
    return path


def is_text_exit_in_element(driver, timeout, path, text):
    """
    判断某些文本是否存在指定元素当中，只能判断html的文本 不能判断dom元素属性中的文本如：placeholder='测试' 无法判断
    这个方法需要元素可见 否则会报错
    :param driver: 驱动
    :param timeout: 超时时间
    :param path: 元素的xpath
    :param text: 需要检测的文本
    :return: 存在返回True,不存在返回False
    """
    locator = ('xpath', path)
    wait = WebDriverWait(driver, timeout, 0.3)
    flag = wait.until(EC.text_to_be_present_in_element(locator, text))
    return flag


def wait_element_be_found(driver, xpath, timeout):
    """
    获取某个元素并设置超时时间
    :param driver:驱动
    :param xpath:寻找元素的xpath
    :param timeout:超时时间int类型
    :return: element:返回被找到的元素
    """
    wait = WebDriverWait(driver, timeout, 0.3)
    ele = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return ele


def is_element_exit(driver, element_xpath):
    """
    判断元素是否存在 存在返回True 不存在返回False
    :param driver: 驱动
    :param element_xpath: 元素的xpath
    :return: 存在返回True 不存在返回False
    """
    try:
        wait = WebDriverWait(driver, 10, 0.3)
        element = wait.until(EC.presence_of_element_located((By.XPATH, element_xpath)))
        return True
    except:
        get_allure_screen_shoot(driver, '异常截图')
        return False


def move_to_element_or_click(driver, element, click=0, ele_name=None):
    """
    鼠标悬停到某个元素表面
    :param driver: 驱动
    :param element: 需要悬停的元素
    :param click: 是否需要点击 若需要点击操纵则传入1 默认没有点击操作
    :param ele_name: 点击的元素名称
    :return:
    """
    actions = ActionChains(driver)
    if click == 0:
        actions.move_to_element(element).perform()
    else:
        actions.move_to_element(element).perform()
        time.sleep(1)
        click_ele('元素名称', driver, element)


def get_current_mon_day():
    """
    获取当前的月份和日期
    :return: 返回字符串形式的当日的月份日期 mm-dd(如：12-25)
    """
    now_day = datetime.date.today()  # 当天
    start_day = now_day - datetime.timedelta(days=1)  # 开始日期
    date = start_day.strftime('%m-%d')
    return date


def get_allure_screen_shoot(driver, pic_name):
    """
    allure测试报告截图功能
    :param driver: 浏览器驱动
    :param pic_name: 保存的图片名称
    :return:
    """
    allure.attach(driver.get_screenshot_as_png(), pic_name, attachment_type=allure.attachment_type.PNG)


def scroll_to_element(driver, element):
    """
    滚动到对应的元素
    :param driver: 浏览器驱动
    :param element: 需要滚动到的元素
    """
    # 滚动屏幕到指定元素的js
    scroll_js = 'arguments[0].scrollIntoView()'
    driver.execute_script(scroll_js, element)
    time.sleep(0.5)

def scroll_to_top(driver):
    """
    滚动到顶部
    """
    js_top = "var q=document.documentElement.scrollTop=0"
    driver.execute_script(js_top)
    time.sleep(1.0)


def scroll_to_bottom(driver):
    """
    滚动到底部
    """
    js_bottom = "window.scrollTo(0,document.body.scrollHeight);"
    driver.execute_script(js_bottom)
    time.sleep(1.0)


def is_img_loaded(driver, img):
    """
    判断图片是否加载完成
    :param driver: 浏览器驱动
    :param img: 图片
    :return:
    """
    js_judgement_img = \
        'return arguments[0].complete && typeof arguments[0].naturalWidth ' \
        '!= \"undefined\" && arguments[0].naturalWidth > 0'
    flag = driver.execute_script(js_judgement_img, img)
    return flag


def test_fail_img_nums(driver, images):
    """
    校验异常图片个数 并输出有多少张图片未加载或有异常
    :param driver: 浏览器驱动
    :param images: 图片的集合
    """
    i = 0
    for img in images:
        scroll_to_element(driver, img)
        load = wait_until_true(is_img_loaded, 10, driver, img)
        visible = wait_until_true(is_element_visible, 10, img)
        if not load or not visible:
            i += 1
            get_allure_screen_shoot(driver, '异常图片')
    print('有', i, '张图片未加载或者加载时间过长')
    return i


def is_element_exit_by_method(driver, method, value):
    """
    根据传入的元素定位方式判断元素是否存在
    例:method=xpath、value=/div/div[2]/div/div[1]/span[1]
    :param driver: 浏览器驱动
    :param method: 根据什么方法来查询元素
    :param value: 查询的参数
    """
    try:
        element = driver.find_element(by=method, value=value)
    except NoSuchElementException as e:
        print(format(e))
        return False
    else:
        return True


def chose_search_time(driver, date_bef):
    """
    修改查询时间
    :param driver: 浏览器驱动
    :param date_bef: 往前查询的天数 需要查前一天的则传入1
    :return date : 返回查询的日期 用做截图文件名后缀
    """
    # 选择查询时间
    now_day = datetime.date.today()  # 当天
    start_day = now_day - datetime.timedelta(days=date_bef)  # 开始日期
    start_time = start_day.strftime('%Y-%m-%d') + ' 00:00:00'  # 开始的具体时间
    end_day = start_day + datetime.timedelta(days=1)  # 结束日期
    end_time = end_day.strftime('%Y-%m-%d') + ' 00:00:00'  # 结束的具体时间
    date = start_day.strftime('%m-%d')

    start_input = driver.find_element_by_xpath('//*[@id="history"]/div[1]/form/div[3]/div/div/input[1]')
    end_input = driver.find_element_by_xpath('//*[@id="history"]/div[1]/form/div[3]/div/div/input[2]')
    index = 1
    # 删除开始时间
    while index <= 18:
        start_input.send_keys(Keys.BACK_SPACE)
        index += 1
    start_input.send_keys(start_time[1:])
    index = 1
    # 删除结束时间
    while index <= 18:
        end_input.send_keys(Keys.BACK_SPACE)
        index += 1
    end_input.send_keys(end_time[1:])
    time.sleep(1)
    # 点击空白处 触发查询
    ele = driver.find_element_by_xpath('//*[@id="history"]/div[1]/form/div[3]/label')
    click_ele('空白处', driver, ele)
    time.sleep(2)
    return date


def rename_folder(root_dir, folder_name):  # 修改rootDir路径下的文件夹名
    """
    重命名文件夹 （点位快照需求项目所使用）
    :param root_dir: 待改名的文件夹所在的目录
    :param folder_name: 需要修改的文件夹的原名
    """
    num = 0
    dirs = os.listdir(root_dir)
    for folder in dirs:
        num = num + 1
        name_error = folder_name + '（异常）'
        if folder == name_error:
            break
        elif folder == folder_name:
            temp = folder + '（异常）'
            old_name = os.path.join(root_dir, folder)  # 老文件夹的名字
            new_name = os.path.join(root_dir, temp)  # 新文件夹的名字
            os.rename(old_name, new_name)  # 替换
            break
