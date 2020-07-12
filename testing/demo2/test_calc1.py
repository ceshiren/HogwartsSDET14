#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 测试文件
import sys

import pytest

print(sys.path.append('../..'))
from pythoncode.calc import Calculator


# 模块级别
# def setup_module():
#     print("模块级别setup")
#
#
# def teardown_module():
#     print("模块级别teardown")


# 函数级别 类外面的使用def 定义的叫做函数，
# 在类里面使用def 定义的叫方法
# def setup_function():
#     print("函数级别 setup")
#
#
# def teardown_function():
#     print("函数级别 teardown")


def test_case1():
    print("testcase1")


class TestCalc:
    # setup_class， teardown_class每个类里面 执行前后分别 执行
    def setup_class(self):
        self.cal = Calculator()
        print("类级别 setup")

    def teardown_class(self):
        print("类级别 teardown")

    # 函数级别 每条类里面的测试用例前和后分别 执行setup teardown
    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    @pytest.mark.parametrize('a, b, result', [
        (1, 1, 3),
        (2, 2, 4),
        (100, 100, 200),
        (0.1, 0.1, 0.2),
        (-1, -1, -2)
    ]
        , ids=['int', 'int', 'bignum', 'float', 'fushu'])
    # @pytest.mark.add
    def test_add(self, a, b, result):
        # cal = Calculator()
        assert result == self.cal.add(a, b)
        assert result == self.cal.add(a, b)
        assert result == self.cal.add(a, b)

    # @pytest.mark.add
    def test_add1(self):
        # cal = Calculator()
        assert 3 == self.cal.add(1, 2)

    # @pytest.mark.div
    def test_div(self):
        # cal = Calculator()
        print("登录操作111")
        assert 1 == self.cal.div(2, 1)
        print("登录操作222")
        assert 1 == self.cal.div(2, 1)
        print("登录操作333")
        assert 1 == self.cal.div(2, 1)

    def test_assume(self):
        print("登录操作")
        pytest.assume(1 == 2)
        print("搜索操作")
        pytest.assume(2 == 2)
        print("加购操作")
        pytest.assume(3 == 2)
