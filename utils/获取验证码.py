import pickle
import random
import string
import time
from lib.ShowapiRequest import ShowapiRequest

from PIL import Image
import os


def get_code(driver, xpath):
    # 获取验证码图片
    t = time.time()
    path = os.path.dirname(os.path.dirname(__file__)) + '\\screenshots'
    picture_name1 = path + '\\' + str(t) + '.png'

    driver.save_screenshot(picture_name1)

    ce = driver.find_element_by_xpath(xpath)

    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    dpr = driver.execute_script('return window.devicePixelRatio')

    print(dpr)
    im = Image.open(picture_name1)
    img = im.crop((left*dpr, top*dpr, right*dpr, height*dpr))

    t = time.time()

    picture_name2 = path + '\\' + str(t) + '.png'
    img.save(picture_name2)  # 这里就是截取到的验证码图片

    r = ShowapiRequest("http://route.showapi.com/184-4", "456925", "df5348b01d1e48d6bf293ad862e3d4dd")

    r.addFilePara("image", picture_name2)
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    text = res.json()['showapi_res_body']
    code = text['Result']
    return code
