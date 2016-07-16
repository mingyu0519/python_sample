# coding=utf-8
import requests,json

# result = requests.get("http://localhost:8899/hello")
#
# print result.text
# print result.json().get("foo")


def login_pass_test():
    result = requests.get("http://localhost:8899/hello")
    assert 0==result.json().get("resultcode")

def login_fail_test():
    assert 1==2
