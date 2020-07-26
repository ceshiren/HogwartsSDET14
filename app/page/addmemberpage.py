#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
添加成员页
'''
# from app.page.contactaddpage import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from app.page.basepage import BasePage


class AddMemberPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    add_manual_element = (MobileBy.XPATH,
                          "//android.widget.TextView[@text='手动输入添加']")
    toast_ele = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def add_menual(self):
        '''
        手动输入添加
        '''
        from app.page.contactaddpage import ContactAddPage
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//android.widget.TextView[@text='手动输入添加']").click()
        self.find_and_click(self.add_manual_element)

        return ContactAddPage(self.driver)

    def get_toast(self):
        # text = '成功'
        # element = WebDriverWait(self.driver, 10).until(
        #     lambda x: x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        element = self.webdriver_wait(self.toast_ele)
        result = element.text
        return result
