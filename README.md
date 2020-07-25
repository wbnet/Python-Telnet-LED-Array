# Python-Telnet-LED-Array
Using Scroll pHAT HD to show Cisco switch interface load

Uses Python, telnet and RegEx
to read Cisco switch interface receive load,
convert to a percentage
and display on Scroll pHAT HD (LED array).

On 100 Mbps switch port
x percent = x Mbps


---- Example output ----

LabSW3>enable
Password: 
LabSW3#show interfaces Fa1/0/37 | include load
     reliability 255/255, txload 29/255, rxload 28/255
LabSW3#exit

['29', '28']
txload
29
rxload
28
float value
10.9803921569
round value
11.0
int value
11
str value
11
