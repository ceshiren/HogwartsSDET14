#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
主页面
'''
from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage
from app.page.contactlistpage import ContactListPage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    contactlist = (MobileBy.XPATH,
                   "//android.widget.TextView[@text='通讯录']")

    def goto_contactlist(self):
        '''
        进入到通讯录
        '''
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//android.widget.TextView[@text='通讯录']").click()
        self.find_and_click(self.contactlist)

        return ContactListPage(self.driver)

    def goto_workbench(self):
        pass
