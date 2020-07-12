#!/usr/bin/env python
# -*- coding: utf-8 -*-

# datas = [[1,2,3],[0.2,0.3,0.4]]
# myids = ['整数','浮点数']
import yaml

with open('datas/a.yml') as f:
    datas = yaml.safe_load(f)
    # myids 和mydatas 要与conftest.py 勾子函数里面的
    # metafunc.module.datas, ids=metafunc.module.myids 保持一致
    myids = datas.keys()
    mydatas = datas.values()


# param1 要与conftest.py 里面处理的param1 保持一致
def test_param(param1):
    print(f"param = {param1}")
    print("动态生成测试用例")
