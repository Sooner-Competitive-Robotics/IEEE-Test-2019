import json
from pprint import pprint

with open('jsontest.json') as data_file:
	data = json.load(data_file)
pprint(data)

print("\n")
print(data["size"])
print("\n")
print(data["x coords"])
print("\n")
print(data["y coords"])