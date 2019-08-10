import sys,os
sys.path.append(os.getcwd())
import yaml
from Base.Read_Yml import ret_yaml_data


def ret_yaml_data(file_name):
    file_path = '/Users/xuanlonghua/PycharmProjects/lLe_Project/Data' + os.sep + file_name + ".yml"
    with open(file_path,"r") as f:
        return yaml.load(f,Loader=yaml.FullLoader)

def yaml_data():
    data_list = []
    data = ret_yaml_data("qq_login").get("QQ_login")
    for i in data.keys():
        data_list.append((i,data.get(i).get("username"),data.get(i).get("password")))
        return data_list

abc = yaml_data()


print(abc)