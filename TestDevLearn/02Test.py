#coding: utf-8

def hotel_Activity():
    monday = "周一"
    tuesday = "周二"
    wednesday = "周三"
    thursday = "周四"
    friday = "周五"
    saturday = "周六"
    sunday = "周日"
    data = [monday, tuesday, wednesday, thursday, friday ]
    mlxlx = "麻辣小龙虾"
    mlxlx_price = 23
    gbjd = "宫保鸡丁"
    gbjd_price = 12
    szrp = "水煮肉片"
    szrp_price = 32
    gebc = "果儿拌菜"
    grbc_price = 19
    xjdmg = "小鸡炖蘑菇"
    xjdmg_price = 33
    dishes ={mlxlx: mlxlx_price, gbjd: gbjd_price, szrp: szrp_price, gebc:grbc_price, xjdmg:xjdmg_price}
    lst = "罗宋汤"
    zcdht = "紫菜蛋花汤"
    xhnrg = "西湖牛肉羹"
    fqjdt = "番茄鸡蛋汤"
    mjxty = "米酒小汤圆"
    gift_price = 9.8
    gift_dict ={lst: gift_price,zcdht:gift_price,xhnrg:gift_price,fqjdt:gift_price,mjxty:gift_price}
    activity_introduction = "我们饭店不仅每天有特价，为了回馈新老用户到店就送价值29.9的精美礼品，凭小票可进行抽奖\n一等奖: 价值一万元欧洲游\n二等奖: 价值388的豆浆机\n三等奖: 价值288的生活大礼包"
    """
        先将时间整理为一个列表，将卖的菜品、附赠的菜品都整理为字典。
        实现正确的输出：
            1.读取列表的小标
            2.根据列表的小标每次比对卖的菜的下标，确保时间点和卖的菜一一对应（本质是循环一次查找对应下标的数据）
            3.附赠的菜品也是需要和卖的菜对应，再次循环查找对应小标的数据
            4.如果找到，直接跳出循环，用break
        
    """
    for times in data:
        indexs = data.index(times)
        # finds = data
        # print(indexs)
        num = 0
        for keys, values in dishes.items():
            if num == indexs:
                # print(keys, values)
                nums = 0
                for keyss, valuess in gift_dict.items():
                    if num == nums :
                        print("%s特价%s %d元，赠送一份价值%f的%s" % (times, keys, values, valuess, keyss))
                        break
                    else:
                        nums+=1
                break
            else:
                num+=1
    print("**************************")
    print(activity_introduction)


def VBScript():
    str = "When you mind is simple,your world is simple"
    print("定义长度为：{:s}".format(str.zfill(48)))
    print("获取元素i的个数：{:d}".format(str.count("i")))
    print("判断开头元素是不是e:%s" % str.startswith("e"))
    print("判断结尾元素是不是e:%s" % str.endswith("e"))
    print("请找到r的元素在哪个位置:%s" % str.find("r"))
    print("请找到元素a在哪个位置:%s"% str.find("a")+"  如果返回为-1代表str中没有a这个元素")
    print("请把字符串中的W去掉:%s" % str.replace("W", ""))
    print("请把字符串中的your改为my:%s" % str.replace("your", "my"))
    print("请判断字符是由空格组成：{:d}".format(str.isspace()))
    print("请判断字符串是否是标题:%s" % (str.istitle()))
    print("请判断字符串的字母是否都是大写:%s" % (str.isupper()))
    print("请判断字符串的字母是否都是小写:%s" % (str.islower()))









if __name__ == "__main__":
    # hotel_Activity()
    VBScript()