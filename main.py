import sys
import subprocess 
import os
from decouple import config

IP_NETWORK = config('IP_NETWORK')
shubhra_iphone = config('shubhra_iphone')
chandra_big_iphone=config('chandra_big_iphone');
shubhra_iphone_check=True
chandra_big_iphone_check=True

proc = subprocess.Popen(["ping", IP_NETWORK], stdout=subprocess.PIPE)
while True:
	line = proc.stdout.readline()
	if not line:
		break

	connected_ip = line.decode('utf-8').split()[3]
	if connected_ip == shubhra_iphone and shubhra_iphone_check:
	 	print("shubra iphone connected to the network")
	 	shubhra_iphone_check=False
	elif connected_ip == chandra_big_iphone and chandra_big_iphone_check:
		print ("chandra iphone 6s+ connected to the netork")
		chandra_big_iphone_check=False