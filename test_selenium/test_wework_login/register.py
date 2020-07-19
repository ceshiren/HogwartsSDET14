from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Register:
    """
    注册页面的po
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        """
        输入内容
        点击下拉框
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, "#corp_name").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.CSS_SELECTOR, "#manager_name").send_keys("MrDong")
        return True
