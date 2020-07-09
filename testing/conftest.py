#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest


# session 整个项目只执行一次， module 每个模块 也就是每个.py文件 ，只执行一次
# 模块是每一个py运行一次，但是session是整个python执行一次
@pytest.fixture()
def login(request):
    print("登录方法")
    print(request.param)
    # yield 激活fixture teardown方法
    yield ['username', 'passworld']
    print('teardown')
