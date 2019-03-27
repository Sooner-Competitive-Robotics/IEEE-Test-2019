import glob, os
from pprint import pprint
import shutil
import json

#for subdir in os.listdir("/C:"):
subdirpath = "D:"
if os.path.exists(subdirpath):
	for file in os.listdir(subdirpath):
		if file.endswith(".json"):
			shutil.copy(file, "C:/Users/Joseph Chang")
			break;
else:
	print("path not found")
				

with open('C:/Users/Joseph Chang/mars1.json') as data_file:
		data = json.load(data_file)
		pprint(data)