import smbus
import time
import startup
import math
import RPi.GPIO as GPIO
from vision import vision
from gpiozero import Button
from picamera import PiCamera
import jsonread
#import copyjson
from NanoManager import NanoManager

# IEEE competition code

address1 = 10                                           # Address to the drive nano
address2 = 20                                           # Address to the arm nano

bus = smbus.SMBus(1)
camera = PiCamera()
camera.resolution = (600, 600)
camera.rotation = 180

myvision = vision()
myNano = NanoManager()

movedLeft = 0;
movedRight = 0;
movedBack = 0;

# List of info to send. Format is [forward, side, distance]
#data = []cd

while True:
        print('begin')
        
        # Get JSON file location
        data = jsonread.jsonread()
        size = data["size"]
        # no way block is at 4,4 (starting location of robot)
        # no way closest block is 5 feet away
        minDist = 5 # feet
        minX = 4
        minY = 4

        # interates through all coordinates and finds minimum distance and at what coordinates
        while (size > 0):
                print(size)
                print("\n")
                dist = abs(math.sqrt(math.pow((data["x coords"][size - 1] - 4), 2)+math.pow((data["y coords"][size - 1] - 4), 2)))
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
        if (minY == 4):
                if (minX < 4):
                        #turn -90
                        myNano.driveRobot(address1, 0, 0, 0, -90)
                        #driveRobot(address1, data)
                else:
                        #turn 90
                        myNano.driveRobot(address1, 0, 0, 0, 90)
                        #driveRobot(address1, data)

                #drive to cube
                dist = 12*(minX - 4 - 1)
                myNano.driveRobot(1, 0, dist)
        elif (minY > 4):
                dist = 12*abs(minX - 4)
                if (minX < 4):
                        #strafe left
                        myNano.driveRobot(address1, 0, -1, dist)
                        #driveRobot(address1, data)
                elif (minX > 4):
                        # strafe right
                        myNano.driveRobot(address1, 0, 1, dist)
                        #driveRobot(address1, data)
                dist = 12*(minY - 4 - 1)
                print(str(dist))
                myNano.driveRobot(address1, 1, 0, 12)
                #driveRobot(address1, data)
        elif (minY < 4):
                #turn 180
                #myNano.driveRobot(address1, 0, 0, 0, 90)
                #driveRobot(address1, data)
                #myNano.driveRobot(address1, 0, 0, 0, 90)
                #driveRobot(address1, data)
                dist = 12*abs(minX - 4)
                print(dist);
                if (minX < 4):
                        #strafe right (reverse because we turned 180)
                        myNano.driveRobot(address1, 0, 1, dist)
                        #driveRobot(address1, data)
                elif (minX > 4):
                        #strafe left
                        myNano.driveRobot(address1, 0, -1, dist)
                        #driveRobot(address1, data)
                dist = 12*(minY - 4 - 1)
                myNano.driveRobot(address1, 1, 0, dist)
                #driveRobot(address1, data)
                
        # optimal angle for looking for cube
        #myNano.moveArm(address2, 3, 120)
                
        # Align to the cube
        while True:
                camera.capture("center.jpg")
                
                center = myvision.getCenter("center.jpg");
                
                # Cube is to the right
                if (center == 1):
                        myNano.driveRobot(address1, 0, 1, 1)
                # Cube is to the left
                elif (center == -1):
                        myNano.driveRobot(address1, 0, -1, 1)
                elif (center == -2):
                        print("Block not found")
                        myNano.driveRobot(address1, -1, 0, 1)
                # Cube is centered. Move forward to pick cube up.
                else:
                        myNano.driveRobot(address1, 1, 0, 12)
                        #driveRobot(address1, data)
                        # Move arm and pick it up
                        break;
                        
        # pick up block

        myNano.moveArm(address2, 3, 60)
        myNano.moveArm(address2, 2, 0)
        myNano.moveArm(address2, 3, 160)
        
        myNano.moveArm(address2, 2, 180)

        myNano.driveRobot(address1, -1, 0, 12)
        #myNano.driveRobot(address1, 0, 0, 0, 90)
        #myNano.driveRobot(address1, 0, 0, 0, 90)

        # return to start by using the same movements as before
        if (minY == 4):
                dist = 12*(minX - 4 - 1)
                myNano.driveRobot(-1, 0, dist)
        elif (minY > 4):
                dist = 12*abs(minX - 4)
                if (minX < 4):
                        #strafe right
                        myNano.driveRobot(address1, 0, 1, dist)
                        #driveRobot(address1, data)
                elif (minX > 4):
                        # strafe left
                        myNano.driveRobot(address1, 0, -1, dist)
                        #driveRobot(address1, data)
                dist = 12*(minY - 4 - 1)
                print(str(dist))
                myNano.driveRobot(address1, -1, 0, 12)
                #driveRobot(address1, data)
        elif (minY < 4):
                dist = 12*abs(minX - 4)
                print(dist);
                if (minX < 4):
                        #strafe left (reverse because we turned 180)
                        myNano.driveRobot(address1, 0, -1, dist)
                        #driveRobot(address1, data)
                elif (minX > 4):
                        #strafe right
                        myNano.driveRobot(address1, 0, 1, dist)
                        #driveRobot(address1, data)
                dist = 12*(minY - 4 - 1)
                myNano.driveRobot(address1, -1, 0, dist)
                #driveRobot(address1, data)
        

        time.sleep(10000)
        
        #repeat code for remaining cubes
        
