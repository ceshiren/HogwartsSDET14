#!/usr/bin/env python
# -*- coding: utf-8 -*-


# # yield 生成器
# def fun():
#     for i in range(3):
#         print(f"i = {i}")
#         yield # return  同时相当于暂停并且记住 上一次的执行位置
#         print('end')
#
# f = fun()
# next(f)
# next(f)
# next(f)
#
#


def a():
    print("a")
    return "returndatas"


print(a())
