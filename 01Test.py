#coding: utf-8
import sys


def Test():
    print(sys.version)
    print(3//2)#1
    print(3/2)#1.5
    print("test git")

def test2():
    name ="jack"
    age = 17
    if age > 18:
        print("我已经成年了，", end = "")
    else:
        print("还未成年，", end = "")
    print("我叫{}".format(name))
    if 5-8:
        print(True)
    else:
        print(False)

def test3():
    height = float(input("请输入身高："))
    weight = float(input("请输入体重："))
    print("身高为：{}".format(height))
    print("体重为：{}".format(weight))
    BMI = weight / (height ** 2)
    print("BMI={}".format(BMI))
    if BMI < 18.5:
        print("过轻")
    elif 18.5 <= BMI <= 25:
        print("正常")
    elif 25 < BMI <= 28:
        print("过重")
    elif 28 < BMI <= 32:
        print("肥胖")
    else:
        print("严重肥胖")

def fortest():
    for i in range(9):
        for j in range(8):
            print("内循环：", i)
            print("外循环：", j)



if __name__=="__main__":
    # Test()
    # test2()
    # test3()
    fortest()