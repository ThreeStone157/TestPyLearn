#coding: utf-8

import unittest

#类开头必须是test，继承才可以识别为用例类
class TestDemo(unittest.TestCase):
    #所有方法执行前会调用setUp
    def setUp(self):
        pass

    #所有方法执行完成之后，执行tearDown
    def tearDown(self):
        pass

