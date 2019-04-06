import smbus
import time
import startup
import math
import RPi.GPIO as GPIO
from vision import vision
from gpiozero import Button
from picamera import PiCamera
import jsonread
import copyjson
from NanoManager import NanoManager
import os
import sys

# IEEE competition code

address1 = 10                                           # Address to the drive nano
address2 = 20                                           # Address to the arm nano

BUTTON_PIN = 14
GREEN_LED_PIN = 18
RED_LED_PIN = 15

bus = smbus.SMBus(1)
camera = PiCamera()
camera.resolution = (600, 600)
camera.rotation = 180

myvision = vision()
myNano = NanoManager()

movedLeft = 0
movedRight = 0
movedBack = 0

distance = 0

# List of info to send. Format is [forward, side, distance]
#data = []cd
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.OUT)on
GPIO.output(GREEN_LED_PIN, GPIO.LOW)
GPIO.output(RED_LED_PIN, GPIO.LOW)

while True:
        print('begin')
		
        while True:
                start = GPIO.input(BUTTON_PIN)
                if start == True:
                        break;
        
	myNano.driveRobot(address1, 1, 0, 12)
	myNano.driveRobot(address1, -1, 0, 12)
	GPIO.output(RED_LED_PIN, GPIO.HIGH)
        time.sleep(10000)
        
