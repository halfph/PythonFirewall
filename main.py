from time import sleep
from subprocess import run, PIPE
import requests

logoutUrl = "http://172.17.0.2:801/eportal/?c=ACSetting&a=Logout&loginMethod=1&protocol=http%3A&hostname=172.17.0.2" \
            "&port=&iTermType=1&wlanuserip=null&wlanacip=null&wlanacname=null&redirect=null&session=null&vlanid" \
            "=undefined&mac=00-00-00-00-00-00&ip=&queryACIP=0&jsVersion=2.4.3 "
loginUrl = "http://172.17.0.2:801/eportal/?c=ACSetting&a=Login&loginMethod=1&protocol=http%3A&hostname=172.17.0.2&port" \
           "=&iTermType=1&wlanuserip=10.128.71.201&wlanacip=210.36.18.65&wlanacname=ME60-1&redirect=null&session=null" \
           "&vlanid=0&mac=06-6f-bb-d0-bf-cd&ip=10.128.71.201&enAdvert=0&jsVersion=2.4.3&DDDDD=%2C0%2C2007310308" \
           "%40telecom&upass=113998&R1=0&R2=0&R3=0&R6=0&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag" \
           "=&username=&password=&user=&cmd=&Login= "

# logoutUrl = "http://172.17.0.2:801/eportal/?c=ACSetting&a=Logout&loginMethod=0&protocol=http%3A&hostname=172.17.0.2&port=&iTermType=1&wlanuserip=null&wlanacip=null&wlanacname=null&redirect=null&session=null&vlanid=undefined&mac=00-00-00-00-00-00&ip=&queryACIP=0&jsVersion=2.4.3"
# loginUrl = "http://172.17.0.2:801/eportal/?c=ACSetting&a=Login&loginMethod=1&protocol=http%3A&hostname=172.17.0.2&port=&iTermType=1&wlanuserip=10.128.71.201&wlanacip=210.36.18.65&wlanacname=ME60-1&redirect=null&session=null&vlanid=0&mac=06-6f-bb-d0-bf-cd&ip=10.128.71.201&enAdvert=0&jsVersion=2.4.3&DDDDD=%2C0%2C2007310308%40telecom&upass=113998&R1=0&R2=0&R3=0&R6=0&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag=&username=&password=&user=&cmd=&Login="

CheckInternetPerSecond = 5

def login():
    response = requests.get(loginUrl).status_code
    print("状态码{}".format(response))


def logout():
    response = requests.get(logoutUrl).status_code
    print("状态码{}".format(response))


def checkInternet():
    code = run("ping baidu.com", stdout=PIPE, stderr=PIPE, stdin=PIPE,
               shell=True).returncode
    return code


def fireWall():
    print()


while True:
    if checkInternet():
        print("现在是断网状态")
        print("现在开始重新联网")
        login()  # 重新开始登录
    else:
        print("现在是正常联网状态")
        print("准备断开网络")
        logout()
    sleep(CheckInternetPerSecond)     # 每隔1s 检测一次
