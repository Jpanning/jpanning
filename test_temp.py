from influxdb import InfluxDBClient
client = InfluxDBClient(host='localhost', 
			port=8086, 
			username='admin',
			password='beer')
line='temp_info,sensor=temp1 fermtemp=55,ambtemp=66'
client.write([line], {'db':'temperatures'}, 204, 'line')
client.close() 
