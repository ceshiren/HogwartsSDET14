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
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap").click()
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
