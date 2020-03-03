import time,os,logging
from selenium.webdriver.support.ui import WebDriverWait
from baseView.BaseElement import Element
from selenium.webdriver.support import expected_conditions as EC
class BaseView(object):
    def __init__(self,driver):
        self.driver=driver

    def get_element(self,type,*loc):
        elements = {
            Element.find_element_by_id: lambda: self.driver.find_element(*loc),

        }
        return elements[type]()


    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def send_keys(self,key,*loc):
        self.find_element(*loc).clear()
        return self.find_element(*loc).send_keys(key)

    def get_time(self):
        self.now=time.strftime("%Y%m%d%H%M%S")
        return self.now

    def get_window_size(self):
        """
        获取窗口大小
        :return:
        """
        return self.driver.get_window_size()

    def get_screenshot(self,name):
        '''截图方法'''
        time=self.get_time()
        image_file=os.path.dirname(os.path.dirname(__file__))+'/screenshots/{0}_{1}.png'.format(time,name)
        logging.info('get screenshot:{} '.format(image_file))
        self.driver.get_screenshot_as_file(image_file)

    def get_toast(self,value,method=None):
        if method =='allvalue':
            logging.info('匹配全部值')
            mag = '//*[@text=\'{}\']'.format(value)
            try:
                toast=WebDriverWait(self.driver,5).until(lambda x:x.find_element_by_xpath(mag))
            except Exception as e:
                logging.info('匹配失败')
                return False
            else:
                logging.info('匹配成功:{}'.format(toast.text))
                return True
        else:
            logging.info('匹配部分值')
            mag = ("xpath", ".//*[contains(@text,'{}')]".format(value))
            try:
                toast = WebDriverWait(self.driver,5).until(EC.presence_of_element_located(mag))
            except Exception as e:
                logging.info('匹配失败')
                return False
            else:
                logging.info('匹配成功:{}'.format(toast.text))
                return True
        #logging.info(toast.text)




    def swipe(self,direction,duration):
        """
        :param direction:Up上--- Down---下  Left---左  Right---右
        :param duration:持续时间
        :return:
        """
        size=self.get_window_size()
        x=size['width']
        y=size['height']
        x1=int(x*0.1)
        x5=int(x*0.5)
        x9=int(x*0.9)
        y1=int(y*0.1)
        y5=int(y*0.5)
        y9=int(y*0.9)

        if direction == 'Up' or direction == 'up':
            logging.info('向上滑动')
            return self.driver.swipe(x5,y9,x5,y1,duration)
        elif direction == 'Down' or direction == 'dowm':
            logging.info('向下滑动')
            return self.driver.swipe(x5,y1,x5,y9,duration)
        elif direction == 'Left' or direction == 'left':
            logging.info('向左滑动')
            return self.driver.swipe(x9,y5,x1,y5,duration)
        elif direction == 'Right' or direction == 'right':
            logging.info('向右滑动')
            return self.driver.swipe(x1,y5,x9,y5,duration)
        else:
            logging.error('滑动失败')