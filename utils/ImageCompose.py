import os
import shutil
from os import listdir
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def img_compose_final(scene, date, area, equipment, point, flag='h'):
    """
    该方法用于拼接单个点位的多个查询模式的所有截图
    :param scene:场景名称
    :param date: 日期
    :param area: 区域名称
    :param equipment:设备名称
    :param point: 点位名称
    :param flag: 横向拼接（h）或纵向拼接(v)
    """
    # 拼图素材路径
    path_element = f'B:\ScreenShoot\拼图素材{area}2\\'
    # 拼图保存路径
    path_save = 'B:\ScreenShoot'
    # 创建图片保存目录
    path1 = 'B:\\'
    path2 = 'ScreenShoot'
    file_path = os.path.join(path1, path2, scene, date, area)
    # 判断不包含（异常）的文件夹是否存在
    index_normal = os.path.exists(file_path)
    # 默认包含（异常）的文件名不存在
    index_error = False
    if not index_normal:
        # 如果文件名中没有（异常）的文件夹不存在则判断有（异常）的文件夹是否存在 如果都不存在则创建不包含（异常）的文件夹
        error_path = os.path.join(path1, path2, scene, date + '（异常）')
        index_error = os.path.exists(error_path)
        if not index_error:
            os.makedirs(file_path)
        else:
            file_path = os.path.join(path1, path2, scene, date + '（异常）', area)
            if not os.path.exists(file_path):
                os.makedirs(file_path)
    # 获取待拼接的图片
    ims = [Image.open(path_element + '%s' % fn) for fn in listdir(
        path_element) if fn.endswith('.png')]
    ims_size = [list(im.size) for im in ims]
    # 获取待拼接图片的最大高度 否则合成的图片高度只是第一张的高度 后续更高的图会被截掉一部分
    max_height = get_max_height(ims_size)
    # 选择拼接方式 横向或者纵向
    if flag == 'h':  # 横向
        compose_width = 0  # 合成图片的宽度 由所有需要合成的图片的宽度累加
        for i in range(len(ims_size)):
            compose_width += ims_size[i][0]
        # 创建一个多张原图合并后大小的空白图 高度为一张图的高度
        join_image = Image.new('RGB', (compose_width, max_height), color=(255, 255, 255))
        left_width = 0  # 每一张横向拼接的图距离左边的的距离 每拼一张就要加一个图片宽度
        for img in ims:
            join_image.paste(img, (left_width, 0))  # 依次将原图黏贴到指定位置
            left_width += ims_size[0][0]
        # 保存 哪个文件夹存在保存到哪个文件夹中
        if index_error:
            join_image.save(f'{path_save}\\{scene}\\{date}（异常）\\{area}\\{equipment}_{point}.png')
        else:
            join_image.save(f'{path_save}\\{scene}\\{date}\\{area}\\{equipment}_{point}.png')
        shutil.rmtree(path_element)

    elif flag == 'v':  # 纵向
        compose_height = 0  # 合成图片的高度 由所有需要合成的图片的高度累加
        for i in range(len(ims_size)):
            compose_height += ims_size[i][1]
        # 创建一个多张原图合并后大小的空白图 宽度为一张图的宽度
        join_image = Image.new('RGB', (ims_size[0][0], compose_height), color=(255, 255, 255))
        top_height = 0  # 每一张纵向拼接的图距离顶部的距离 每拼一张就要加一个图片高度
        for img in ims:
            join_image.paste(img, (0, top_height))  # 依次将原图黏贴到指定位置
            top_height += ims_size[0][1]
        # 保存 哪个文件夹存在保存到哪个文件夹中
        if index_error:
            join_image.save(f'{path_save}\\{scene}\\{date}（异常）\\{area}\\{equipment}_{point}.png')
        else:
            join_image.save(f'{path_save}\\{scene}\\{date}\\{area}\\{equipment}_{point}.png')
        shutil.rmtree(path_element)


