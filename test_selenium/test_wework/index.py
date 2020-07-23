from selenium.webdriver.common.by import By

from test_selenium.test_wework.add_member import AddMember
from test_selenium.test_wework.base_page import BasePage


class Index(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        """
        添加成员
        :return:
        """

        def add_member_condition(x):
            """
            改写显示等待条件
            :param x:
            :return:
            """
            elements_len = len(self.finds(By.ID, "username"))
            if elements_len <= 0:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
            # 如果 username 不存在，就会触发 until 中的列循环
            return elements_len > 0

        self.find(By.CSS_SELECTOR, "#menu_contacts").click()
        # self.wait_for_condition(add_member_condition)
        self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()

        return AddMember(self._driver)

    def goto_import_address(self):
        """
        导入通讯录
        :return:
        """
        pass

    def goto_join_member(self):
        """
        成员加入
        :return:
        """
