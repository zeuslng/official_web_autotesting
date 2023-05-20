import argparse
import os
import sys
import pytest

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)
env = 'online'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--env", type=str, required=False, help="测试环境，ot或者线上")
    parser.add_argument("-t", "--thread", type=str, required=False, help="进程数")
    args = parser.parse_args()
    env = args.env or 'online'
    thread_num = args.thread or 2
    # 使用pytest执行用例，并获取allure执行结果
    pytest.main(['--dist=loadscope', '--alluredir', './allure-results', '-s', '-n', f'{thread_num}'])
    # 使用命令生成测试报告 注:在终端中使用命令时要cd 进入当前文件夹之前命令 否则文件夹的相对路径会错误
    # os.system('allure generate --clean')
