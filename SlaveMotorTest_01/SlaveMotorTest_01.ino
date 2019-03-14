#include "RobotLib.h"
#include <Wire.h>
#include "IEEErobot2019.h"

void setup()
{
	robotSetup();

 Serial.begin(9600);

	Wire.begin(10);
	Wire.onReceive(testEvent);
	
}

void loop()
{
	delay(100);
}

void testEvent()
{
	int counter = 0;
	
	int byteA = 0; //strafe forward
	int byteB = 0; //strafe sideways
  int byteC = 0; // distance
	int byteD = 0; // angle
  
  while(Wire.available()) 
  {
		int number = Wire.read();

    Serial.print("Values: ");

    if (counter == 1){
	    byteA = number;
    }

    if (counter == 2){
	    byteB = number;
    }

    if (counter == 3){
      byteC = number;
    }

    if (counter == 4){
      byteD = number;
    }
    
    Serial.print(number);
    Serial.print(", ");
    
    counter++;
  }

  Serial.println();

  //Serial.print(drivetrain.convertInchesToSteps(byteC));
  
  if (byteA != 0 && byteB == 0)
  {
    mpu.calibrateGyro();
    
    smartDrive(byteC, 0); //0 angle? reset first?
  }

	//drivetrain.strafe(byteA, byteB, drivetrain.convertInchesToSteps(byteC) * 10);

  delay(100);
}
