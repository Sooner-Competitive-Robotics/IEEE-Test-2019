import smbus
import time
import startup
import math
import RPi.GPIO as GPIO
from vision import vision
from gpiozero import Button
from picamera import PiCamera
import jsonread
import copyjson
from NanoManager import NanoManager

# IEEE competition code

address1 = 10						# Address to the drive nano
address2 = 20						# Address to the arm nano

bus = smbus.SMBus(1)
camera = PiCamera()
camera.resolution = (600, 600)
camera.rotation = 180

myvision = vision()
myNano = NanoManager


# List of info to send. Format is [forward, side, distance]
data = []cd

while True:
	print('begin')
	
	# Get JSON file location
	data = jsonread.jsonread()
	size = data["size"]
	# no way block is at 4,4 (starting location of robot)
	# no way closest block is 5 feet away
	minDist = 5 # feet
	minX = 4
	minY = 4

	# interates through all coordinates and finds minimum distance and at what coordinates
	while (size > 0):
		print(size)
		print("\n")
		dist = abs(math.sqrt(math.pow((data["x coords"][size - 1] - 4), 2)+math.pow((data["y coords"][size - 1] - 4), 2)))
		if (dist < minDist):
			minX = data["x coords"][size - 1]
			minY = data["y coords"][size - 1]
			minDist = dist
		size = size - 1
	
	print("MinX:", minX)
	print("\n")
	print("MinY:", minY)
	print("\n")
	
	# Drive to one location
		# if y coordinate is < 4 turn 180, > 4 nothing, = 4 turn 90 or -90 depending on x coor
		# if x coordinate is < 4 strafe left, > 4 strafe right, else nothing
		# stop one block away from actual location maybe?
	
	#drive up to cube 
	# if y != 4, drive (abs(y coord - 4ft) - 1 ft)
	# if y == 4, drive (abs(x coord - 4ft) - 1 ft)
	if (minY == 4):
		if (minX < 4):
			#turn -90
			data = [0, 0, 0, -90]
			driveRobot(address1, data)
		else:
			#turn 90
			data = [0, 0, 0, 90]
			driveRobot(address1, data)
		
		#drive to cube
		data = [1, 0, 12*(minX - 4 - 1)]
	else:
		if (minY > 4):
			if (minX < 4):
				#strafe left
				data = [0, -1, 12*abs(minX - 4)]
				driveRobot(address1, data)			
			else if (minX > 4):
				# strafe right
				data = [0, 1, 12*abs(minX - 4)] 
				driveRobot(address1, data)				
		else if (minY < 4):
			#turn 180
			data = [0, 0, 0, 90]
			driveRobot(address1, data)
			data = [0, 0, 0, 90]
			driveRobot(address1, data)
			if (minX < 4):
				#strafe right (reverse because we turned 180)
				data = [0, 1, 12*abs(minX - 4)]
				driveRobot(address1, data)
			else if (minX > 4):
				#strafe left
				data = [0, -1, 12*abs(minX - 4)]
				driveRobot(address1, data)
		
		data = [1, 0, 12*(minY - 4 - 1)]


# Sends I2C signal then wait until the end
def driveRobot(address, data):
	bus.write_i2c_block_data(address, 0, data)
	time.sleep(myNano.getWaitTime(myNano.convertInchesToSteps(data[2])))
	