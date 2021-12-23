import glob
import time
#import os
from datetime import datetime
#import  paho.mqtt.client as mqtt
#from influxdb import InfluxDBClient

#client = InfluxDBClient(host='localhost',
			#port=8086,
			#username='admin',
			#password='beer')

temp_f = 0
base_dir = '/sys/bus/w1/devices/'
device_files = []
device_files.append(base_dir + '/28-3c01f095bdb1/w1_slave')
device_files.append(base_dir + '/28-3c01f0955b4b/w1_slave')
#file1 = open("GetTemps.txt","a")

#mqttBroker = "mqtt.eclipseprojects.io"
#mqttBroker="192.168.86.234"
#client = mqtt.Client("mqtt")
#client.connect(mqttBroker)
#print(client)

#def on_connect(client, userdata, flags, rc):
#	if rc==0:
#		print("Connected OK, Returned code=", rc)
#	else:
#		print("Bad connection, returned code=", rc)

def read_temp_raw(device_file):
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp(device_file):
	lines = read_temp_raw(device_file)
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read.temp.raw_a
		#print("We madi it")
		equals_pos =  lines[1].find('t=')
		print(equals_pos)
		if equals_pos != -1:
			temp_string = lines[1][equals_pos+2:]
			print(temp_string)
			temp_c = float(temp_string) / 1000 + 0.7
			print(temp_c)
			global temp_f
			temp_f = float(temp_c * 9.0 / 5.0 + 32)
			print(temp_f)
			#temp_c = str(round(temp_c, 2))
			#print(temp_f)
			return temp_f

temperature_results = [0]*len(device_files)


while True:

	for device_num, device_file in enumerate(device_files):
		now = datetime.now()
		dt_string = now.strftime("%m/%d/%y  %H:%M:%S")
		temperature_results[device_num] = read_temp(device_file)
		#print(temperature_results[1])
		#line='temp_info,sensor=temp1 fermtemp=temperature_results[1],ambtemp=temperature_results[1]'
		#client.write([line],{'db':'temperatures'}, 204, 'line')
		#mosquitto_pub -h '192.168.86.234' -t "mqtt/temp1" -m "99"
		#client.publish("mqtt/temp1",temperature_results[0])
		#client.publish("mqtt/temp2",temperature_results[1])
		#file1.write(str(temperature_results[device_num]))
		#print('Probe 1: ' + str(temperature_results[0]) + ' F, ' + 'Probe 2: ' + str(temperature_results[1]) + ' F  at ' + dt_string)
		#print('Probe #2: ' + str(temperature_results[1]) + ' F' + ' at ' + dt_string) 
		#client.close()
		time.sleep(2)
