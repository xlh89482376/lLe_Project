from Page.qq_login import QQ_Login

class Page_obj:
    def __init__(self,driver):
        self.driver = driver

    def re_qq_login(self):
        #返回qq登陆对象页面
        return QQ_Login(self.driver)