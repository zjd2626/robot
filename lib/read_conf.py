#!/usr/bin/env python3
# coding=utf-8
#__author__='David Chung'


import configparser
import string
import random
import time
import os

cf = configparser.ConfigParser()

cf.read(os.path.abspath("../conf/dell.conf"))

login_url = cf.get("login", "login_url")
login_username = cf.get("login", "login_username")
login_password = cf.get("login", "login_password")

firefox_bin = cf.get("env", "firefox")
geckodriver = cf.get("env", "geckodriver")


def vmname_gen():
    seq = string.ascii_lowercase
    name = ''
    for i in range(random.randint(4, 16)):
        name += str(random.choice(seq))
    return "qa" + name


def diskname_gen():
    return "qa" + time.strftime("%Y%m%d%H%M%S")


vmname = vmname_gen()
diskname = diskname_gen()
