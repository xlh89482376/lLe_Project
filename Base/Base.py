from selenium.webdriver.support.wait import WebDriverWait
import time

class Base:
    def __init__(self,driver):
        self.driver = driver

    def find_element_I(self,loc,timeout=10,poll=0.5):
        """
        :param loc: 元祖 例如：(By.ID, ID属性值)...
        :param timeout:
        :param poll:
        :return: 返回定位对象
        """
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))

    def find_elements_I(self,loc,timeout=10,poll=0.5):
        """
        :param loc: 元祖 例如：(Bt.ID, ID属性值)...
        :param timeout:
        :param poll:
        :return:返回定位对象
        """
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))

    def click_element(self,loc):
        # 点击元素
        self.find_element_I(loc).click()

    def click_elements(self,loc,num):
        self.find_elements_I(loc)[num].click()

    def input_text(self,loc,text):
        # 输入操作
        input = self.find_element_I(loc)
        input.clear()
        input.send_keys(text)


