import pytesseract
import cv2
import random
import LetterRecognition
import ShapeDetection
import Centerpoint

#This class contains static methods for analyzing pictures for object recognition.
class vision:

	def getLetter(image):
		return LetterRecognition.findImage(image)

	def isCube(image):
		return ShapeDetection.findShape(image)

	def getCenter(image):
		return Centerpoint.center(image)

	#def 
