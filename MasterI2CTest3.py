import smbus
import time
import startup
import vision

bus = smbus.SMBus(1)
address1 = 10
# address2 = 2

#start()
camera = PiCamera()
camera.resolution = (600, 600)
camera.rotation = 180

while True:	
	
	print('begin')
	
	while (True):
		camera.capture("CameraPictures/center.jpg")
		
		if (center("CameraPictures/center.jpg") == 1):
			bus.write_i2c_bloc_data(address1, 0, [0, 1, 0, 1, 0, 0])
		elif (center("CameraPictures/center.jpg") == -1):
			bus.write_i2c_bloc_data(address1, 0, [0, -1, 0, 1, 0, 0])
		else:
			break
		
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
	angle2 = 0
	
	bus.write_i2c_block_data(address1, 0, [forward, strafe, turn, dist, angle1, angle2])
	
	
	
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