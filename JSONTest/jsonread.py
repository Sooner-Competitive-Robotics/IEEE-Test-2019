import json
import math
from pprint import pprint

def jsonread():
	print("hi\n")
	with open('jsontest.json') as data_file:
		data = json.load(data_file)
	pprint(data)
	
	print("\n")
	print(data["size"])
	print("\n")
	print(data["x coords"])
	print("\n")
	print(data["y coords"])
	print("\n")
	
	return data
	
# Get JSON file location
data = jsonread()
size = data["size"]
minDist = 96 # inches
minX = 4
minY = 4

print(data["x coords"][5])

while (size > 0):
	print(size)
	print("\n")
	dist = abs(math.sqrt(math.pow((data["x coords"][size - 1] - 4), 2)+math.pow((data["x coords"][size - 1] - 4), 2)))
	if (dist < minDist):
		minX = data["x coords"][size - 1]
		minY = data["y coords"][size - 1]
	size = size - 1

print(minX)
print("\n")
print(minY)
print("\n")