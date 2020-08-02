import yaml
from selenium.webdriver.common.by import By

from xueqiu_app.page.base_page import BasePage
from xueqiu_app.page.search import Search


class Market(BasePage):
    def goto_search(self):
        #self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        self.steps("../page/market.yaml")
        return Search(self.driver)