import sys
import subprocess 
import os
from decouple import config

IP_NETWORK = config('IP_NETWORK')
device_count=int(config('device_count'))
device_ip=[]
device_flag={}
device_name=[]

for i in range(0,device_count):
	device_ip.append(config('device_ip[' + str(i) + ']'))
	device_name.append(config('device_name[' + str(i) + ']'))
	device_flag[i]=True

proc = subprocess.Popen(["ping", IP_NETWORK], stdout=subprocess.PIPE)
while True:
	line = proc.stdout.readline()
	if not line:
		break

	connected_ip = line.decode('utf-8').split()[3]
	for i in range(0,device_count):
		if (connected_ip == str(device_ip[i]) and device_flag[i] == True):
			print (str(device_name[i]) +  " is connected")
			device_flag[i]=False