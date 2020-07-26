#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
通讯录列表页
'''
from appium.webdriver.common.mobileby import MobileBy

from app.page.addmemberpage import AddMemberPage
from app.page.basepage import BasePage


class ContactListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    addmember_text = "添加成员"

    def add_contact(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()
        self.find_by_scroll(self.addmember_text).click()

        return AddMemberPage(self.driver)

    def search_contact(self):
        pass
