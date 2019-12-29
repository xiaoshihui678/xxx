from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


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
        self.driver.switch_to.frame('login_frame')
        self.findElement(self.usr).send_keys('568582494')
        self.findElement(self.pwd).send_keys('xiaoshihui666')
        self.findElement(self.login_btn).click()
        self.findElement(self.write_em).click()
        self.driver.switch_to.frame('mainFrame')
        self.findElement(self.person).send_keys('450837357@qq.com')
        self.findElement(self.item).send_keys('@qq.com')
        self.findElement(self.send_btn).click()


url = 'https://mail.qq.com/'
# driver = webdriver.Firefox(r'/Applications/Firefox.app/Contents/MacOS/firefox')
driver = webdriver.Chrome(r'/Users/xshsapple/Downloads/chromedriver')
driver.get(url)
driver.maximize_window()
s = SendEmail(driver)
s.send()
driver.quit()
