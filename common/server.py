#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/12
# @Author  : Mcen (mmocheng@163.com)
# @Name    : server
import subprocess
import os
class server(object):
    def get_devices(self):
        cmd='adb devices'
        a=os.popen(cmd).read()
        dict=str(a).splitlines()
        # print(dict)
        if len(dict)>2:
            # print(dict[1].split()[0])
            return dict[1].split()[0]
        else:
            print('devices找不到')
    def connect_devices(self):
        cmd='start /b adb connect 127.0.0.1:7555'
        a=os.popen(cmd).read()
        if '无法连接' in a:
            print('由于目标计算机积极拒绝，无法连接')
        elif 'already' in a:
            print('已经连上，无需重新连')
        else:
            print('连接成功')


if __name__ == '__main__':
    s=server()
    s.get_devices()
    # s.connect_devices()