import requests
class Util:
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