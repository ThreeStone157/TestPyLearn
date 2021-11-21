#coding: utf-8
import json

import requests

"""
请求方法的封装，暂时先封装get、post请求方法
"""

class RequetsApi:
    #请求post方法
    def post_method(self, url, data=None, header=None):
        if header is not None:
            res = requests.post(url, data=json.dumps(data), headers=header)
        else:
            res = requests.post(url, data=json.dumps(data))
        if str(res) =="<Response [200]>":
            return res.json()
        else:
            return res.text

    # 请求get方法
    def get_method(self, url, data=None, header=None):
        if header is not None:
            res = requests.get(url, data=json.dumps(data), headers=header)
        else:
            res = requests.get(url, data=json.dumps(data))
        if str(res) =="<Response [200]>":
            return res.json()
        else:
            return res.text
    #提供给调用的方法
    def send(self, url, method, data=None, header=None):
        method = method.upper()
        if method == "POST":
            return self.post_method(url, data, header)
        elif method == "GET":
            return self.get_method(url, data, header)
        else:
            print("请求方式错误！！！")


