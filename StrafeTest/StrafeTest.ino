//#include <RobotLib.h>
#include "StepperMotorDrivetrain.h"
#include "IEEErobot2019.h"

bool turnDone = false;

void setup()
{
  Serial.begin(9600);
  robotSetup();
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

