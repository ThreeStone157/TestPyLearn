# coding: utf-8
import os
import sys
sys.path.append(r'.')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import unittest
from HTMLTestRunner import HTMLTestRunner
import datetime
from common.emails import Emails
from testcase import test_excel


class UnitTestRun:
	report_name = ""
	file_path = ""

	# 创建一个测试套件
	def unittest_run(self):
		suit = unittest.TestSuite()
		load = unittest.TestLoader()

		suit.addTest(load.loadTestsFromTestCase(test_excel.TestExcels))

		times = datetime.datetime.now()
		times_str = times.strftime('%Y_%m_%d_%H_%M_%S')
		self.report_name = r"{}.html".format(times_str)

		file_path = r"..\report\{}".format(self.report_name)
		fp = open(file_path, "wb")
		runner = HTMLTestRunner(stream=fp, description="接口测试报告", title="接口测试报告")
		runner.run(suit)
		fp.close()

	def send_email(self):
		email = Emails()
		email.send_email(self.report_name)


if __name__ == "__main__":
	utr = UnitTestRun()
	utr.unittest_run()
	utr.send_email()
