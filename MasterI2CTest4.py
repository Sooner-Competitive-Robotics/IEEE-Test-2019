import smbus
import time
import startup
from vision import vision
from NanoManager import NanoManager
from gpiozero import Button
from picamera import PiCamera
import RPi.GPIO as GPIO

def driveRobot(address, forward, strafe, dist):
    bus.write_i2c_block_data(address, 0, [forward, strafe, dist])
    waitTime = myNano.getWaitTime(myNano.convertInchesToSteps(dist))
    print("waiting: " + str(waitTime))
    time.sleep(waitTime)

# This sequence determines the cube's location relative to the robot's location
# then moves accordingly to center itself. 

address1 = 10
bus = smbus.SMBus(1)
camera = PiCamera()
camera.resolution = (600, 600)
camera.rotation = 180

myvision = vision()
myNano = NanoManager()

while True:	
	
	print('begin')
	
	while (True):
		# read image
		camera.capture("center.jpg")
		
		result = myvision.getCenter("center.jpg")
		
		if (result == 1):
			print("strafe right")
			#myNano.driveRobot(address1, 0, 1, 1)
		elif (result == -1):
			print("strafe left")
			#myNano.driveRobot(address1, 0, -1, 1)
		elif (result == -2):
			print("Block not found")
			#myNano.driveRobot(address1, -1, 0, 1)
		else:
			print("center")
			time.sleep(2)
			break
	
	print('while done')

	dist = 12	
	forward = 1
	turn = 0
	strafe = 0
	angle = 0
	
	print('before signal')
	#myNano.driveRobot(address1, 1, 0, 12)
	print('signal sent')
	
	time.sleep(5000000)
