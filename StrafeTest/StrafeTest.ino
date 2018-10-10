//#include <RobotLib.h>
#include "StepperMotorDrivetrain.h"

bool turnDone = false;

StepperMotorDrivetrain drivetrain;


void setup()
{
  Serial.begin(9600);
  //Initialize motors and basic drivetrain functions
  drivetrain.initFrontLeft(2, 3, 4, 5);
  drivetrain.initFrontRight(40, 41, 42, 43);
  drivetrain.initBackLeft(8, 9, 10, 11);
  drivetrain.initBackRight(53, 52, 51, 50);
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

