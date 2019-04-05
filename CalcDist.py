from imutils import paths
import numpy as np
import imutils
import cv2

# Finds focal lengths. Used for calibration
def findFocalLength(name, KNOWN_DISTANCE):
	#KNOWN_DISTANCE = 5
	KNOWN_WIDTH = 1.5
	image = cv2.imread(name)
	marker = find_marker(image)
	focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH

# Returns the image with distance	
def calcDist(name):
	KNOWN_WIDTH = 1.5
	FOCAL_LENGTH = 500
	
	image = cv2.imread(name)
	marker = find_marker(image)
	inches = dist2Cam(KNOWN_WIDTH, FOCAL_LENGTH, marker[1][0])
	return inches

# returns contour with largest area
def find_marker(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1] #optimal threshold 103
	edged = cv2.Canny(gray, 35, 125)
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key = cv2.contourArea)

	return cv2.minAreaRect(c)
	
# Calculates the distance
def dist2Cam(knownWidth, focalLength, perWidth):
	return knownWidth * focalLength / perWidth
	
if __name__ == '__main__':
	main()