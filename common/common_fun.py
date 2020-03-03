#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/10
# @Author  : Mcen (mmocheng@163.com)
# @Name    : common_fun
from baseView.BaseView import BaseView
from selenium.webdriver.common.by import By
from common.desired_caps import appium_desired
import logging
import logging.config
import os,time

class Common(BaseView):
    button2=(By.ID,'android:id/button2')
    skipBtn=(By.ID,'com.tal.kaoyan:id/tv_skip')
    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')

    def check_cancelBtn(self):
        logging.info('====检查是否升级====')
        try:
            element = self.find_element(*self.button2)
            print(element)
        except Exception as e:
            logging.error('===没有找到元素===')
        else:
            logging.info('===点击升级按钮===')
            element.click()
    def check_skipBtn(self):
        logging.info("===检查跳过按钮===")
        try:
            element = self.find_element(*self.skipBtn)
        except Exception as e:
            logging.info('无跳过按钮元素!')
        else:
            logging.info('点击跳过按钮')
            element.click()

if __name__ == '__main__':
    driver=appium_desired()
    a=Common(driver)
    a.check_cancelBtn()


