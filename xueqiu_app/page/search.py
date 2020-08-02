import yaml
from selenium.webdriver.common.by import By

from xueqiu_app.page.base_page import BasePage


class Search(BasePage):
    def search(self, stock_name):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("阿里巴巴")
        # self.find(By.XPATH, "//*[@text='阿里巴巴-SW' and @resource-id='com.xueqiu.android:id/name']").click()
        # self.find(By.XPATH,
        #f"//*[contains(@resource-id, 'stock_item_container')]//*[@text='{stock_name}']/../..//*[@text='加自选']").click()
        self.steps("../page/search1.yaml")

    def is_choose(self, stock_name):
        # eles = self.finds(By.XPATH,
        #                   f"//*[contains(@resource-id, 'stock_item_container')]//*[@text='{stock_name}']/../..//*[@text='已添加']")
        # return len(eles) > 0
        return self.steps("../page/search2.yaml")
