import sys
import os
import time

import allure
import pytest
from test_generate_report import env
import utils.TestTool as tool
import pageModule.ch.ch_cases as case

path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)

if env == 'ot':
    cases_url = 'https://ot-www.sucheon.com/application.html'
else:
    cases_url = 'https://www.sucheon.com/application.html'


class TestCases(object):

    def setup_class(self) -> None:
        self.driver = tool.get_driver()
        self.case = case.Cases(self.driver)
        self.driver.get(cases_url)
        self.driver.maximize_window()

    def teardown_class(self):
        print('"====有异常抛出也会结束进程关掉driver====')
        self.driver.quit()
