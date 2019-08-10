from Base.Base import Base
import Page,time

class QQ_Login(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_me_btn(self):
        self.click_elements(Page.me_btn,3)

    def click_qq_btn(self):
        self.click_element(Page.qq_btn)

    def click_switch_btn(self):
        self.click_element(Page.switch_btn)

    def click_login(self,account,passwd):
        self.input_text(Page.qq_account,account)
        self.input_text(Page.qq_passwd,passwd)
        self.click_element(Page.login)
        time.sleep(3)
        self.click_element(Page.authorize_login)
        time.sleep(10)
        self.click_element(Page.Advertisement_back_btn)
