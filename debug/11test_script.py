import sys,os
sys.path.append(os.getcwd())

from Page.Page_Obj import Page_obj
from Base.Init_Driver import init_driver
import pytest,time
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
import subprocess


command_executor = "http://127.0.0.1:4723/wd/hub"

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

# filename = './Logs/'+time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime(time.time()))+'.txt'#日志文件名添加当前时间
filename = os.getcwd().replace('debug','Logs/logcat/')+time.strftime("%Y-%m-%d_%H:%M:%S",time.localtime(time.time()))+'.txt'
logcat_file = open(filename,'w')
logcmd = 'adb logcat -v time'
Poplog = subprocess.Popen('adb logcat -v time',stdout=logcat_file,shell=True)
    # subprocess.Popen('adb logcat -v time',stdout=logcat_file,stderr=subprocess.PIPE)

#点击me
data = WebDriverWait(driver,10,1).until(lambda x:x.find_elements_by_id("com.tencent.news:id/b0e"))
data[3].click()
time.sleep(10)
#点击qq
driver.find_element_by_id("com.tencent.news:id/kf").click()
time.sleep(10)
#点击授权并登陆
data1 = driver.find_elements_by_id("android.widget.Button")
print(data1[0].text)

time.sleep(5)

logcat_file.close()
Poplog.terminate()
driver.quit()