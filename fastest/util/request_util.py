# coding=utf-8
from sys import path
path.append(r"./util")
import json_util,requests,md5

SETTING = "data/conf/setting.json"

# 发送接口测试请求
def request(url,method):
    result = None
    if method.lower() == "get":
        result = requests.get(url)
    elif method.lower() == "post":
        result = requests.post(url)
    else :
        raise Exception("请求方法异常！")
    return result

# 测试接口入口
def fasttest(json,att):
    # 获取请求数据
    test_data = json_util.read(json,att)
    url = test_data.get("url")
    method = test_data.get("method")
    params = test_data.get("request")
    check_data = test_data.get("check")

    # 获取setting数据
    host = json_util.read(SETTING,"host")
    port = json_util.read(SETTING,"port")

    # 拼接完整的url
    url = "http://" + host + ":" + str(port) + "/" + url

    # 获取请求结果
    result = request(url,method)
    print result.headers
    print result.status_code == 200
    print result.text
    # assert result.status_code == 200
    # assert result.text
