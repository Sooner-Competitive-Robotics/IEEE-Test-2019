import smbus
import time
import startup
from vision import vision
from NanoManager import NanoManager
from gpiozero import Button
from picamera import PiCamera
import RPi.GPIO as GPIO

bus = smbus.SMBus(1)
address1 = 10
# address2 = 2

#start()
camera = PiCamera()
camera.resolution = (600, 600)
camera.rotation = 180

myvision = vision()
myNano = NanoManager()


def driveRobot(address, forward, strafe, dist):
    bus.write_i2c_block_data(address, 0, [forward, strafe, dist])
    waitTime = myNano.getWaitTime(myNano.convertInchesToSteps(dist))
    print("waiting: " + str(waitTime))
    time.sleep(waitTime)

driveRobot(address1, 1, 0, 12)
driveRobot(address1, 0, 1, 12)
driveRobot(address1, -1, 0, 12)
driveRobot(address1, 0, -1, 12)
