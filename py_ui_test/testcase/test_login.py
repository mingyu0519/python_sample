import os
from nose import with_setup
from time import sleep
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

DRIVER = None;

def initGlobal():
    global DRIVER
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = '36ffe29f'
    desired_caps['app'] = PATH('./ufenqi.apk')
    DRIVER = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def clean():
    global DRIVER
    DRIVER.quit()

@with_setup(initGlobal(),clean())
def test_inapp():
    print "in app"
    assert 1==1
