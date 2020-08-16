import requests
import json
class BaseApi:
  params = {}

  def send(self, data):
    # pytest test_wework.py::TestWework::test_create
    raw_data = json.dumps(data)
    for key, value in self.params.items():
      raw_data = raw_data.replace("${"+key+"}", value)
    data = json.loads(raw_data)
    return requests.request(**data).json()