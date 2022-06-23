#coding:utf-8
import logging
from datetime import datetime
import time


class Student():
	count = 0

	def __init__(self, name):
		self.name = name
		Student.count +=1
	def get_name(self):
		return self.name

	def exce(self):
		try:
			r = 10 /0
			print("1111")
		# except TypeError as es:
		# 	logging.exception(es)
		except ZeroDivisionError as e:
			print("except:", e)
			# logging.exception(e)
		finally:
			print("finally.....")
		print("end")

	def datetimes(self):
		now = datetime.now()
		print(now,type(now))
		data_str = now.strftime("%Y-%m-%d")
		data_strs = now.strftime("%Y-%m-%d %H:%M:%S")
		data_strss = now.strftime("%Y/%m/%d %H:%M:%S")
		data_obj = datetime.strptime(data_strs, "%Y-%m-%d %H:%M:%S")
		print(data_str)
		print(data_strss)
		print(data_obj)
		sjc = time.localtime()
		print(sjc)
		#获取时间戳
		sjcs = time.time()
		print(sjcs, type(sjcs))
		sjcs_obj = time.localtime(sjcs)
		print(sjcs_obj, type(sjcs_obj))
		time.sleep(100)
		before_sjcs = sjcs - 10000
		before_sjcs_obj = time.localtime(before_sjcs)
		print(before_sjcs_obj)

if __name__ =="__main__":
	Students1 = Student("zs")
	# print(Students1.count)
	# Students2= Student("zs")
	# print(Students2.count)
	# Students1.exce()
	# defi.variables()
	Students1.datetimes()




# 1660611700