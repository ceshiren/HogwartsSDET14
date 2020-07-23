from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            chrome_options = Options()
            # 和浏览器打开的调试端口进行通信
            # 浏览器要使用 --remote-debugging-port=9222 开启调试
            chrome_options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=chrome_options)
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_for_click(self, locator):
        # 显示等待
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_condition(self, condition):
        # 满足 condition 的显示等待
        WebDriverWait(self._driver, 10).until(condition)
