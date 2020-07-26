#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml

from app.page.app import App

with open('../datas/addcontact.yml') as f:
    addcontactdatas = yaml.safe_load(f)

with open('../datas/delcontact.yml') as f:
    delcontactdatas = yaml.safe_load(f)


class TestContact:

    def setup_class(self):
        self.app = App()
    def teardown_class(self):
        self.app.stop()

    def setup(self):
        self.main = self.app.start().goto_main()
    def teardown(self):
        self.app.back(5)

    @pytest.mark.parametrize('name,gender,phonenum',
                             addcontactdatas)
    def test_addcontact(self, name, gender, phonenum):
        '''
        添加联系人
        '''
        # name = "霍格name2"
        # gender = "女"
        # phonenum = "13700000002"
        mypage = self.main.goto_contactlist(). \
            add_contact().add_menual(). \
            set_name(name).set_gender(gender).set_phonnum(phonenum).click_save()
        text = mypage.get_toast()
        # mypage.add_menual()
        assert '成功' in text
        self.app.back()
