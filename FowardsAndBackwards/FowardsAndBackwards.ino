//#include <RobotLib.h>
#include "StepperMotorDrivetrain.h"

StepperMotorDrivetrain drivetrain;

void setup()
{
  //Initialize motors and basic drivetrain functions
  drivetrain.initBackRight(5, 4, 3, 2);
  drivetrain.initBackLeft(43, 42, 41, 40);
  drivetrain.initFrontRight(11, 10, 9, 8);
  drivetrain.initFrontLeft(50, 51, 52, 53);
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

