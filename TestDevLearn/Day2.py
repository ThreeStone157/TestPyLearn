#coding: utf-8
import formatter

def functions():
    str = "  "
    str1 = "Hello Pyhtons "
    print(str.isspace())
    print(str1.isspace())
    print(str1.istitle())
    print(str1.isupper())
    print(str.islower())

    str2 = "活动数据发了"
    print(str2)

def symbol():
    print("%c" % 1000)
    print("%d" % 333.6)
    print("%f" % 234.78)
    print("%u" % -232)
    str = "  tomorrow is sunny day is  -  "
    print(str.find("is",9))
    res = str.find("is", 13)
    print(res)
    print(str.capitalize())
    print(str.casefold())
    print(str.strip(" "))
    print(str.replace("is", "23"))
    print("我叫{0}".format("小明"))
    print("我叫{0}, 今年{1}岁".format("小明", 18))


if __name__ == "__main__":
    # functions()
    symbol()