from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import threading


list = {'http://192.168.1.10:6666/wd/hub',
        }
for host in list:
    driver = webdriver.Remote(command_executor=host,
                              desired_capabilities=DesiredCapabilities.CHROME)
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('吴浦建是傻逼吗')
    driver.find_element_by_id('su').click()
    time.sleep(2)
    driver.close()
