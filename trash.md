# Windows 防火墙
### 目的: Ban掉172.17.0.2和172.17.0.1 (http://172.17.0.1/) 游览器访问不到 不给访问登录校园网
### protocol后面跟的是协议类型 搬掉TCP https就访问不到了
### 搬掉icmp cmd就ping不到了
### netsh advfirewall firewall add rule name="ban connectInternet0" dir=out remoteip=xxx.xxx.xxx.xxx(这个地方是IP) action=block protocol=TCP

### netsh advfirewall firewall add rule name="ban connectInternet1" dir=out remoteip=172.17.0.1 action=block
### netsh advfirewall firewall add rule name="ban connectInternet4" dir=out remoteip=172.17.0.2 action=block

### 用来查看防火墙状态
### netsh advfirewall show currentprofile

### command = "netsh advfirewall show allprofiles"
