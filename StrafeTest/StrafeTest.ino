#include "RobotLib.h"
#include "StepperMotorDrivetrain.h"
#include "IEEErobot2019.h"

bool turnDone = false;

void setup()
{
	//Wire.begin(001);
	//Wire.onRecieve(testEvent);
	
	robotSetup();
	
	//Serial.begin(9600);
	//robotSetup();
}

void loop()
{
  //gyroInterrupt();

/*
  while (!turnDone)
  {
    updateGyro();
    turnDone = drivetrain.stepToAngle(90, GYRO_YAW);
  }
  Serial.println("Done");
  turnDone = false;
  resetGyro();
  delay(100);
 */ 

	// Straight Forwards Strafe
	drivetrain.setRPM(15);
	drivetrain.strafe(1, 0, drivetrain.convertInchesToSteps(12));
	delay(500);
	
	// Straight Backwards Strafe
	drivetrain.setRPM(15);
	drivetrain.strafe(-1, 0, drivetrain.convertInchesToSteps(12));
	delay(500);
	
	// Straight Right Strafe
	drivetrain.setRPM(15);
	drivetrain.strafe(0, 1, drivetrain.convertInchesToSteps(12));
	delay(500);
	
	// Straight Left Strafe
	drivetrain.setRPM(15);
	drivetrain.strafe(0, -1, drivetrain.convertInchesToSteps(12));
	delay(500);

	// Straight Forwards Left Strafe
	drivetrain.setRPM(15);
	drivetrain.strafe(1, -1, drivetrain.convertInchesToSteps(12));
	delay(500);

  // Straight Backwards Right Strafe
  drivetrain.setRPM(15);
  drivetrain.strafe(-1, 1, drivetrain.convertInchesToSteps(12));
  delay(500);

   // Straight Forwards Right Strafe
  drivetrain.setRPM(15);
  drivetrain.strafe(1, 1, drivetrain.convertInchesToSteps(12));
  delay(500);
  
	// Straight Backwards Left Strafe
	drivetrain.setRPM(15);
	drivetrain.strafe(-1, -1, drivetrain.convertInchesToSteps(12));
	delay(500);

	while(true){};  

}
