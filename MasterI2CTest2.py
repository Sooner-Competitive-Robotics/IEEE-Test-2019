import smbus
import time

bus = smbus.SMBus(1)
address1 = 10
# address2 = 2


while True:	
	
	# distance in inches
	dist = 12
	
	# while !turn
	
	forward = 1
	turn = 1
	
	strafe = 1
	# angle 1 for turning -90 to 90
	angle1 = 90
	
	# angle 2 for turning -180 to 180
	angle2 = 90
	
	#bus.write_i2c_block_data(address1, 0, [forward, strafe, turn, dist, angle1, angle2])
	bus.write_i2c_block_data(address1, 0, [forward, strafe, dist, angle1])
	#bus.write_i2c_block_data(address1, 0, [forward, strafe, turn, dist, angle1, angle2])
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
	
