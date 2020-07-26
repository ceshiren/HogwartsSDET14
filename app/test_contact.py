#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
联系人用例
'''
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

with open('datas/addcontact.yml') as f:
    addcontactdatas = yaml.safe_load(f)

with open('datas/delcontact.yml') as f:
    delcontactdatas = yaml.safe_load(f)


class TestContact:

    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["noReset"] = "true"
        caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
        # caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app
        caps['settings[waitForIdleTimeout]'] = 0

        # 与server 建立连接,初始化一个driver 创建session,返回一个sessionid
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize('name,gender,phonenum',
                             addcontactdatas)
    def test_addcontact(self, name, gender, phonenum):
        '''
        添加联系人用例设计
        1、打开应用
        2、点击通讯录
        3、点击添加成员
        4、手动输入添加
        5、输入【用户名】，姓别，手机号
        6、点击保存
        7、验证添加成功
        '''
        # name = "霍格name1"
        # gender = "女"
        # phonenum = "13700000001"
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.TextView[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()

        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.TextView[@text='手动输入添加']").click()
        # 设置姓名
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '姓名')]/../*[@class='android.widget.EditText']").send_keys(name)

        # 设置性别
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '性别')]/..//*[@text='男']").click()
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        # 设置手机号
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phonenum)

        # 点击保存
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").click()
        # 验证成功 Toast
        # self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        element = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        result = element.text
        assert '成功' in result
        self.driver.back()

    @pytest.mark.parametrize('name', delcontactdatas)
    def test_delcontact(self, name):
        '''
        删除联系人
        '''
        # name = "霍格沃兹name3"
        self.driver.find_element(MobileBy.XPATH,
                                 "//android.widget.TextView[@text='通讯录']").click()

        # 点击 搜索框
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq_").click()
        # 输入 联系人姓名
        self.driver.find_element(MobileBy.ID,
                                 "com.tencent.wework:id/ffq").send_keys(name)
        sleep(3)
        # 获取联系人列表
        elelist = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        # 判断 搜索出来的列表长度
        if len(elelist) < 2:
            print("没有这个联系人")
            return
        # 存在 联系人，点击第一个
        elelist[1].click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq0").click()
        # 点击 编辑成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        # 滚动查找  删除成员 并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()
        # 确定删除
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        sleep(2)
        # 验证删除成功
        elelist_after = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")

        assert len(elelist) - len(elelist_after) == 1
