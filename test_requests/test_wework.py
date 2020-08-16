import json
import random
import re

import pytest
import requests


def test_create_data():
    "userid, name, mobile"
    data = [("kenan" + str(x),
             "kenan",
             "138%08d" % x) for x in range(20)]
    return data


class TestWework:
    @pytest.fixture(scope="session")
    def token(self):
        request_params = {
            "corpid": "wwe653983e4c732493",
            "corpsecret": "T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"
        }
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params=request_params)
        return r.json()['access_token']

    def get_token(self):
        """
        获取 token
        https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        """

        request_params = {
            "corpid": "wwe653983e4c732493",
            "corpsecret": "T72_Vgw9TaNS-FLDU2gJlw6AteerMXsuMval9kGNZbc"
        }
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params=request_params)
        return r.json()['access_token']

    def test_create(self, token, userid, mobile, name="柯南", department=None):
        """
        创建成员
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        if department is None:
            department = [1]
        request_body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department}
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
                          json=request_body)
        return r.json()

    def test_get(self, token, userid):
        """
        获取成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}")
        return r.json()

    def test_update(self, token, userid, name="柯南"):
        """
        更新成员信息
        https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {
            "userid": userid,
            "name": name
        }

        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
                          json=request_body)
        return r.json()

    def test_delete(self, token, userid):
        """
        删除成员
        https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        r = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")
        return r.json()

    @pytest.mark.parametrize("userid, name, mobile", test_create_data())
    def test_wework(self, token, userid, name, mobile):
        """
        整体测试
        :return:
        """
        try:
            assert "created" == self.test_create(token, userid, mobile, name)["errmsg"]
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                re_userid = re.findall(":(.*)'$", e.__str__())[0]
                self.test_delete(token, re_userid)
                assert "created" == self.test_create(token, userid, mobile, name)["errmsg"]
        assert name == self.test_get(token, userid)["name"]
        assert "updated" == self.test_update(token, userid, name="柯南5555")["errmsg"]
        assert "柯南5555" == self.test_get(token, userid)["name"]
        assert "deleted" == self.test_delete(token, userid)["errmsg"]
        assert 60111 == self.test_get(token, userid)["errcode"]
