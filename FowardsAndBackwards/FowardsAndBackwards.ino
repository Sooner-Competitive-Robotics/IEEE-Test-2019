//#include <RobotLib.h>
#include "StepperMotorDrivetrain.h"
#include "IEEErobot2019.h"
bool turnDone = false;

void setup()
{
  Serial.begin(9600);
  //Initialize motors and basic drivetrain functions
  driveSetup();
}

void loop()
{
  drivetrain.step(drivetrain.convertInchesToSteps(12), drivetrain.convertInchesToSteps(12));
  delay(500);

  drivetrain.step(drivetrain.convertInchesToSteps(-12), drivetrain.convertInchesToSteps(-12));
  delay(500);

  while(true){};
}

