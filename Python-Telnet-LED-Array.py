#!/usr/bin/env python

# Uses Python, telnet and RegEx
# to read Cisco switch interface receive load,
# convert to a percentage
# and display on Scroll pHAT HD (LED array).

# On 100 Mbps switch port
# x percent = x Mbps

import getpass
import sys
import telnetlib
import re

import signal
import time
import scrollphathd

HOST = "10.0.90.103"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

# user = "john"
# password = "TempPass"
# mysecret = "TempSecret"

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

# "username john privilege 15" added to switches,
# so enable password not required.

# tn.write("enable\n")
# tn.write(mysecret + "\n")

tn.write("show interfaces Fa1/0/37 | include load\n")
tn.write("exit\n")

# print tn.read_all()
mystr = tn.read_all()
print mystr

x = re.findall("load\s(\d+)\/", mystr)
print x

txload = x[0]
rxload = x[1]

print txload + " - txload"
print rxload + " - rxload"

rxpct = 100 * (float(rxload) / 255)
print str(rxpct) + " - float value"

rxpct = round(rxpct)
print str(rxpct) + " - round value"

rxpct = int(rxpct)
print str(rxpct) + " - int value"

rxpct = str(rxpct)
print rxpct + " - str value"


# Display on LED array

scrollphathd.clear()

scrollphathd.write_string(rxpct, x=0, y=0, font=None, letter_spacing=1, brightness=0.2)

scrollphathd.show()
time.sleep(4)
