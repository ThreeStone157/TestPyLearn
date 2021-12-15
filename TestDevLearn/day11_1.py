#coding:utf-8
import os
import  functools
import time
from sqlalchemy import func


class advanced_features:
    def files(self):
        file_list = [d for d in os.listdir(".")]
        print(file_list)
    def dicts(self):
        d = {"x": "a", "y": "b", "z": "c"}
        for k, v in d.items():
            print(k+":"+v)
    #如果略表里面有None，这个是没有lower方法的，会报错
    def lists(self):
        L = ["XXX", "XYQzz", "sa132WE", "2233", None]
        print()
        list_lower = [s.lower() for s in L if isinstance(s, str) == True]
        # list_upper = [s.upper() for s in L]
        print(list_lower)
        # print(list_upper)
    #嵌套循环里面不能有else: for 后面的if是筛选条件，不能带else: 不然如何筛选
    def ifelse(self):
        print([x if x%2 == 0 else -x for x in range(1,11)])
        print([x for x in range(1, 11) if x % 2 == 0 ])

    def generators(self):
        L = (x*x for x in range(1, 11))
        for i in L:
            print(i)

    def log(func):
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            # print(func(*args, **kw))
            return func(*args, **kw)
        return wrapper

    @log
    def now(self):
        print("111")

    def logs(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return  func(*args, **kw)
            return wrapper
        return  decorator

    def logss(self, func):
       @functools.wraps(func)
       def wrapper(*args, **kw):
           print('call %s():' % func.__name__)
           # print('%s %s():' % (text, func.__name__))
           return func(*args, **kw)
       return wrapper

    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            t1 = time.time()
            res = fn(*args, **kw)
            t2 = time.time()
            print('%s executed in %s ms' % (fn.__name__, t2 - t1))
            return res
        return wrapper


    @metric
    def nows(self):
        time.sleep(0.1)
        print("111")



if __name__ == "__main__":
    advanced_featuress = advanced_features()
    advanced_featuress.files()
    advanced_featuress.dicts()
    advanced_featuress.lists()
    advanced_featuress.ifelse()
    advanced_featuress.generators()
    # advanced_featuress.nows()

