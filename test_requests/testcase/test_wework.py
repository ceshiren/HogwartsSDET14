from test_requests.api.wework import WeWork
from test_requests.api.util import Util
import requests
class TestWework:
  def test_get(self):
    print(WeWork().test_get("qiaoqiao333"))

  def test_create(self):
    print(WeWork().test_create("kenan8888", "13800000001"))

  def test_update(self):
    print(WeWork().test_update("kenan8888", "wangwu"))

  def test_delete(self):
    print(WeWork().test_delete("kenan8888"))

  def test_session(self):
    s = requests.session()
    s.params = {"access_token": Util().get_token()}
    res = s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get?userid=kenan8888")
    print(res.json())
