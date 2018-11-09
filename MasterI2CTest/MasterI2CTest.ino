#include <Wire.h>
//this is arbitrary; slaveAddress is dictated by user in slave's code
byte slaveAddress = 8;

//to send integer types of greater than 1 byte, need to use bitwise operations to send and receive
//Website for help on sending data:
//https://thewanderingengineer.com/2015/05/06/sending-16-bit-and-32-bit-numbers-with-arduino-i2c
//uint8_t ledState = 1;
uint8_t rpm = 25;
//uint8_t distance = 12;

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
}

void loop() {
  
  // put your main code here, to run repeatedly:
  Wire.beginTransmission(slaveAddress);
  //send RPM
  //Wire.write(ledState);
  Wire.write(rpm);
  //delay(100);
  //send distance
  //Wire.write(distance);
  Wire.endTransmission();
  delay(100);
  //while(true){};
}
