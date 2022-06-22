from urllib import parse

import yaml


class readYaml:
    parameter = ""

    # 读取参数配置文件publicparameter,路径是相对路径，文件名称如果不传是默认读取公共参数文件。
    def __init__(self, file_path=None):
        if file_path == None:
            parameter = open(r"..\config\publicParameter", mode="r", encoding="utf-8")
        else:
            parameter = open(file_path, mode="r", encoding="utf-8")
        self.parameter = yaml.load(parameter, Loader=yaml.FullLoader)
        parameter.close()
        print(self.parameter)

    # 根据调用的参数，拼接成一个请求
    def read_request_parameter(self, path, environment=None):
        # 将字典转义为请求的字符串
        param = self.parameter["read_parameter"]
        self.urlenc = parse.urlencode(param)
        # 获取请求的域名
        if environment == None:
            domain_name = self.parameter["转测服"]
        else:
            domain_name = self.parameter[environment]
        # 将请求的域名+请求路径+请求的参数拼接
        URL = domain_name + path + "?" + self.urlenc
        return URL


if __name__ == "__main__":
    ry = readYaml()
    url = ry.read_request_parameter("/web/hpjy/getUser", "转测服")
    print(url)
