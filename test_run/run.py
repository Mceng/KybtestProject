#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/11
# @Author  : Mcen (mmocheng@163.com)
# @Name    : run

import HTMLTestRunner    #引入HTMLTestRunner
import time,os
import unittest
from common.send_email import *

#1\定义文件查找的目录和测试报告生成的目录
test_case_dir='../test_case'
reports_dir = os.path.dirname(os.path.dirname(__file__))
now = time.strftime("%Y%m%d_%H%M%S",time.localtime())
reportname = now+"_result.html"

reportpath = os.path.join(reports_dir,'reports',reportname)


#定义测试套件
testunit=unittest.TestSuite()
#定义 discover 方法的参数
discover=unittest.defaultTestLoader.discover( test_case_dir , pattern ='test_l*.py' , top_level_dir=None )
#discover 方法筛选出来的用例，循环添加到套件中
for test_suite in discover:
    for test_case in test_suite:
        testunit.addTests(test_case)

with open(reportpath,'wb') as file:
    # 定义测试报告
    runner= HTMLTestRunner.HTMLTestRunner(stream=file,
                                       title=u'APP测试报告',
                                       description=u'用例执行情况')
    #运行Case
    runner.run(testunit)

#发送邮件
#send_mail()