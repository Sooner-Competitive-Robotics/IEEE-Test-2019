#include "RobotLib.h"
#include "StepperMotorDrivetrain.h"
#include <Wire.h>
#include "IEEErobot2019.h"


void setup()
{
	robotSetup();
	//Serial.begin(9600);
	Wire.begin(10);
	Wire.setClock(100000);
	Wire.onReceive(testEvent);
}

void loop()
{
	
	delay(100);
}

void testEvent()
{
	drivetrain.setRPM(15);
	drivetrain.strafe(1, 0, drivetrain.convertInchesToSteps(12));
	//delay(500);
	// int counter = 0;
	
	// int byteA = 0; //strafe forward
	// int byteB = 0; //strafe sideways
  // int byteC = 0; // distance
	// int byteD = 0; // angle
  
  // while(Wire.available()>0) 
  // {
		// int number = (int)Wire.read();

    // //Serial.print("Values: ");

    // if (counter == 1){
	    // byteA = number;
    // }

    // if (counter == 2){
	    // byteB = number;
    // }

    // if (counter == 3){
      // byteC = number;
    // }

    // if (counter == 4){
      // byteD = number;
      // break;
    // }
    
    // //Serial.print(number);
    // //Serial.print(", ");
    
    // counter++;
  //}

  // //Serial.println();
    
  // //Serial.print(drivetrain.convertInchesToSteps(byteC));
  // drivetrain.setRPM(15);
  // drivetrain.strafe(byteA, byteB, drivetrain.convertInchesToSteps(byteC) * 10);
  
  // if (byteA != 0 && byteB == 0)
  // {
    // //mpu.calibrateGyro();
    
    // //smartDrive(byteC, 0); //0 angle? reset first?
  // }

  // delay(2000);
	

}
