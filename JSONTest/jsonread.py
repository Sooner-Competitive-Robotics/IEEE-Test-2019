import json

def jsonread():
	print("hi\n")
	with open('jsontest.json') as data_file:
		data = json.load(data_file)
	
	return data