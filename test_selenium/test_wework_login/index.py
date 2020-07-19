from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from test_selenium.test_wework_login.login import Login
from test_selenium.test_wework_login.register import Register


class Index:
    """
    首页面 po
    """

    def __init__(self):
        chrome_options = Options()
        # 和浏览器打开的调试端口进行通信
        # 浏览器要使用 --remote-debugging-port=9222 开启调试
        # chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_register(self):
        """
        点击立即注册
        进入到注册的po
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        return Register(self.driver)

    def goto_login(self):
        """
        点击企业登录
        进入到企业登录po
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        return Login(self.driver)

