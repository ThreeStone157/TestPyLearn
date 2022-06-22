# coding:utf-8
import unittest

from ddt import ddt, data

from common.Mylogging import MyLogger
from common.RequestApi import RequetsApi
from common.OperateExcel import operate_excel
import logging


@ddt
class testExcels(unittest.TestCase):
    execlRW = operate_excel("F:\工作文件\hpjyInterface.xlsx")
    cases_data = execlRW.read_datas()
    mylog = MyLogger()
    mylog.create_logger()

    @data(*cases_data)
    def test_excel(self, case):
        print(case)
        url = case["URL"]
        method = case["请求方式"]
        resApi = RequetsApi()
        res = resApi.send(url, method)
        try:
            print(res.status_code)
            self.assertEqual(200, res.status_code)
        except AssertionError as e:
            # print(e)
            logging.error("{}请求错误返回结果是:{}".format(url, res.text))
        finally:
            logging.info("请求正常，返回的结果是:{}".format(res.text))


if __name__ == "__main__":
    unittest.main()
