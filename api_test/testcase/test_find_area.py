# coding=utf-8
import requests,json

# result = requests.get("http://localhost:8899/hello")
#
# print result.text
# print result.json().get("foo")


def test_assert():
    "测试断言"
    assert 0==0

def test_assert_error():
    "测试断言错误"
    assert 1==1
