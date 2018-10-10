//#include <RobotLib.h>
#include "StepperMotorDrivetrain.h"

StepperMotorDrivetrain drivetrain;

void setup()
{
  Serial.begin(9600);
  //Initialize motors and basic drivetrain functions
  drivetrain.initBackRight(5, 4, 3, 2);
  drivetrain.initBackLeft(43, 42, 41, 40);
  drivetrain.initFrontRight(11, 10, 9, 8);
  drivetrain.initFrontLeft(50, 51, 52, 53);
  drivetrain.setRPM(25);
}

void loop()
{
  Serial.print("Code start");
  
  // Straight Left Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(0, -1, drivetrain.convertInchesToSteps(12));
  delay(500);

  Serial.print("Left Strafe finished");
  
   // Straight Right Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(0, 1, drivetrain.convertInchesToSteps(12));
  delay(500);

  Serial.print("Right Strafe finished");
  
   // Straight Forwards Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(1, 0, drivetrain.convertInchesToSteps(12));
  delay(500);

  Serial.print("Forwards finished");
   
   // Straight Backwards Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(-1, 0, drivetrain.convertInchesToSteps(12));
  delay(500);

  Serial.print("Backwards finished");
  
   // Straight Forwards Left Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(1, -1, drivetrain.convertInchesToSteps(12));
  delay(500);

  Serial.print("Diagnoal forward left finished");
  
   // Straight Forwards Right Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(1, 1, drivetrain.convertInchesToSteps(12));
  delay(500);

  Serial.print("Diagonal forward right finished");
  
   // Straight Backwards Left Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(-1, -1, drivetrain.convertInchesToSteps(12));
  delay(500);

  Serial.print("Diagonal backwards left");
  
   // Straight Backwards Right Strafe
  drivetrain.setRPM(25);
  drivetrain.strafe(-1, 1, drivetrain.convertInchesToSteps(12));
  delay(500);

  Serial.print("Diagonal backwards right");

  while(true){};

}

