//#include <RobotLib.h>
#include "StepperMotorDrivetrain.h"
bool turnDone = false;

StepperMotorDrivetrain drivetrain;


void setup()
{
  //Initialize motors and basic drivetrain functions
  //TODO: Specify pins, right now they're based on last year
  //drivetrain.initLeft(16, 15, 25, 24);
  //drivetrain.initRight(10, 11, 8, 7);
  drivetrain.setRPM(25);
}

void loop()
{
  // Straight Left Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(0, 1, drivetrain.convertInchesToSteps(12));
  delay(500);

  while(true){};
}

