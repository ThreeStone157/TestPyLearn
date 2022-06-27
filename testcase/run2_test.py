# coding: utf-8
import sys
import unittest
from HTMLTestRunner import HTMLTestRunner
from common.email import Email
from testcase import test_excel

s = sys.path
sys.path.append(s)
# 创建一个测试套件
suit = unittest.TestSuite()
load = unittest.TestLoader()

suit.addTest(load.loadTestsFromTestCase(test_excel.TestExcels))

fp = open("report.html", "wb")
runner = HTMLTestRunner(stream=fp, description="接口请求报告", title="接口自动化报告")

runner.run(suit)
fp.close()

email = Email()
email.send_email(r"report.html")
