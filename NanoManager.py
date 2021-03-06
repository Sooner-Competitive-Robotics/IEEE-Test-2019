import smbus
import math
import time

class NanoManager:
	
	# Calculate the amount of time the amount of steps will take
	def getWaitTime(self, steps):
                rpm = 15.0
                STEPS_PER_REVOLUTION = 200
                return abs(int(steps/200*(15/rpm)*4)) + 2
	
	# Calculate the number of steps needed to go x inches
	def convertInchesToSteps(self, inches):
		STEPS_PER_REVOLUTION = 200
		return int((STEPS_PER_REVOLUTION/(4*math.pi))*inches*1.04)

	def driveRobot(self, address, forward, strafe, dist, angle):
                bus = smbus.SMBus(1)
                bus.write_i2c_block_data(address, 0, [forward, strafe, dist, angle])
                if dist == 0:
                        waitTime = 3
                else:
                        waitTime = NanoManager.getWaitTime(NanoManager, NanoManager.convertInchesToSteps(NanoManager, dist))
                print("waiting: " + str(waitTime))
                time.sleep(waitTime)

	# fist: 0 closed, 180 open
	def moveArm(self, address, state, angle):
                bus = smbus.SMBus(1)
                bus.write_i2c_block_data(address, 0, [state, angle])
                print("waiting: 1")
                time.sleep(1)
    
