import smbus
import time

bus = smbus.SMBus(1)
address1 = 001
# address2 = 002


while True:	
	
	# distance in inches
	dist = 12
	
	# while !turn
	
	dist1 = 0;
	dist2 = 1;
	
	bus.write_i2c_block_data(address1, 0, 12, dist1, dist2)
	
	time.sleep(500);

# turn method
# def turn (target, current, 
	
# Method 1
	# At JSON file location
	
	# Take picture
	
	# Locate block using distance and height calculations
	
	# Adjust robot to block
	
	# Pick block up
	

