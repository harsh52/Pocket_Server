#!/usr/bin/env python
from subprocess import *
import fileinput
with open("/etc/wpa_supplicant/wpa_supplicant.conf","w+") as network:
	metwork.write('network={\n'
'ssid="your_wifi_name\n"'
'psk="Wifi_password"\n"'
'proto=RSN\n'
'key_mgmt=WPA-PSK\n'
'pairwise=CCMP\n'
'auth_alg=OPEN\n'
'}')

with open("/etc/network/interfaces","w+") as a:
	a.write('auto wlan0\n'
		'allow-hotplug wlan0\n'
		'iface wlan0 inet dhcp\n'
		'wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf\n'
		'iface default inet dhcp\n')