def img_compose(equipment, area_name, point, num, flag='h'):
    """
    该方法用于拼接单个查询类型的多个日期的截图
    :param equipment:设备名称
    :param area_name: 区域名称
    :param point: 点位名称
    :param num: 用于区分相同点位的不同数据类型截图
    :param flag: 横向拼接（h）或纵向拼接(v)
    """
    # 拼图素材路径
    path_element = f'B:\ScreenShoot\拼图素材{area_name}\\'
    # 拼图保存路径
    path_save = f'B:\ScreenShoot\拼图素材{area_name}2'
    n = str(num)
    # 创建图片保存目录
    path1 = 'B:\\'
    path2 = 'ScreenShoot'
    # file_path = os.path.join(path1, path2, scene, area)
    file_path = os.path.join(path1, path2, path_save)
    index = os.path.exists(file_path)
    if not index:
        os.makedirs(file_path)
    # 获取待拼接的图片
    ims = [Image.open(path_element + '%s' % fn) for fn in listdir(
        path_element) if fn.endswith('.png')]
    ims_size = [list(im.size) for im in ims]
    # 选择拼接方式 横向或者纵向
    if flag == 'h':  # 横向
        compose_width = 0  # 合成图片的宽度 由所有需要合成的图片的宽度累加
        for i in range(len(ims_size)):
            compose_width += ims_size[i][0]
        # 创建一个多张原图合并后大小的空白图 高度为一张图的高度
        join_image = Image.new('RGB', (compose_width, ims_size[0][1]))
        left_width = 0  # 每一张横向拼接的图距离左边的的距离 每拼一张就要加一个图片宽度
        for img in ims:
            join_image.paste(img, (left_width, 0))  # 依次将原图黏贴到指定位置
            left_width += ims_size[0][0]
        # 保存
        join_image.save(f'{path_save}\\{equipment}_{point}_{n}.png')
        shutil.rmtree(path_element)

    elif flag == 'v':  # 纵向
        compose_height = 0  # 合成图片的高度 由所有需要合成的图片的高度累加
        for i in range(len(ims_size)):
            compose_height += ims_size[i][1]
        # 创建一个多张原图合并后大小的空白图 宽度为一张图的宽度
        join_image = Image.new('RGB', (ims_size[0][0], compose_height))
        top_height = 0  # 每一张纵向拼接的图距离顶部的距离 每拼一张就要加一个图片高度
        for img in ims:
            top_height += ims_size[0][1]
            join_image.paste(img, (0, compose_height - top_height))  # 依次将原图黏贴到指定位置
        # 保存
        join_image.save(f'{path_save}\\{equipment}_{point}_{n}.png')
        shutil.rmtree(path_element)


def add_border(img_url, border=1):
    """
    给图片添加边框
    :param img_url:需要添加边框的图片全路径
    :param border: 边框的宽度 若不传入宽度 则默认添加1px的边框
    """
    path_old = os.path.join(img_url)  # 原图的地址
    path_new = os.path.join(img_url)  # 保存的地址

    img = Image.open(path_old)  # 加载原图
    img_new = Image.new(mode='RGB',
                        size=(img.size[0] + border * 2, img.size[1] + border * 2),
                        color=(0, 0, 0))  # 创建一个size=(100, 80)的RGB幕布，幕布颜色由color值决定
    img_new.paste(img, (border, border))  # 贴图
    img_new.save(path_new)  # 保存新图


def add_text(img_url, text):
    """
    给图片添加文字
    :param img_url:需要添加边框的图片全路径
    :param text: 文字内容
    """
    # 设置字体以及字体大小
    font_size = 50
    font = ImageFont.truetype("B:\devSoft\\textfont\\NotoSansHans-Bold.otf", 50)
    # 打开图片
    image = Image.open(img_url)

    # 计算文字和图片的一半宽度
    img_width = image.size[0] / 2
    font_width = len(text) * font_size / 2
    draw_ = ImageDraw.Draw(image)
    # 文字填写位置使用二分一图片宽度减去二分之一文本宽度 这样文本就水平居中了
    draw_.text((img_width - font_width, 75), text, (0, 0, 0), font=font)
    # 保存图片 路径和原路径相同 可以直接覆盖原图
    image.save(img_url)


# 获取拼接图片中的最大高度
def get_max_height(ims):
    height = 0
    for im in ims:
        if im[1] > height:
            height = im[1]
    return height
