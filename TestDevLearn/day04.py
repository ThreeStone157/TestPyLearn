#coding: utf-8

class Person():
    name = ""
    age = ""
    sex = ""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("这个是{}性".format(self.sex))

    def data(self):
        print("我叫{}，今年{}岁了".format(self.name, self.age))

class Vehicle():
    trans_type = "SUV"
    speed = 0
    size = ()
    def __init__(self, trans_type, speed, *size):
        self.trans_type = trans_type
        self.speed = speed
        self.size = size


    def show_info(self):
        print("我的所属类型为：{},速度：{}，体积{}".format(self.trans_type, self.speed, self.size))

    def move(self):
        print("我向前移动了50米")

    def set_speed(self, newspeed):
        self.speed = newspeed

    def get_speed(self):
        print("我的时速为{}km/h".format(self.speed))

    def speed_up(self):
        self.speed = int(self.speed) + 10
        print("我的速度由{}km/h提升到了{}km/h".format(self.speed-10, self.speed))
    def speed_down(self):
        self.speed -= 15
        print("我的速度由{}km/h下降到了{}km/h".format(self.speed + 15, self.speed))
    def transport_identify(self):
        if self.trans_type == "SUV":
            print("类型匹配")
        else:
            print("类型不匹配")

if __name__ == "__main__":
    # p = Person("张三", "18")
    # p.sex = "男"
    # p.work() 
    # p.data()
    tool1 = Vehicle("SUV", "20", (4, 2,1.5))
    tool1.show_info()
    tool1.move()
    tool1.set_speed(40)
    tool1.get_speed()
    tool1.speed_up()
    tool1.speed_down()
    tool1.transport_identify()
