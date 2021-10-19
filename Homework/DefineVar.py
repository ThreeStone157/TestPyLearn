#coding:utf-8

def variables():
    javaLearn = {"《java架构师》": 6600}
    Pythonlearn = {"《python工程师》": 4280}
    AlgorithmeLear = {"《算法入门》": 1280}
    totalMoney = 0
    # print(type(javaLearn.keys()))
    key = list(AlgorithmeLear.keys())
    print(key[0])
    # for key in javaLearn.keys():
    #     print(key)
    print("小慕在书店买了一本{},花了{}元".format(list(javaLearn.keys())[0],javaLearn.get(list(javaLearn.keys())[0])))
    print("小慕在书店又买了一本{},花了{}元".format(list(Pythonlearn.keys())[0], Pythonlearn.get(list(Pythonlearn.keys())[0])))
    print("小慕在书店再买了一本{},花了{}元".format(list(AlgorithmeLear.keys())[0], AlgorithmeLear.get(list(AlgorithmeLear.keys())[0])))
    totalMoney += javaLearn.get(list(javaLearn.keys())[0]) + Pythonlearn.get(list(Pythonlearn.keys())[0]) + AlgorithmeLear.get(list(AlgorithmeLear.keys())[0])
    print("小慕总共花了{}元".format(totalMoney))

def counts():
    str ="hello python 睡大觉大佬"
    str_count = str.count("大")
    print(str_count)
    list_1 = ["22s", "b", "cv"]
    list_count = list_1.count("b")
    print(list_count)
    dict_1 = {
        "list_1": str_count,
        "str": list_count
    }
    print(dict_1)

def switch():
    str = "this is my dog!"
    print(str.startswith("this"))
    print(str.endswith("my dog"))
    print(str.find("a"))
    print(str.index("m"))
    print(str.replace("my", "啥"))

def maxs():
    str1 = "11层大大陈sa"
    str2 = "cd"
    str = "打陈"
    print(max(str1))
    print(max(str2))
    print(max(str))

if __name__ == "__main__":
    variables()
    # counts()
    # switch()
    # maxs()