import sys,os
sys.path.append(os.getcwd())

from Base.Base import Base
from Page.Page_Obj import Page_obj
from Base.Init_Driver import init_driver
import pytest,time
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from Tools.Tools import Tool
import subprocess
from Base.Read_Yml import ret_yaml_data
import allure


def yaml_data():
    data_list = []
    data = ret_yaml_data("qq_login").get("QQ_login")
    for i in data.keys():
        data_list.append((i,data.get(i).get("username"),data.get(i).get("password")))
        return data_list

class Test_QQ_Login():
    def setup_class(self):
        self.driver = init_driver()
        self.qq_login_obj = Page_obj(self.driver).re_qq_login()

    def teardowm_class(self):
        self.driver.quit()

    @pytest.fixture()
    @allure.step(title='打开app，点击我')
    def click_me(self):
        # 点击 我 按钮
        self.qq_login_obj.click_me_btn()
        time.sleep(5)

    @allure.step(title='点击qq按钮')
    @pytest.fixture()
    def click_qq(self):
        # 点击 qq 按钮
        self.qq_login_obj.click_qq_btn()
        time.sleep(5)

    @allure.step(title='点击切换账号')
    @pytest.fixture()
    def click_switch_btn(self):
        #点击切换按钮
        self.qq_login_obj.click_switch_btn()
        time.sleep(5)

    @allure.step(title='输入用户名、密码，登陆')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures("click_me","click_qq","click_switch_btn")
    @pytest.mark.parametrize("test_num,account,passwd",yaml_data())
    def test_qq_login(self,test_num,account,passwd):
        allure.attach("描述:验证腾讯视频qq登陆功能")
        r = Tool.open_logcat(test_num)
        #测试case
        self.qq_login_obj.click_login(account,passwd)
        # self.driver.get_screenshot_as_file(
        #     './screenshot/' +test_num + time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time())) + '.png')
        #截图
        self.driver.get_screenshot_as_file('./screenshot/'+ test_num + '_' +time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime(time.time()))+'.png')
        Tool.close_logcat(r)






