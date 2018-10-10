//#include <RobotLib.h>
#include "StepperMotorDrivetrain.h"
bool turnDone = false;

StepperMotorDrivetrain drivetrain;


void setup()
{
  //Initialize motors and basic drivetrain functions
  drivetrain.initFrontLeft(2, 3, 4, 5);
  drivetrain.initFrontRight(40, 41, 42, 43);
  drivetrain.initBackLeft(8, 9, 10, 11);
  drivetrain.initBackRight(53, 52, 51, 50);
  drivetrain.setRPM(25);
}

void loop()
{
  drivetrain.step(drivetrain.convertInchesToSteps(120), drivetrain.convertInchesToSteps(120));
  delay(500);

  drivetrain.step(drivetrain.convertInchesToSteps(-120), drivetrain.convertInchesToSteps(-120));
  delay(500);

  while(true){};
}

