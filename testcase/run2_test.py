import unittest
from HTMLTestRunner import HTMLTestRunner
from common.Email import Email
from testcase import test_Excel
#创建一个测试套件
suit = unittest.TestSuite()
load = unittest.TestLoader()

suit.addTest(load.loadTestsFromTestCase(test_Excel.testExcels))

fp = open("report.html", "wb")
runner = HTMLTestRunner(stream=fp,
                        description="接口请求报告",
                        title="接口自动化报告")

runner.run(suit)
fp.close()

email = Email()
email.send_email(r"F:\code\TestDevLearn\testcase\report.html")
