#include "StepperMotorDrivetrain.h"
#include <Wire.h>
//Arbitrary
int slaveAddress = 8;

StepperMotorDrivetrain drivetrain;

void setup() {
  // put your setup code here, to run once:
  Wire.begin(8);
  Wire.onReceive(receiveRPM);
  delay(100);
  Wire.onReceive(receiveDistance);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(100);
  while(true);
}

void receiveRPM(int data){
  //TODO: figure out how to read in 2 bytes and convert into integer
  drivetrain.setRPM(data);
}

void receiveDistance(int data){
  //TODO: figure out how to read in 2 bytes and convert into integer
  drivetrain.step(drivetrain.convertInchesToSteps(data), drivetrain.convertInchesToSteps(data));
}
