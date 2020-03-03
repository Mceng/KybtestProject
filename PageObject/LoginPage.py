import logging,time
from common.desired_caps import appium_desired
from common.common_fun import Common
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

class LoginView(Common):

    login_username=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
    login_password=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
    login_Btn=(By.ID,'com.tal.kaoyan:id/login_login_btn')
    task_no_task=(By.ID,'com.tal.kaoyan:id/task_no_task')
    usercenter_username=(By.ID,'com.tal.kaoyan:id/activity_usercenter_username')




    def Login_swipe(self):
        self.check_cancelBtn()
        #self.swipe('left',2000)
        self.check_skipBtn()

    def login_action(self,username,password):
        self.Login_swipe()
        logging.info('输入用户名:{}'.format(username))
        self.find_element(*self.login_username).send_keys(username)
        logging.info('输入密码{}'.format(password))
        self.send_keys(password,*self.login_password)
        logging.info('点击登陆')
        self.find_element(*self.login_Btn).click()
        #self.get_toast('用户名或密码错误')


    def login_status(self):
        self.login_after_ad()
        logging.info('检查是否登陆成功')
        try:
            self.find_element(*self.button_mysefl).click()
            element=self.find_element(*self.usercenter_username)
        except Exception:
            logging.error('登陆失败')
            self.get_screenshot('登陆失败')
            return False
        else:
            logging.info('{}--登陆成功'.format(element.text))
            return True

    def login_after_ad(self):
        logging.info('检查登陆后的广告')
        try:
            element=self.find_element(*self.task_no_task)
        except Exception:
            logging.info('登陆后的没有广告')
        else:
            logging.info('点击登陆后的广告')
            element.click()
    def login_after_ad(self):
        logging.info('检查登陆后的广告')
        try:
            element=self.find_element(*self.task_no_task)
        except Exception:
            logging.info('登陆后的没有广告')
        else:
            logging.info('点击登陆后的广告')
            element.click()

if __name__ == '__main__':
    deriver=appium_desired()
    a=LoginView(deriver)
    # a.login_action('q1234','12356')
    a.login_action('mmoo12', 'q123456')
    # self.login_status()







		