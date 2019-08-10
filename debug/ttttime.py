import sys,os,time
sys.path.append(os.getcwd())
import subprocess
from appium import webdriver
from Tools.Tools import Tool

command_executor = "http://127.0.0.1:4723/wd/hub"


desired_caps = {
    # 系统
    'platformName': 'Android',
    # 版本
    'platformVersion': '5.0',
    # 设备号
    'deviceName': os.popen('adb devices').readlines()[1][0],
    # 包名
    'appPackage': 'com.android.settings',
    # app名
    # 'app': appLocation,
    # 启动名
    'appActivity': '.Settings',
    # 允许中文输入
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    # 应用不进行重置
    'noReset': True
}
driver = webdriver.Remote(command_executor,desired_caps)

time.sleep(3)



r = Tool.open_logcat()

driver.get_screenshot_as_file('./screenshot/'+time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime(time.time()))+'.png')
    #测试case
try:
    driver.start_activity("", "")
    driver.install_app("/Usghua/Downloads/698e4d14603d859b3e4d8c1e9d4826f0.apk")

except:
    driver.get_screenshot_as_file('/Users/xuanlonghua/PycharmProjects/lLe_Project/screenshot' + time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(time.time())) + '.png')
finally:
    #截图

    Tool.close_logcat(r)




driver.quit()


