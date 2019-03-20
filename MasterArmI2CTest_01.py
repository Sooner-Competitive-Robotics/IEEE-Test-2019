import smbus
import time
import startup
from vision import vision
from gpiozero import Button
from picamera import PiCamera
import RPi.GPIO as GPIO

bus = smbus.SMBus(1)
address1 = 10
address2 = 20

#this code assumes that the robot is in position to pick up the cube
def main():
	startup.start()
	myvision = vision()

	while True:	
		
		print('begin')
		
		# writing to address 2, first byte is "state", 2nd byte is "angle or position"
		
		# put claw up
		clawUp()
		
		# make claw open
		clawOpen()
		
		print('ready to pick block up')
		
		# place block in position to be picked up
		time.sleep(7)
		
		# put claw down
		clawDown()
		
		# close claw
		clawClose()
		
		# put claw up
		clawUp()
		
		# extend
		extend()
		
		# retract
		retract()		
		
		print('finished running')
		
		#TODO: Wait for response that operation is finished
		time.sleep(50000)
	
def clawUp()
{
	# put claw up
	bus.write_i2c_block_data(address2, 0, [3, -40])
	time.sleep(2)
}

def clawDown()
{
	# put claw down
	bus.write_i2c_block_data(address2, 0, [3, 40])
	time.sleep(2)
}

def clawOpen()
{
	# make claw open
	bus.write_i2c_block_data(address2, 0, [2, -20])
	time.sleep(2)
}

def clawClose()
{
	# close claw
	bus.write_i2c_block_data(address2, 0, [2, 20])
	time.sleep(2)
}

def extend() 
{
	# extend arm
	bus.write_i2c_block_data(address2, 0, [1, 1])
	time.sleep(5)
}

def retract()
{
	# retract arm
	bus.write_i2c_block_data(address2, 0, [1, -1])
	time.sleep(5)
}

if __name__ == "__main__":
    main()