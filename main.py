import os
import sys

path = os.path.dirname(__file__)
sys.path.append(path)
# sys.path.append('E:/dev_project/official_web_autotesting-master')
print(f'已经把path：{path}添加到sys.path了')
# 获取项目根路径
BASS_DIR = os.getcwd()
# 测报报告存放的根路径
ALLURE_DIR = os.path.join(BASS_DIR, 'allure-report')
# 当前历史报告文件夹序号
Build_Order = 1


# 首先根据history.json文件中的buildOder字段判断该创建哪一个版本的历史文件夹
# 如果没有json文件 那么就先创建json文件并且创建报告文件夹名为1
def get_order():
    global Build_Order
    if os.path.exists(ALLURE_DIR):
        print('文件夹存在！！！！！')
    else:
        os.mkdir(ALLURE_DIR)
    f_dir = os.path.join(ALLURE_DIR, 'report-history.json')
    if os.path.exists(f_dir):
        with open(f_dir, mode='r') as f:
            res = f.read()
            # 若json文件存在 那么下一个BuildOrder就是当前的+1
            Build_Order = eval(res)[0]['buildOrder'] + 1
            print(Build_Order)
    else:
        with open(f_dir, mode='w') as f:
            data = """[{"buildOrder": 1,"reportUr": "","data": ""}]"""
            f.write(data)


if __name__ == '__main__':
    # 首先调用get_order获取这次测试用例报告的文件夹序列
    get_order()
    # 然后运行测试用例
    test_commend = 'pytest -vs .\\run_case\ch\ --alluredir ./temp'
    os.system(test_commend)

    # 然后运行用例 将报告创建在新文件夹下
    if not os.path.exists(os.path.join(BASS_DIR, 'temp')):
        os.mkdir(os.path.join(BASS_DIR, 'temp'))
    generate_commend = f'allure generate ./temp -o ./allure-report/{Build_Order}'
    os.system(generate_commend)

    # 将此次测试报告中的历史存入history-trend.json中
    his_dir = os.path.join(ALLURE_DIR, str(Build_Order) + '\widgets\history-trend.json')
    report_his = os.path.join(ALLURE_DIR, 'report-history.json')

    # 先打开当前测试报告的结果
    with open(his_dir, mode='r+') as f2:
        res = f2.read()
        res = eval(res)
        h1_data = res[0]["data"]
        # 保存为json需要双引号
        print(str(h1_data).replace("'", '"'))

    # 当前测试报告结果保存到测试报告历史文件中
        with open(report_his, mode='r+') as f1:
            h = eval(f1.read())
            if Build_Order == 1:
                h[0]['data'] = h1_data
            else:
                data = {"buildOrder": Build_Order, "reportUr": "", "data": h1_data}
                h.append(data)
            print(str(h).replace("'", '"'))
            # 对数据进行排序 根据buildOrder字段降序
            h.sort(key=lambda x: x['buildOrder'], reverse=True)
            # 将指针放在最前面 然后覆盖写入
            f1.seek(0)
            # 保存为json需要双引号
            f1.write(str(h).replace("'", '"'))
            # 同时保存一份到此次测试结果的历史文件中
            f2.seek(0)
            f2.write(str(h).replace("'", '"'))



