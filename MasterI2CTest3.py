import smbus
import time
import startup
from vision import vision
from gpiozero import Button
from picamera import PiCamera
import RPi.GPIO as GPIO

bus = smbus.SMBus(1)
address1 = 10
# address2 = 2

#start()
camera = PiCamera()
camera.resolution = (600, 600)
camera.rotation = 180

myvision = vision()

while True:	
	
	print('begin')
	
	while (True):
		camera.capture("center.jpg")
		
		if (myvision.getCenter("center.jpg") == 1):
			print('strafe right')
			bus.write_i2c_block_data(address1, 0, [0, 1, 1])
		elif (myvision.getCenter("center.jpg") == -1):
			print('strafe left')
			bus.write_i2c_block_data(address1, 0, [0, -1, 1])
		elif (myvision.getCenter("center.jpg") == -1):
			bus.write_i2c_block_data(address1, 0, [0, 1, 1])
		else:
			print('center')
			break
		time.sleep(5)
	
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
	
	
	
	#TODO: Wait for response that operation is finished
	time.sleep(50000)
	
	

# turn method
# def turn (target, current, 
	
# Method 1
	# At JSON file location
	
	# Take picture
	
	# Locate block using distance and height calculations
	
	# Adjust robot to block
	
	# Pick block up
