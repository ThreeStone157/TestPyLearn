# coding:utf-8
import unittest
from ddt import ddt, data
import os
import sys
sys.path.append(r'.')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from common.mylogging import MyLogger
from common.requestApi import RequestApi
from common.operate_excel import OperateExcel
import logging
from common.read_yaml import ReadYaml


@ddt
class TestExcels(unittest.TestCase):
    my_log = MyLogger()
    my_log.create_logger()
    ry = ReadYaml()
    read_execl = OperateExcel(ry.parameter["testcase_file_path"])
    cases_data = read_execl.read_data_table()

    @data(*cases_data)
    def test_excel(self, case):
        print(111)
        url = case["URL"]
        method = case["请求方式"]
        res_api = RequestApi()
        res = res_api.send(url, method, case["请求数据"])
        try:
            self.assertEqual(200, res.status_code)
        except AssertionError as e:
            logging.error("{}请求错误返回结果是:{}".format(url, res.text))
        finally:
            logging.info("请求正常，返回的结果是:{}".format(res.text))


if __name__ == "__main__":
    unittest.main()
