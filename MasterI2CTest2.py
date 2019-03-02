import smbus
import time

bus = smbus.SMBus(1)
address1 = 10
# address2 = 2


while True:	
	
	# distance in inches
	dist = 12
	
	# while !turn
	
	forward = 0
	turn = 1
	
	bus.write_i2c_block_data(address1, 0, [forward, turn, dist])
	
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
	

