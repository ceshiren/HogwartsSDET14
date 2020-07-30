from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _black_list = [
        (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")
    ]
    _max_err_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator=None):
        try:
            # 如果元素找到，就清空 error 计数
            if locator is None:
                result = self.driver.find_element(*by)
            else:
                result = self.driver.find_element(by, locator)
            self._error_num = 0
            return result
        except Exception as e:
            # 如果没找到，就进行黑名单处理
            if self._error_num > self._max_err_num:
                # 如果 erro 次数大于指定指，清空 error 次数并报异常
                self._error_num = 0
                raise e
            self._error_num += 1
            for ele in self._black_list:
                # 对黑名单进行点击
                eles = self.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(by, locator)
            raise ValueError("元素不在黑名单中")

    def finds(self, by, locator=None):
        if locator is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, locator)

    def set_implicitly_wait(self, second):
        self.driver.implicitly_wait(second)