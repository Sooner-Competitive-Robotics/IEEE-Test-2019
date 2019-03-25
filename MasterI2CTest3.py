import smbus
import time
import startup
from vision import vision
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

print("First data incoming")
bus.write_i2c_block_data(address1, 0, [0 ,1, 12])
print("First data sent. sleeping for 10s")
time.sleep(10)
print("Second data incoming")
bus.write_i2c_block_data(address1, 0, [1, 0, 12])
print("Second data sent. sleeping for 4s")
time.sleep(4)
