import smbus
import time
import startup
from vision import vision
from gpiozero import Button
from picamera import PiCamera
import RPi.GPIO as GPIO


# This sequence determines the cube's location relative to the robot's location
# then moves accordingly to center itself. 

address1 = 10
bus = smbus.SMBus(1)
camera = PiCamera()
camera.resolution = (600, 600)
camera.rotation = 180

myvision = Vision()
myNano = NanoManager()

while True:	
	
	print('begin')
	
	while (True):
		# read image
		camera.capture("center.jpg")
		
		if (myvision.getCenter("center.jpg") == 1):
			print('strafe right')
			bus.write_i2c_block_data(address1, 0, [0, 1, 0.3])
			time.sleep(myNano.getWaitTime(myNano.convertInchesToSteps(0.3)))
		elif (myvision.getCenter("center.jpg") == -1):
			print('strafe left')
			bus.write_i2c_block_data(address1, 0, [0, -1, 0.3])
			time.sleep(myNano.getWaitTime(myNano.convertInchesToSteps(0.3)))
		elif (myvision.getCenter("center.jpg") == -1):
			bus.write_i2c_block_data(address1, 0, [0, 1, 1])
			time.sleep(myNano.getWaitTime(myNano.convertInchesToSteps(0.3)))
		else:
			print('center')
			break
	
	print('while done')
	#calculate distance to object	
	# distance in inches
	dist = 12	
	# while !turn
	forward = 1
	turn = 0
	strafe = 0
	# angle 1 for turning -90 to 90
	angle1 = 0
	# angle 2 for turning -180 to 180
	#angle2 = 0
	
	print('before signal')
	bus.write_i2c_block_data(address1, 0, [forward, strafe, dist])
	print('signal sent')