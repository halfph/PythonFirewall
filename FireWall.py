import os


class Command:
    CheckFireWallStatus = "netsh advfirewall show allprofiles"
    TurnFireWallOn      = "netsh advfirewall set allprofiles state on"
    TurnFireWallOff     = "netsh advfirewall set allprofiles state off"
    ResetFireWall       = "netsh advfirewall reset"
    BanIpByAll          = 'netsh advfirewall firewall add rule name="ban connectInternet1" ' \
                          'dir=out remoteip=172.17.0.2 action=block'
    BanIpByTcp          = 'netsh advfirewall firewall add rule name="ban connectInternet1" ' \
                          'dir=out remoteip=172.17.0.2 action=block protocol=TCP'
    BanIpByIcmpIvp4     = 'netsh advfirewall firewall add rule name="ban connectInternet1" ' \
                          'dir=out remoteip=172.17.0.2 action=block protocol=icmpv4'
    BanIpByIcmpIvp6     = 'netsh advfirewall firewall add rule name="ban connectInternet1" ' \
                          'dir=out remoteip=172.17.0.2 action=block protocol=icmpv6'
    BlackList = []

    def __int__(self):
        pass

    def ping(self, xxx: str):
        return str("ping " + xxx)

    def checkFireWallStatus(self):
        os.system(self.CheckFireWallStatus)

    # 需要管理员权限
    def turnFireWallOn(self):
        os.system(self.TurnFireWallOn)

    def turnFireWallOff(self):
        os.system(self.TurnFireWallOff)

    def banIpByAll(self):
        os.system(self.BanIpByAll)

    def block(self):
        self.turnFireWallOn()
        self.banIpByAll()

    def reset(self):
        os.system(self.ResetFireWall)


def BlockIP():
    command = Command()
    command.checkFireWallStatus()


def Check():
    command = Command()
    command.checkFireWallStatus()
