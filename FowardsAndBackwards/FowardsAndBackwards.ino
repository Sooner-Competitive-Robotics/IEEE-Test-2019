//#include <RobotLib.h>
#include "StepperMotorDrivetrain.h"
bool turnDone = false;

StepperMotorDrivetrain drivetrain;


void setup()
{
  Serial.begin(9600);
  //Initialize motors and basic drivetrain functions
  drivetrain.initFrontLeft(2, 3, 4, 5);
  drivetrain.initFrontRight(33, 32, 31, 30);
  drivetrain.initBackLeft(8, 9, 10, 11);
  drivetrain.initBackRight(53, 52, 51, 50);
  drivetrain.setRPM(25);
}

void loop()
{
  drivetrain.step(drivetrain.convertInchesToSteps(12), drivetrain.convertInchesToSteps(12));
  delay(500);

  drivetrain.step(drivetrain.convertInchesToSteps(-12), drivetrain.convertInchesToSteps(-12));
  delay(500);

  while(true){};
}

