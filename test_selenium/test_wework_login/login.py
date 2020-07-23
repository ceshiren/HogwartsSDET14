from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_selenium.test_wework_login.register import Register


class Login:
    """
    登录页面的po
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def scan(self):
        """
        扫描二维码
        :return:
        """
        pass

    def goto_register(self):
        """
         点击企业注册
         进入到注册的po
         :return:
         """
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return Register(self.driver)
