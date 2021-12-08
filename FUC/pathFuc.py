#coding: utf-8

import os

class pathFuc:
	# current_paths = ""
	#查询当前路径
	def current_path(self):
		return os.getcwd()

	#查询路径下所有的文件、文件夹
	def listdirs(self, path):
		return os.listdir(path)
	#根据路径，创建文件夹
	def makedirss(self, path):
		os.makedirs(path)



if __name__ == "__main__":
	pathFucs = pathFuc()
	print(pathFucs.current_path())
	print(pathFucs.listdirs(pathFucs.current_path()))
	# print(pathFucs.makedirss("t"))
	# os.removedirs("t")
	# os.rename("t", "tt")
	# os.rmdir("t")
	print(os.path.split(pathFucs.current_path())[0])

	#17版本：https://test-web.tga.qq.com/permanent_hpjy/hpjy_personal/personal?tga_url=1
	#体验服链接：https://gray-web.tga.qq.com/tiyan/permanent_hpjy/hpjy_personal/personal?isprod=4&tga_url=1
