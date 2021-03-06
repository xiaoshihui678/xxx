from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import threading
from selenium.webdriver.support.ui import WebDriverWait



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
        
        
class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def findElement(self,*args):
        return WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_xpath(*args))


class SendEmail(Base):
    loginIn = '//a[text()="帐号密码登录"]'
    usr = '//input[@id="u"]'
    pwd = '//input[@id="p"]'
    login_btn = '//input[@id="login_button"]'
    write_em = '//a[@id="composebtn"]'
    person = '//input[@accesskey="t"]'
    # person = '/html/body/form[2]/div[2]/div[3]/div[2]/table[1]/tbody/tr/td[2]/div[1]/div[2]/input'
    item = '//input[@id="subject"]'
    send_btn = '//a[@name="sendbtn"]'

    def send(self):
        # self.findElement(self.loginIn).click()
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame('login_frame')
        self.findElement(self.usr).send_keys('568582494')
        self.findElement(self.pwd).send_keys('xiaoshihui666')
        self.findElement(self.login_btn).click()
        self.findElement(self.write_em).click()
        self.driver.implicitly_wait(5)
        self.driver.switch_to.frame('mainFrame')
        self.findElement(self.person).send_keys('450837357@qq.com')
        self.findElement(self.item).send_keys('浦建你是傻逼吗，收到请回答')
        self.findElement(self.send_btn).click()


list = {'http://192.168.1.10:6666/wd/hub'}

driver = webdriver.Remote(command_executor=host,desired_capabilities=DesiredCapabilities.CHROME)
url = 'https://mail.qq.com/'
# driver = webdriver.Firefox(r'/Applications/Firefox.app/Contents/MacOS/firefox')
#driver = webdriver.Chrome(r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
driver.get(url)
driver.maximize_window()
s = SendEmail(driver)
s.send()
driver.quit()
