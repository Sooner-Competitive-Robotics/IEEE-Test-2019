class NanoManager:
	
	# Calculate the amount of time the amount of steps will take
	def getWaitTime(self, steps):
		rpm = 15.0
		STEPS_PER_REVOLUTION = 200
		# Determine how many seconds we want to wait and convert to integer. 
		totalTime = float(steps / STEPS_PER_REVOLUTION) / rpm * 60
		T = (totalTime / steps) / 2
		return int(T) + 1
	
	# Calculate the number of steps needed to go x inches
	def convertInchesToSteps(self, inches):
		rpm = 15.0
		STEPS_PER_REVOLUTION = 200
		return int((STEPS_PER_REVOLUTION/(4*3.141592653589))*inches)

                
