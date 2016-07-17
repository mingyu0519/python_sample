# coding=utf-8
from sys import path,_getframe
path.append(r"./util")
import request_util

LOGIN_JSON = "data/login.json"

def login_test():
    request_util.fasttest(LOGIN_JSON, _getframe().f_code.co_name)

def login1_test():
    request_util.fasttest(LOGIN_JSON, _getframe().f_code.co_name)

login_test()
login1_test()
