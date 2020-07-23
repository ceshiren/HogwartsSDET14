from selenium.webdriver.common.by import By

from test_selenium.test_wework.base_page import BasePage


class AddMember(BasePage):
    def add_member(self):
        """
        添加成员页面，实现成员添加
        :return:
        """
        self.find(By.ID, "username").send_keys("MrDong23456")
        self.find(By.ID, "memberAdd_acctid").send_keys("MrDong23456")
        self.find(By.ID, "memberAdd_phone").send_keys("11111111112")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
