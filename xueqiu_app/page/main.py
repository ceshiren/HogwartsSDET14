import yaml
from selenium.webdriver.common.by import By

from xueqiu_app.page.base_page import BasePage
from xueqiu_app.page.market import Market


class Main(BasePage):

    def goto_market(self):
        # 伪造黑名单
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        # self.set_implicitly_wait(3)
        self.steps("../page/main.yaml")
        return Market(self.driver)
