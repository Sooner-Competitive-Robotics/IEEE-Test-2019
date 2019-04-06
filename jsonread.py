import json
import os

def jsonread():
        path = '/home/pi/locations/mars1.json.txt'
        if (os.stat(path).st_size == 0):
                data = 0
        else:
                with open(path) as data_file:
                        data = json.load(data_file)
        return data
