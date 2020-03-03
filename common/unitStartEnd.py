#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/11
# @Author  : Mcen (mmocheng@163.com)
# @Name    : unitStartEnd
import unittest
import logging
import logging.config
import time
from common.desired_caps import appium_desired
class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('=====setUp======')
        self.driver=appium_desired()

    def tearDown(self):
        logging.info('=====tearDown======')
        time.sleep(4)
        self.driver.close_app()


