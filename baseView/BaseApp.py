#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/9/12
# @Author  : Mcen (mmocheng@163.com)
# @Name    : baseapp
import os
import subprocess
class AppBase(object):
    apppath=os.path.join(os.path.dirname(os.path.dirname(__file__)),'app','kaoyan3.1.0.apk')

    def get_app_package(self):
        """
        获取包名
        :return:
        """
        cmd = 'aapt dump badging {} | findstr package'.format(self.apppath)
        a=os.popen(cmd).read()
        result =''
        if a != '':
            dict=a.split( )
            result=dict[1][6:-1]
        return result

    def get_app_name(self):
        """
        获取应用名
        :return:
        """
        cmd = 'aapt dump badging {} | findstr application-label:'.format(self.apppath)
        a=subprocess.Popen(cmd,stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE,shell=True)
        # print(str((a.stdout.read()),encoding = "utf-8"))

        (output, err) = a.communicate()
        if output != "":
            result = output.split()[0].decode()[18:]
            print(result)
        return result

    def get_app_version(self):
        """
        获取app版本
        :return:
        """
        cmd = 'aapt dump badging {} | findstr versionName'.format(self.apppath)
        a=os.popen(cmd).read()
        result=''
        if a != '':
            dict=a.split( )
            # print(dict)
            result=dict[3][13:-1]
        return result

    def get_app_activity(self):
        """
        获取启动页
        :return:
        """
        cmd = 'aapt dump badging {} | findstr launchable-activity'.format(self.apppath)
        a=os.popen(cmd).read()
        result=''
        if a != '':
            dict=a.split( )
            # print(dict)
            result=dict[1][6:-1]
        return result
    def get_app_size(self):
        """
        获取app大小
        :return:
        """
        size = round(os.path.getsize(self.apppath)/(1024*1000),3)
        # print(str(size) + "M")
        return str(size) + "M"

    def get_men_total(self,devices):
        """
        获取最大运行内存
        :param devices:
        :return:
        """
        cmd = "adb -s " + devices + " shell cat /proc/meminfo"
        get_cmd = os.popen(cmd).readlines()
        men_total = 0
        men_total_str = "MemTotal"
        print(get_cmd)
        for line in get_cmd:
            if line.find(men_total_str) >= 0:
                men_total = line[len(men_total_str) + 1:].replace("kB","").strip()
                break

        # print(int(men_total))
        return int(men_total)

    def get_phone_info(self,devices):
        cmd = "adb -s "+ devices +" shell cat /system/build.prop"
        # phone_info = os.popen(cmd, mode="r").readlines()
        phone_info =subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()


        l_list = {}
        release = "ro.build.version.release=" # 版本
        model = "ro.product.model=" # 型号
        brand = "ro.product.brand=" # 品牌
        device = "ro.product.device=" # 设备名

        for line in phone_info:
             for i in line.split():
                temp = i.decode()
                if temp.find(release) >= 0:
                    l_list["release"] = temp[len(release):]
                    break
                if temp.find(model) >= 0:
                    l_list["model"] = temp[len(model):]
                    break
                if temp.find(brand) >= 0:
                    l_list["brand"] = temp[len(brand):]
                    break
                if temp.find(device) >= 0:
                    l_list["device"] = temp[len(device):]
                    break
        print(l_list)
        return l_list
if __name__ == '__main__':
    a=AppBase()
    a.get_phone_info('127.0.0.1:7555')
