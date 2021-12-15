#coding: utf-8
import os

class Test1:
    #有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
    def combination(self):
        num = 0
        for i in range(1, 5):
            for j in range(1, 5):
                for z in range(1, 5):
                    if(i != j) and (i!= z) and (j !=z):
                        print(i,j,z)
                        num += 1
        print("有%s个无重复的三位数！"% num)

    def commission(self):
        profit = [1000000,600000, 400000, 200000,100000, 0]
        rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
        i = int(input("当月净利润为:"))
        com = 0
        for idx in range(0, 6):
            if i > profit[idx]:
                com += (i- profit[idx]) * rate[idx]
                i = profit[idx]
        print(com)


if __name__ == "__main__":
    test1 = Test1()
    test1.combination()
    test1.commission()