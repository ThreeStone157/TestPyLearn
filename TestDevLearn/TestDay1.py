#coding:utf-8
import copy


a = [[1,2,3],[4,5,6]]
b = a
c = copy.copy(a)
a.append(7)
a[1][2] = 10
print(b)
print(c)

info = {"name": "张三", "age": 12}
print(info)
print("name" in info)
print("张三" in info)
print(10%3)
print(10**2)
print(10//3)
print(info.get("name")*2)
name="李四"
listTest=[1,2,3]
print(name*3)
print(name)
print(listTest*2)

def compare():
    a =1
