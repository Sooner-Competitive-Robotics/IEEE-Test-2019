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

  // Straight Left Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(0, -1, drivetrain.convertInchesToSteps(36));
  delay(500);
  
  // Straight Right Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(0, 1, drivetrain.convertInchesToSteps(36));
  delay(500);

  // Straight Forwards Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(1, 0, drivetrain.convertInchesToSteps(36));
  delay(500);

  // Straight Backwards Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(-1, 0, drivetrain.convertInchesToSteps(36));
  delay(500);

  // Straight Forwards Left Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(1, -1, drivetrain.convertInchesToSteps(36));
  delay(500);

  // Straight Forwards Right Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(1, 1, drivetrain.convertInchesToSteps(36));
  delay(500);

  // Straight Backwards Left Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(-1, -1, drivetrain.convertInchesToSteps(36));
  delay(500);

  // Straight Backwards Right Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(-1, 1, drivetrain.convertInchesToSteps(36));
  delay(500);

  while(true){};

}

