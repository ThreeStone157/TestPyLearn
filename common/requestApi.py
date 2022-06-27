# coding: utf-8
import json

import requests

from common.read_yaml import ReadYaml

"""
请求方法的封装，暂时先封装get、post请求方法
"""


class RequestApi:
    def __init__(self):
        self.ry = ReadYaml()

    @staticmethod
    def post_method(url, data=None, header=None):
        if header is not None:
            response = requests.post(url, data=json.dumps(data), headers=header)
        else:
            response = requests.post(url, data=json.dumps(data))
        return response

    @staticmethod
    def get_method(url, data=None, header=None):
        if header is not None:
            response = requests.get(url, data=json.dumps(data), headers=header)
        else:
            response = requests.get(url, data=json.dumps(data))
        return response

    # 提供给调用的方法
    def send(self, url, method="post", data=None, header=None):
        method = method.upper()
        url = self.ry.read_request_parameter(url, "现网")
        # url = "https://hpjy-op.tga.qq.com:443" + url
        if method == "POST":
            return self.post_method(url, data, header)
        elif method == "GET":
            return self.get_method(url, data, header)
        else:
            print("请求方式错误！！！")


if __name__ == "__main__":
    resApi = RequestApi()
    res = resApi.send("/app/hpjy/getHpjyCfg", "post")
    print(res)
