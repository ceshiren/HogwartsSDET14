#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

import pytest

# session 整个项目只执行一次， module 每个模块 也就是每个.py文件 ，只执行一次
# 模块是每一个py运行一次，但是session是整个python执行一次
import yaml


@pytest.fixture()
def login():
    print("登录方法")
    # print(request.param)
    # yield 激活fixture teardown方法
    yield ['username', 'passworld']
    print('teardown')


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    print(len(items))
    # 倒序执行 items里面的测试用例
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)

        if 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)


# 命令行去添加一个参数
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )
    mygroup.addoption("--env1",  # 注册一个命令行选项
                      default='test',
                      dest='env1',
                      help='set your run env'
                      )


# 处理命令行传来的参数，设置成fixture，将 test 环境和dev环境或者其它环境
# 分别处理，获取想要的不同环境下的测试数据。
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        datapath = 'datas/test/data.yml'

    if myenv == 'dev':
        datapath = 'datas/dev/data.yml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas


# 通过 方法动态的生成测试用例
def pytest_generate_tests(metafunc: "Metafunc") -> None:
    if "param1" in metafunc.fixturenames:
        metafunc.parametrize("param1",
                             metafunc.module.mydatas,
                             ids=metafunc.module.myids,
                             scope='function')
