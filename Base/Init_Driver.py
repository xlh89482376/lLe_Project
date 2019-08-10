from appium import webdriver
import os

command_executor = "http://127.0.0.1:4723/wd/hub"

def init_driver():
    desired_caps = {
        # 系统
        'platformName': 'Android',
        # 版本
        'platformVersion': '5.0',
        # 设备号
        'deviceName': os.popen('adb devices').readlines()[1][0],
        # 包名
        'appPackage': 'com.tencent.news',
        # app名
        # 'app': appLocation,
        # 启动名
        'appActivity': '.activity.SplashActivity',
        # 允许中文输入
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        # 应用不进行重置
        'noReset': True
    }
    driver = webdriver.Remote(command_executor,desired_caps)
    return driver
