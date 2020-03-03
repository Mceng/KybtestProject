#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-28 12:53:33
# @Author  : Mcen (mmocheng@163.com)
# @Link    : http://example.org
# @Version : $Id$

import unittest
import logging
from common.unitStartEnd import StartEnd
from PageObject.LoginPage import LoginView
from ddt import ddt,data,unpack,file_data

@ddt
class test_LoginCase(StartEnd):
    @data(
        {'username':'mmoo12','password':'q123456'}
    )
    @unpack
    def test_login_pass(self,username,password):
        logging.info('=====test_login_mmoo=======')
        a=LoginView(self.driver)
        a.login_action(username,password)
        self.assertTrue(a.login_status())

    @data(
        {'username':'自学网2017','password':'zxw2018'}
    )

    @unpack
    # @unittest.skip('123')
    def test_login_fail2017(self,username,password):
        logging.info('=====test_login_自学网2017=======')
        a=LoginView(self.driver)
        a.login_action(username,password)
        self.assertFalse(a.login_status())
    @data(
        {'username':'自学网2018','password':'zxw2018'}
    )
    @unpack
    @unittest.skip('123')
    def test_login_2018(self,username,password):
        logging.info('=====test_login_自学网2018=======')
        a=LoginView(self.driver)
        a.login_action(username,password)
        self.assertFalse(a.login_status())

if __name__ == '__main__':
    unittest.main()
		
		
	
