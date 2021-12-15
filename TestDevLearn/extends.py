#coding: utf-8

class parent():
    name = "爸爸"
    age = ""
    def __init__(self, age):
        self.age = age
        print("爸爸今年{}岁了".format(self.age))

    def sf(self):
        print("我是{},今年{}岁了".format(self.name, self.age))

class children1(parent):
    name = "儿子1号"
    def sf1(self):
        print("我是{}".format(self.name))



if __name__ == "__main__":
    children11 = children1(11)
    children11.sf()