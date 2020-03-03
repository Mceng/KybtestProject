#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/10
# @Author  : Mcen (mmocheng@163.com)
# @Name    : desired_caps

from appium import webdriver
import yaml
import logging
import logging.config
import os

CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired():
    with open('../config/caps.yaml','r',encoding='utf-8') as file:
        data=yaml.load(file)
    app_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(app_dir,'app',data['appname'])

    desired_caps={
        'platformName': data['platformName'],
        'deviceName': data['deviceName'],
        # 'udid' : data['udid'],
        'platformVersion': data['platformVersion'],
        'appPackage': data['appPackage'],
        'appActivity': data['appActivity'],
        'noReset': data['noReset'],
        # 'app' : app_path,
        'unicodeKeyboard': data['unicodeKeyboard'],
        'resetKeyboard': data['resetKeyboard'],
        #'automationName': data['automationName']
    }

    logging.info('start app...')
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    appium_desired()
