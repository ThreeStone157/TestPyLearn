#coding: utf-8

def exchange():
    num = -1
    # print(type(num))、、
    while num != 0:
        print("************欢迎使用货币转换系统****************")
        print("1.人民币转换为美元")
        print("2.美元转换为人民币")
        print("3.人民币转换为欧元")
        print("0.结束程序")
        print("请选择您需要的服务", end=":")
        num = int(input())
        print("~~~~~~~~~~~~~~~~~~~~~~")
        if num == 1:
            print("欢迎使用人民币兑换美元服务")
            print("请您输入需要转换的人民币金额", end=":")
            price = int(input())
            print("您需要转换的人民币为:{}元".format(price))
            prices = price / 7.06
            prices = round(prices, 2)
            print("兑换成美元为:{}$".format(prices))
            print("=========================")
        elif num == 2:
            print("欢迎使用美元兑换人民币服务")
            print("请您输入需要转换的美元金额", end=":")
            price = int(input())
            print("您需要转换的美元为:{}元".format(price))
            prices = price * 7.06
            prices = float('%.2f' % prices)
            print("兑换成人民币为:{}$".format(prices))
            print("=========================")
        elif num == 3:
            print("欢迎使用人民币兑换欧元服务")
            print("请您输入需要转换的人民币金额", end=":")
            price = int(input())
            print("您需要转换的人民币为:{}元".format(price))
            prices = price * 0.12
            prices = float('%.2f' % prices)
            print("兑换成欧元为:{}$".format(prices))
            print("=========================")
    print("感谢您的使用，祝您生活愉快，再见！")

def adds(a:int, b:int, *args:int, **kwargs):
    print(type(args), type(kwargs))

#deposit：本金， interestRate：利率,newAge；现在的年龄，oldAge：以后的年龄，annualIncome：预计年收入
def interest(deposit, interestRate, newAge, oldAge, annualIncome):
    print("{}的存款为{}".format(newAge, deposit))
    deposit =  deposit + deposit * interestRate + annualIncome  #(本金+利息+年存款)

    if newAge != oldAge:
        newAge += 1
        interest(deposit, interestRate, newAge, oldAge, annualIncome)

    else:
        print("{}的存款为{},年利率为{}+预计以后每年纯存款为{}时。{}的存款有{}".format(newAge, deposit, interestRate, annualIncome, oldAge, deposit))


def ranges():
    sum = 0
    for i in range(0, 5):
        sum += i
    print(sum)

def gooes(i):
    if i < 3:
        i += 1
        print("鹅鹅鹅")
        print("************")
        gooes(i)

def seq(*args):
    num = args[0][0]
    num1 = args[0][1]
    num2 = args[0][2]
    if num < 88:
        return num1 * num2
    else:
        return num1 + num2

def log(fuc):
    def wrapper():
        print("call %s():" % fuc.__name__)
        fuc()

    return wrapper

@log
def hello():
    print("hello world")
def now(aa):
    print("2018-11-27")

if __name__ == "__main__":
    exchange()
    adds(1, 2, 3, 5, name = "2233")
    interest(0, 0.04, 25, 35, 15)
    ranges()
    gooes(0)
    touple1 = (90, 2, 4)
    # seq(touple1)
    returns = seq(touple1)
    print(returns)
    rest = lambda x, y: x**2 + y**3
    print(rest(y=2, x=3))
    now("12 33")
    hello()
