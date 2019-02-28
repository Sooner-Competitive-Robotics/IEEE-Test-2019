//#include <RobotLib.h>
#include "StepperMotorDrivetrain.h"
#include "IEEErobot2019.h"

bool turnDone = false;

void setup()
{
	//Wire.begin(001);
	//Wire.onRecieve(testEvent);
	
	//robotSetup();
	
	Serial.begin(9600);
	robotSetup();
}

void loop()
{
  gyroInterrupt();
	
	// Straight Left Strafe
	//drivetrain.setRPM(25);
	//drivetrain.strafe(1,0, drivetrain.convertInchesToSteps(36));
	//delay(500);
/*
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
	*/
}
/*
void testEvent()
{
	int counter = 0;
	
	int byteA = 0;
	int byteB = 0;
	
    while(Wire.available()) {
		int number = Wire.read();

        if (counter == 0){
			byteA = number;
        }

        if (counter == 1){
			byteB = number;
        }

        counter++;
    }
	
	drivetrain.strafe(byteB, byteC, drivetrain.convertInchesToSteps(byteA));
}
*/
