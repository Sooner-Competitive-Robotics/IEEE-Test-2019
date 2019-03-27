import json

def jsonread():
	with open('/home/pi/locations/mars1.json') as data_file:
		data = json.load(data_file)
	
	return data
	