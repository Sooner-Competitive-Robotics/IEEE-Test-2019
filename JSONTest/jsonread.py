import json
from pprint import pprint

with open('data.json') as data_file:
	data = json.load(data_file)
pprint(data)

print("\n")
print(data["Location 1-6"]["X"])
print("\n")
print(data["Location 1-6"]["Y"])