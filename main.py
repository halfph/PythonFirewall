import os
from time import sleep
from subprocess import run, PIPE
import requests

import FireWall

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

# Windows 防火墙
# 目的: Ban掉172.17.0.2和172.17.0.1 (http://172.17.0.1/) 游览器访问不到 不给访问登录校园网
# protocol后面跟的是协议类型 搬掉TCP https就访问不到了
# 搬掉icmp cmd就ping不到了
# netsh advfirewall firewall add rule name="ban connectInternet0" dir=out remoteip=xxx.xxx.xxx.xxx(这个地方是IP) action=block protocol=TCP

# netsh advfirewall firewall add rule name="ban connectInternet1" dir=out remoteip=172.17.0.1 action=block
# netsh advfirewall firewall add rule name="ban connectInternet4" dir=out remoteip=172.17.0.2 action=block

# 用来查看防火墙状态
# netsh advfirewall show currentprofile

command = "netsh advfirewall show allprofiles"


def fireWall():
    os.system(FireWall.Command.ping("119.91.141.182"))


print(FireWall.Command.ping("django"))
exit(0)
