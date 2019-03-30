import cv2
import imutils

# https://www.pyimagesearch.com/2016/02/01/opencv-center-of-contour/

# Returns -1 if object is to the left
#			0 if object is in the center
#			1 if object is to the right
#			-2 if object doesn't exist

	
def center(imagename):
	image = cv2.imread(imagename)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (5, 5), 0)
	thresh = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY)[1]
	cv2.imshow("blr", blurred)
	cv2.imshow("image", image)
	cv2.imshow("thresh", thresh)
	cv2.waitKey(0)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	
	cX = 0
	cY = 0
	
	for c in cnts:
		M = cv2.moments(c)
		
		if M["m00"] == 0:
			return -2
			
		cX = int(M["m10"] / M["m00"])
		cY = int(M["m01"] / M["m00"])
	
	# image dim
	width, height = image.shape[:2]
	
	# Get the x coord difference
	print("cX " + str(cX))
	diff = cX - width/2
	print(diff)
	
	#####################################################
	#    Use this value to change radius tolerance      #
	#####################################################
	CENTER_RANGE = 100
	
	if diff == 300 or diff == -300:
		return -2
	
	if diff > CENTER_RANGE:
		return 1
	elif diff < -CENTER_RANGE:
		return -1
	else:
		return 0


center("center.jpg")
