#!/usr/bin/env python3
import glob
import time
from datetime import datetime
from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost',
			port=8086,
			username='admin',
			password='beer')

temp_f = 0
base_dir = '/sys/bus/w1/devices/'
device_files = []
device_files.append(base_dir + '/28-3c01f095bdb1/w1_slave')
device_files.append(base_dir + '/28-3c01f0955b4b/w1_slave')
device_files.append(base_dir + '/28-3c01f095e5c0/w1_slave')

def read_temp_raw(device_file):
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp(device_file):
	lines = read_temp_raw(device_file)
	#while lines[0].strip()[-3:] == "YES":
	#time.sleep(0.2)
	#lines = read.temp.raw_a
	equals_pos =  lines[1].find('t=')
	#print(equals_pos)
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		#print("temp_string ",temp_string)
		temp_c = float(temp_string) / 1000 + 0.7
		global temp_f
		temp_f = temp_c * 9.0 / 5.0 + 32
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
		fermtemp_temp = float(temperature_results[0])
		ambtemp_temp = float(temperature_results[1])
		airtemp_temp = float(temperature_results[2])
		#print("Look at this ",fermtemp_temp, ambtemp_temp)
		line="temp_info,sensor=temp1 fermtemp=%f,ambtemp=%a,airtemp=%r" %  (fermtemp_temp,ambtemp_temp,airtemp_temp)
		#print(line)		
		client.write([line],{'db':'temperatures'}, 204, 'line')
		#file1.write(str(temperature_results[device_num]))
		#print('Probe 1: ' + str(temperature_results[0]) + ' F, ' + 'Probe 2: ' + str(temperature_results[1]) + ' F  at ' + dt_string)
		#print('Probe #2: ' + str(temperature_results[1]) + ' F' + ' at ' + dt_string) 
		#client.close()
		time.sleep(60)
