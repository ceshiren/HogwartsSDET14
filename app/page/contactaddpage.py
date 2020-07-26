#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from app.page.addmemberpage import AddMemberPage
from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage


class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    name_element = (MobileBy.XPATH,
                    "//*[contains(@text, '姓名')]/../*[@class='android.widget.EditText']")
    gender_element = (MobileBy.XPATH,
                      "//*[contains(@text, '性别')]/..//*[@text='男']")
    male_ele = (MobileBy.XPATH, "//*[@text='男']")
    female_ele = (MobileBy.XPATH, "//*[@text='女']")
    phonenum_ele = (MobileBy.XPATH, "//*[@text='手机号']")
    save_ele = (MobileBy.ID, "com.tencent.wework:id/gq7")

    def set_name(self, name):
        # 设置姓名
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//*[contains(@text, '姓名')]/../*[@class='android.widget.EditText']").send_keys(name)

        self.find_and_sendkeys(self.name_element, name)
        return self

    def set_gender(self, gender):
        # 设置性别
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//*[contains(@text, '性别')]/..//*[@text='男']").click()
        self.find_and_click(self.gender_element)
        if gender == '男':
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
            self.find_and_click(self.male_ele)
        else:
            self.find_and_click(self.female_ele)
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        return self

    def set_phonnum(self, phonenum):
        # 设置手机号
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)
        self.find_and_sendkeys(self.phonenum_ele, phonenum)
        return self

    def click_save(self):
        from app.page.addmemberpage import AddMemberPage
        # 点击保存
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").click()
        self.find_and_click(self.save_ele)
        return AddMemberPage(self.driver)
