# 作业
def display_message():
    """本章所学习"""
    print("学习编写函数")

def favourite_book(title):
    """打印喜欢的书"""
    print("我喜欢的书是" + title)

def make_shirt(size, sentence):
    """输入尺码和字样"""
    print("这件上衣是" + size + "\nslogan is：" + sentence)

def return_two_value(valvel, value2):
    """返回两个值"""
    return valvel, value2


# display_message()
# favourite_book("爱丽丝")
# make_shirt("large","xixi")

# x, y = return_two_value(1, "zhangsan")
# (1, 2)
# print(x)
# print(y)

def test1(*name):
    """可变参数"""
    print(name)

def test2(**name):
    """关键字参数"""
    print(name)


# test1("zhangsan", "lisi", 111)
# test2(name="zhangsan", age=18)

import time as tt
print("start")
tt.sleep(4)
print("end")

from time import sleep as sl
print("start")
sl(10)
print("end")