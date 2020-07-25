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
# user = raw_input("Enter your telnet username: ")
# password = getpass.getpass()

user = "john"
password = "TempPass"
mysecret = "TempSecret"

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
# tn.write("TempSecret\n")
tn.write(mysecret + "\n")

tn.write("show interfaces Fa1/0/37 | include load\n")
tn.write("exit\n")

# print tn.read_all()
mystr = tn.read_all()
print mystr

x = re.findall("load\s(\d+)\/", mystr)
print x

txload = x[0]
rxload = x[1]

print "txload"
print txload

print "rxload"
print rxload

rxpct = 100 * (float(rxload) / 255)
print "float value"
print rxpct

rxpct = round(rxpct)
print "round value"
print rxpct

rxpct = int(rxpct)
print "int value"
print rxpct

rxpct = str(rxpct)
print "str value"
print rxpct


# Display on LED array

scrollphathd.clear()

scrollphathd.write_string(rxpct, x=0, y=0, font=None, letter_spacing=1, brightness=0.2)

scrollphathd.show()
time.sleep(4)
