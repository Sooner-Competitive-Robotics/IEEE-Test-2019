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

VIEWING_ANGLE = 150

bus = smbus.SMBus(1)
camera = PiCamera()
camera.resolution = (600, 600)
camera.rotation = 180

myvision = vision()
myNano = NanoManager()

movedLeft = 0
movedRight = 0
movedBack = 0
found_cube = True
back_counter = 0
distance = 0

# List of info to send. Format is [forward, side, distance]
#data = []cd
GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.OUT)
GPIO.output(GREEN_LED_PIN, GPIO.LOW)
GPIO.output(RED_LED_PIN, GPIO.LOW)

# Forwards and Backwards
while True:
        start = GPIO.input(BUTTON_PIN)
        if start == True:
                break;
        
myNano.driveRobot(address1, 1, 0, 12, 0)
myNano.driveRobot(address1, -1, 0, 12, 0)
GPIO.output(RED_LED_PIN, GPIO.HIGH)
time.sleep(10000)

while True:
        print('begin')

        #check if file is in location
        #if true, proceed to round code (and button)
        #if not, run through jsonread
        
        if not os.path.isfile("/home/pi/locations/mars1.json"):
                copy = False
                while (not copy):
                        copy = copyjson.copyjson()
                        print('copied')
                        GPIO.output(GREEN_LED_PIN, GPIO.HIGH)
                        time.sleep(3)
                        print('green led')
                        sys.exit(0)
                        print('you shouldnt be seeing this')
        
        # button pressed = round code starting
        while True:
                start = GPIO.input(BUTTON_PIN)
                if start == True:
                        break;
        
        # Get JSON file location
        data = jsonread.jsonread()
        
        if (data == 0):
                myNano.driveRobot(address1, 1, 0, 12, 0)
                myNano.driveRobot(address1, -1, 0, 12, 0)
                GPIO.output(RED_LED_PIN, GPIO.HIGH)
                time.sleep(10000)
        
        # If for some reason json is empty just go forwards and backwards
        #if len(data) <= 0:
                #myNano.driveRobot(address1, 1, 0, 12, 0)
                #myNano.driveRobot(address1, -1, 0, 12, 0)
                #GPIO.output(RED_LED_PIN, GPIO.HIGH)
                #time.sleep(10000)
        size = data["size"]
        # no way block is at 4,4 (starting location of robot)
        # no way closest block is 5 feet away
        minDist = 5 # feet
        minX = 4
        minY = 4
        
        fuck = False
        while (size > 0):
                if (data["y coords"][size - 1] > 4):
                        fuck = True
                size = size - 1

        size = data["size"]
        # interates through all coordinates and finds minimum distance and at what coordinates
        while (size > 0):
                print(size)
                print("\n")
                dist = abs(math.sqrt(math.pow((data["x coords"][size - 1] - 4), 2)+math.pow((data["y coords"][size - 1] - 4), 2)))

                #if all cubes are behind bot and there's one cube on the same x coordinate as robot, then just do forwards and backwards
                if (data["x coords"][size - 1] == 4 and data["y coords"][size - 1] <= 4 and not fuck):
                        myNano.driveRobot(address1, 1, 0, 12, 0)
                        myNano.driveRobot(address1, -1, 0, 12, 0)
                        GPIO.output(RED_LED_PIN, GPIO.HIGH)
                        os.remove("/home/pi/locations/mars1.json")
                        time.sleep(100000)
                  
                if (not (data["y coords"][size - 1] <= 1) and not (data["x coords"][size - 1] == 4 and data["y coords"][size - 1] <= 4)):
                        if (dist < minDist):
                                minX = data["x coords"][size - 1]
                                minY = data["y coords"][size - 1]
                                minDist = dist
                size = size - 1
        
        print("MinX:", minX)
        print("\n")
        print("MinY:", minY)
        print("\n")
        
        # Drive to one location
                # if y coordinate is < 4 turn 180, > 4 nothing, = 4 turn 90 or -90 depending on x coor
                # if x coordinate is < 4 strafe left, > 4 strafe right, else nothing
                # stop one block away from actual location maybe?
        
        #drive up to cube 
        # if y != 4, drive (abs(y coord - 4ft) - 1 ft)
        # if y == 4, drive (abs(x coord - 4ft) - 1 ft)
        #if (minY == 4):
        #        if (minX < 4):
        #                #turn -90
        #                myNano.driveRobot(address1, 0, 0, 0, -90)
        #        else:
        #                #turn 90
        #                myNano.driveRobot(address1, 0, 0, 0, 90)

        #        #drive to cube
        #        dist = 12*(minX - 4 - 1)
        #        myNano.driveRobot(1, 0, dist, 0)
        
        if (minY > 4):
                dist = 12*abs(minX - 4)
                if (minX < 4):
                        #strafe left
                        myNano.driveRobot(address1, 0, -1, dist, 0)
                elif (minX > 4):
                        # strafe right
                        myNano.driveRobot(address1, 0, 1, dist, 0)
                dist = 12*(minY - 4 - 1)
                print(str(dist))
                myNano.driveRobot(address1, 1, 0, 12, 0)
        elif (minY <= 4):
                #drive back
                myNano.driveRobot(address1, -1, 0, 12*(4 - minY + 1), 0)
                                #myNano.driveRobot(address1, 0, 0, 0, 90)
                #myNano.driveRobot(address1, 0, 0, 0, 90)
                dist = 12*abs(minX - 4)
                print(dist);
                if (minX < 4):
                        #strafe left 
                        myNano.driveRobot(address1, 0, -1, dist, 0)
                elif (minX > 4):
                        #strafe right
                        myNano.driveRobot(address1, 0, 1, dist, 0)
                                                
                #dist = 12*(minY - 4 - 1)
                #myNano.driveRobot(address1, 1, 0, dist, 0)
                
        # optimal angle for looking for cube
        myNano.moveArm(address2, 3, VIEWING_ANGLE)
        # Align to the cube
        while True:
                camera.capture("center.jpg")
                
                
                center = myvision.getCenter("center.jpg");
                
                # Cube is to the right
                if (center == 1):
                        myNano.driveRobot(address1, 0, 1, 2, 0)
                        movedRight += 1
                # Cube is to the left
                elif (center == -1):
                        myNano.driveRobot(address1, 0, -1, 2, 0)
                        movedLeft += 1
                elif (center == -2):
                        print("Block not found")
                        print(back_counter)
                        if back_counter >1:
                                found_cube = False
                                break
                        myNano.driveRobot(address1, -1, 0, 3, 0)
                        movedBack += 1
                        back_counter = back_counter + 1
                # Cube is centered. Move forward to pick cube up.
                else:
                        #distance = myvision.getDist2Cube("center.jpg")
                        myNano.moveArm(address2, 3, 60)
                        #print("distance to cube: " + str(distance))
                        myNano.driveRobot(address1, 1, 0, 12, 0)
                        
                        # Move arm and pick it up
                        break;
                        
        # pick up block
        myNano.moveArm(address2, 2, 0)
        myNano.moveArm(address2, 3, VIEWING_ANGLE)

        while(movedRight != 0):
                myNano.driveRobot(address1, 0, -1, 2, 0)
                movedRight -= 1
        while(movedLeft != 0):
                myNano.driveRobot(address1, 0, 1, 2, 0)
                movedLeft -= 1
        while(movedBack != 0):
                myNano.driveRobot(address1, 1, 0, 3, 0)
                movedBack -= 1

        if found_cube:
                myNano.driveRobot(address1, -1, 0, 12, 0)
        #myNano.driveRobot(address1, 0, 0, 0, 90)
        #myNano.driveRobot(address1, 0, 0, 0, 90)

        # return to start by using the same movements as before
        #if (minY == 4):
        #        dist = 12*(minX - 4 - 1)
        #        myNano.driveRobot(-1, 0, dist)
        if (minY > 4):
                dist = 12*abs(minX - 4)
                if (minX < 4):
                        #strafe right
                        myNano.driveRobot(address1, 0, 1, dist, 0)
                elif (minX > 4):
                        # strafe left
                        myNano.driveRobot(address1, 0, -1, dist, 0)
                dist = 12*(minY - 4 - 1)
                print(str(dist))
                myNano.driveRobot(address1, -1, 0, 12, 0)
        elif (minY <= 4):
                dist = 12*abs(minX - 4)
                if (minX < 4):
                        #strafe right
                        myNano.driveRobot(address1, 0, 1, dist, 0)
                elif (minX > 4):
                        #strafe left
                        myNano.driveRobot(address1, 0, -1, dist, 0)
                dist = 12*(abs(minY - 4) + 1)
                print(dist)
                myNano.driveRobot(address1, 1, 0, dist, 0)
                myNano.moveArm(address2, 2, 180)
                myNano.moveArm(address2, 3, 70)


        #end of code, delete json file
        #os.remove("/home/pi/locations/mars1.json")

        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        time.sleep(10000)
        
        #repeat code for remaining cubes
        
