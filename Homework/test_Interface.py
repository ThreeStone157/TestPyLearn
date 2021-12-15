#=Coding: utf-8
class shortInputException(Exception):
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast

class Interest():
    age = 0
    deposit = 0
    def __init__(self, age, deposit):
        self.age = age
        self.deposit = deposit

    def Deposit(self, rate):
        return self.deposit + self.deposit * rate
    #存款 利率 年龄 年收入
    def Deposit(self, deposit, rate, ages, annual_income):
        self.deposit = deposit + deposit * rate + annual_income
        self.age += 1
        if ages >= self.age:
            return self.Deposit(self.deposit, rate, ages, annual_income)
        else:
            return self.deposit
    def test(self):
        assert isinstance(1, str), "参数错误"
        print("测试成功")
        return 0
    def test2(self):
        try:
            number = 23 * 0
        except Exception as e:
            print(e)
        finally:
            print("执行")
    def test3(self):
        try:
            test = "abc"
            if len(test) < 5:
                raise  shortInputException(len(test), 5)
        except shortInputException as result:
            print("shortInputException:输入的长度为{},"
                  "长度至少应该是{}".format(result.length, result.atleast))
        else:
            print("没有异常的发生")
        finally:
            print("输入的字符串是{}".format(test))



if __name__ == "__main__":
    interests = Interest(25, 0)
    # interests.Deposit(23, 0.04, 30, 16)
    # print("存款为:{}".format(interests.deposit))
    deposit = interests.Deposit(interests.deposit, 0.04, 35, 20)
    print("35岁存款为:{}".format(interests.deposit))
    # interests.test()
    # interests.test3()

