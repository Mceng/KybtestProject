#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/7
# @Author  : Mcen (mmocheng@163.com)
# @Name    : send_email

import smtplib,os,time
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
import logging
import logging.config


def send_mail():
    dir = "../reports"
    lists = os.listdir(dir)
    lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn))
    file_new = os.path.join(dir, lists[-1])

    #定义发送及接收邮箱
    sender = '754730687@qq.com'
    receiver = '879867236@qq.com'
    subject = '发送邮件标题'

    # 配置第三方 SMTP 服务，如qq
    smtpserver = 'smtp.qq.com'
    username = '754730687@qq.com'
    password = 'rlgjycbvmxfrbbbh'

    #创建一个带附件的实例
    msg = MIMEMultipart('related')
    msg['From']=formataddr(["发送人",sender])
    msg['To']=formataddr(["收件人",receiver])
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    msg['Subject'] = Header(subject, 'utf-8')
    msg.attach(MIMEText('邮件发送正文内容', 'html', 'utf-8'))

    # 构造附件1，传送当前目录下的html文件
    att1 = MIMEText(open(file_new, 'rb').read(), 'html', 'utf-8')
    # 构造附件，传送当前目录下的html文件
    att1["Content-Type"] = 'application/octet-stream'
    # filename为邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="AnlewoTestReport.html"'
    msg.attach(att1)

    try:
        smtp=smtplib.SMTP_SSL(smtpserver, 465)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except Exception as e:
        print("Error: 无法发送邮件")

if __name__ == '__main__':
    send_mail()
