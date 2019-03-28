import smbus
import math

class NanoManager:
	
	# Calculate the amount of time the amount of steps will take
	def getWaitTime(self, steps):
                rpm = 15.0
                STEPS_PER_REVOLUTION = 200
                return int(steps/200*(15/rpm)*3) + 2
	
	# Calculate the number of steps needed to go x inches
	def convertInchesToSteps(self, inches):
		STEPS_PER_REVOLUTION = 200
		return int((STEPS_PER_REVOLUTION/(4*math.pi))*inches*1.04)
		
	def driveRobot(address, forward, strafe, distance, angle):
		bus = smbus.SMBus(1)
		bus.write_i2c_block_data(address, 0, [forward, strafe, dist])
		waitTime = myNano.getWaitTime(myNano.convertInchesToSteps(dist))
		print("waiting: " + str(waitTime))
		time.sleep(waitTime)
		
	def moveArm(address, state, angle):
		bus.write_i2c_block_data(address, 0, [state, angle])
		print("waiting: 1")
		time.sleep(1)
    