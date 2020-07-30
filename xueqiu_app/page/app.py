#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver

from xueqiu_app.page.base_page import BasePage
from xueqiu_app.page.main import Main


class App(BasePage):

    def start(self):
        '''
        启动app
        '''
        if self.driver == None:
            # 第一次调用start（）方法的时候driver 为None
            caps = {}
            caps["platformName"] = "android"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            # launch_app() 这个方法不需要传入任何参数， 会自动启动起来DesireCapa里面定义的activity
            # start_activity(packagename, activityname) 可以启动其它的应用的页面
            self.driver.launch_app()
        self.driver.implicitly_wait(20)
        return self

    def goto_main(self):
        """
        进入首页
        :return:
        """
        return Main(self.driver)
