class NanoManager:
	
	# Calculate the amount of time the amount of steps will take
	def getWaitTime(self, steps):
                rpm = 15.0
                STEPS_PER_REVOLUTION = 200
                return int(steps/200*(15/rpm)*3) + 2
	
	# Calculate the number of steps needed to go x inches
	def convertInchesToSteps(self, inches):
		rpm = 15.0
		STEPS_PER_REVOLUTION = 200
		return int((STEPS_PER_REVOLUTION/(4*3.141592653589))*inches*1.04)
