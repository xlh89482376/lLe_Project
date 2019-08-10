import sys,os,time
sys.path.append(os.getcwd())
import subprocess

class Tool():

    @staticmethod
    def open_logcat(test_num):
        #z启动logcat
        with open('/Users/xuanlonghua/PycharmProjects/lLe_Project/Logs/logcat/' + test_num + '_' + time.strftime("%Y-%m-%d_%H:%M:%S",
                                                                                                time.localtime(
                                                                                                        time.time())) + '.txt',
                  "w") as f:
            Poplog = subprocess.Popen('adb logcat -v time', stdout=f, shell=True)
        return Poplog

    @staticmethod
    def close_logcat(Poplog):
        #关闭logcat
        Poplog.terminate()



