# coding:utf-8
import unittest

from ddt import ddt, data

from common.checkback import CheckBack
from common.mylogging import MyLogger
from common.requestApi import RequestApi
from common.operate_excel import OperateExcel
import logging


@ddt
class TestExcels(unittest.TestCase):
    execlRW = OperateExcel(r"E:\Work\和平精英\hpjyInterface.xlsx")
    cases_data = execlRW.read_data_table()
    my_log = MyLogger()
    my_log.create_logger()

    @data(*cases_data)
    def test_excel(self, case):
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
