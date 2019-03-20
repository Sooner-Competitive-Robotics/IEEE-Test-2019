class NanoManager:
	
	rpm = 15.0
	STEPS_PER_REVOLUTION = 200
	
	# Calculate the amount of time the amount of steps will take
	def getWaitTime(steps):
		# Determine how many seconds we want to wait and convert to integer. 
		totalTime = float(steps / STEPS_PER_REVOLUTION) / rpm * 60 * 1000
		T = (totalTime / steps) / 2
		return T
	
	# Calculate the number of steps needed to go x inches
	def convertInchesToSteps(float inches)
		return int(STEPS_PER_REVOLUTION/(4*3.141592653589))*inches);
