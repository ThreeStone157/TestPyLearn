#Coding:utf-8

import unittest
from HTMLTestRunner import HTMLTestRunner

from common.Email import Email
from testcase import test_Excel

suit = unittest.TestSuite()
load = unittest.TestLoader()

suit.addTest(load.loadTestsFromTestCase(test_Excel.testExcels))

runner = HTMLTestRunner(stream=open("report.html", "wb"),
                        description="进房接口请求报告",
                        title="和平接口自动化报告")

runner.run(suit)
email = Email()
email.send_email(r"F:\code\TestDevLearn\testcase\report.html")
