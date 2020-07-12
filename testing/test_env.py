#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 测试用例通过传入 fixture方法，获取 测试数据/ 开发数据
def test_case(cmdoption):
    print("测试环境验证")
    env, datas = cmdoption
    print(f"环境 ： {env} , 数据：{datas}")
    ip = datas['env']['ip']
    port = datas['env']['port']
    url = 'http://' + str(ip) + ":" + str(port)
    # requests.get(url)
    print(url)
