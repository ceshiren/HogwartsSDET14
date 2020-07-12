#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
#
#
# @pytest.mark.dependency()
# @pytest.mark.xfail(reason="deliberate fail")
# def test_a():
#
#     assert False
#
# @pytest.mark.dependency()
# def test_b():
#     pass
#
# # 如果 test_a用例成功， test_c会被执行，
# # 如果 test_a 用例失败， test_c 会被跳过，不被执行
# # depends=[]  列表里面加入依赖的测试用例名称
# @pytest.mark.dependency(depends=["test_a"])
# def test_c():
#     pass
#
# @pytest.mark.dependency(depends=["test_b"])
# def test_d():
#     pass
#
# @pytest.mark.dependency(depends=["test_b", "test_c"])
# def test_e():
#     pass
