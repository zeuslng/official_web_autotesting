

def get_account_password(scene_name, area_name=None):
    """
    输入场景名称获取用户名和密码，
    :param scene_name: 场景用户名
    :param area_name: 场景密码
    :return: username:场景用户名
             password：场景密码
             area_btn_num:场景区域的节点数
    """
    area_btn_num = 0  # 区域的div节点
    username = ''  # 场景用户名
    password = ''  # 场景密码
    area_btn_num = ''  # 区域节点
    if scene_name == '厦门烟草':
        username = 'xiamenyc'
        password = 'xiamenyc'
        if area_name is None:
            return username, password, area_btn_num
        elif area_name == '一区制丝':
            area_btn_num = 1
        elif area_name == '一区动力':
            area_btn_num = 2
        elif area_name == '二区制丝':
            area_btn_num = 3
        elif area_name == '二区卷包':
            area_btn_num = 4
        else:
            print(scene_name + '场景中没有名为‘' + area_name + '’的区域！,请确认输入内容。')
            return None
    elif scene_name == '龙岩烟草':
        username = 'lyyc001'
        password = 'Lyyc001'
        if area_name is None:
            return username, password, area_btn_num
        elif area_name == '二区卷包':
            area_btn_num = 1
        else:
            print(scene_name + '场景中没有名为‘' + area_name + '’的区域！,请确认输入内容。')
            return None
    elif scene_name == '广州宝洁':
        username = 'pggz'
        password = 'pggz'
        if area_name is None:
            return username, password, area_btn_num
        elif area_name == '帮宝适生产车间':
            area_btn_num = 1
        else:
            print(scene_name + '场景中没有名为‘' + area_name + '’的区域！,请确认输入内容。')
    elif scene_name == '成都宝洁':
        username = 'pgcd'
        password = 'Pgcd007'
        if area_name is None:
            return username, password, area_btn_num
        elif area_name == '5楼':
            area_btn_num = 1
        elif area_name == '1楼泵机房子':
            area_btn_num = 2
        else:
            print(scene_name + '场景中没有名为‘' + area_name + '’的区域！,请确认输入内容。')
    elif scene_name == '天津宝洁':
        username = 'pgtj'
        password = 'pgtj'
        if area_name is None:
            return username, password, area_btn_num
        elif area_name == '包装车间':
            area_btn_num = 1
        else:
            print(scene_name + '场景中没有名为‘' + area_name + '’的区域！,请确认输入内容。')
    else:
        print('没有找到名为’' + scene_name + '‘的场景，请确认输入内容！')

    return username, password, area_btn_num
