import requests
from test_requests.api.util import Util
from test_requests.api.baseapi import BaseApi
import yaml
class WeWork(BaseApi):
  def __init__(self):
    self.token = Util().get_token()
    self.params["token"] = self.token
    with open("../api/wework.yaml", encoding="utf-8") as f:
        self.data = yaml.load(f)
  def test_create(self, userid, mobile, name="柯南", department=None):
      """
      创建成员
      https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
      :return:
      """
      if department is None:
          department = "1"
      # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
      #                  json=request_body)
      # data = {
      #   "method": "post",
      #   "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
      #   "json": {
      #       "userid": userid,
      #       "name": name,
      #       "mobile": mobile,
      #       "department": department}
      # }
      self.params["userid"] = userid
      self.params["mobile"] = mobile
      self.params["name"] = name
      self.params["department"] = department
      return self.send(self.data["create"])

  def test_get(self, userid):
      """
      获取成员信息
      https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
      :return:
      """
      #r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}")
      # data = {
      #   "method": "get",
      #   "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
      # }
      self.params["userid"] = userid
      return self.send(self.data["get"])

  def test_update(self,userid, name="柯南"):
      """
      更新成员信息
      https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
      :return:
      """
      # request_body = {
      #     "userid": userid,
      #     "name": name
      # }

      # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
      #                   json=request_body)
      # data = {
      #   "method": "post",
      #   "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
      #   "json":{
      #     "userid": userid,
      #     "name": name
      # } 
      self.params["name"] = name
      self.params["userid"] = userid
      return self.send(self.data["update"])

  def test_delete(self, userid):
      """
      删除成员
      https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
      :return:
      """
      # r = requests.get(
      #     f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}")
      # data = {
      #   "method": "get",
      #   "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
      # }

      self.params["userid"] = userid
      return self.send(self.data["delete"])