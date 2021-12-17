#Coding: utf-8
import os
import re
import yaml


class reade_yaml:

    file_path_yal =""
    def __init__(self, fileName):
        file_path = os.getcwd()
        file_path_yaml = os.path.abspath(os.path.join(file_path, ".."))
        print(file_path_yaml)
        self.file_path_yal = file_path_yaml + "\config\\"+fileName

    def read_data(self):
        with open(self.file_path_yal, encoding='utf-8')as file:
            content = file.read()
            print(type(content))
        print("\n*****转换yaml数据为字典或列表*****")
        # 设置Loader=yaml.FullLoader忽略YAMLLoadWarning警告
        data = yaml.load(content, Loader=yaml.FullLoader)

        print(data.keys())
        params = re.split(":| ", data["IOS"])
        print(params)


if __name__ == "__main__":
    yaml = reade_yaml("parameter.yml")
    yaml.read_data()
