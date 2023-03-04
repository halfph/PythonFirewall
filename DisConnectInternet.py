import os
from subprocess import run, PIPE
from time import sleep

import constants
import requests

constants.LOGOUT_URL = "http://172.17.0.2:801/eportal/?c=ACSetting&a=Logout&loginMethod=1" \
                       "&protocol=http%3A&hostname=172.17.0.2&port=&iTermType=1&wlanuserip=null" \
                       "&wlanacip=null&wlanacname=null&redirect=null&session=null&vlanid" \
                       "=undefined&mac=00-00-00-00-00-00&ip=&queryACIP=0&jsVersion=2.4.3 "
constants.CHECK_TIME = 30


def Logout():
    response = requests.get(constants.LOGOUT_URL).status_code
    print("状态码{}".format(response))


def checkInternet():
    return run("ping baidu.com", stdout=PIPE, stderr=PIPE, stdin=PIPE,
               shell=True).returncode


def Persistence():
    while True:
        if checkInternet() == 0:
            Logout()
        sleep(constants.CHECK_TIME)


Persistence()