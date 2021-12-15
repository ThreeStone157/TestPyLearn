#coding: utf-8

def dicts():
    dict_test1 = {"username": "dawei", "age": "24"}
    print(dict_test1)
    print(dict_test1["username"])
    dict_test1["sex"] = "男"
    print(dict_test1)
    dict_test2 = {"username": 'sss', "ss": "11"}
    dict_test1.update(dict_test2)
    print(dict_test1)
    value = dict_test1.setdefault("usernames", "111")
    print(dict_test1, value)
    list_test1 = list(dict_test1.keys())
    list_value1 = list(dict_test1.values())
    print(list_value1)
    print("-------")

    print(list_test1[3:])
    print(list_test1[2: 6])
    print(dict_test1["age"])
    lsits = dict_test1.get("sex11", "age")
    print(lsits)
    print(dict_test1)
    dict_test3 = dict_test1.copy()
    print(id(dict_test1))
    print(id(dict_test3))

def bools():
    a_1 = 1
    a_2 = 0
    a_3 = 0.0
    print(bool(a_1))
    print(bool(a_2))
    print(bool(a_3))
    print("-------")
    print(bool(not a_1))
    print(bool(not a_2))
    print("-------")
    b_1 = ''
    b_2 = " "
    print(bool(b_1))
    print(bool(b_2))
    print("-------")
    c_1 = []
    c_2 = [1]
    print(bool(c_1))
    print(bool(c_2))
    print("-------")
    d_1 = (0)
    d_2 = (1)
    print(bool(d_1))
    print(bool(d_2))
    print("-------")
    e_1 = {}
    e_2 = {"223": "23"}
    e_2.setdefault("ces ")
    print(bool(e_1))
    print(bool(e_2))
    print(e_2)
    print("-------")
    e_3 = None
    # e_2 = {"223": "23"}
    print(bool(e_3))
    # print(bool(e_2))

def test1():
    dict_test2 = {"username": 'sss', "ss": "11"}
    # s = dict_test2.pop("ss")
    # print(s)
    # ss = dict_test2.popitem()
    # print(type(ss))
    # print(ss, dict_test2)
    print("ss" not in dict_test2)

def test2():
    co = 0
    while co:
        print(co)
    # print(co)
    print(co == False)

def test3_15():
    sum1 = 0
    num1 = 1
    while num1 < 1001:
        if num1 % 2 == 1:
            sum1 += num1
        num1 += 1
    print(sum1)

def ranges():
    r2 = range(1, 10, 2)
    for r in r2:
        print(r)
    r3 = range(7, 11, 2)
    for r1 in r3:
        print(r1)
    print(r2[3: 5])
    a = [1, 3, 5, 7, 9]
    print(a[3: 5])

def lists():
    numList = range(1, 11)
    num = 0
    index = 1
    print("运行结果:")
    for nums in numList:
        if nums % 2 == 0:
            num += nums
            print("第 {:d} 个偶数 {:d}\n".format(index, nums))
            index += 1

def test4_6():
    i = 0
    while i< 10:
        i += 1
        if i == 5:
            continue
        print(i, end=",")


if __name__ == "__main__":
    dicts()
    bools()
    test1()
    test2()
    test3_15()
    ranges()
    lists()
    test4_6()
