# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:52:11 2022

@author: Victor
"""

import subprocess

results = subprocess.check_output(["netsh", "wlan", "show", "network"])
results = results.decode("ascii")
results = results.replace("\r","")
ls = results.split("\n")
ls = ls[4:]
ssids = []
x = 0
while x < len(ls):
    if x % 5 == 0:
        ssids.append(ls[x])
    x += 1
print(ssids)p