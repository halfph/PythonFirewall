import atexit
import os
from time import sleep
from subprocess import run, PIPE
import requests

import DisConnectInternet
import FireWall


def work():
    DisConnectInternet.Logout()
    FireWall.BlockIP()


# @atexit.register
# def clean():
#     FireWall.Check()


work()