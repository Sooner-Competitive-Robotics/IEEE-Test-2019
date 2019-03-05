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
	
	int byteA = 0;
	int byteB = 0;
  int byteC = 0;
	
  while(Wire.available()) {
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
  Serial.print(number);
  Serial.print(", ");
    
    counter++;
  }

  Serial.println();

  //Serial.print(drivetrain.convertInchesToSteps(byteC));
  
	drivetrain.strafe(byteA, byteB, drivetrain.convertInchesToSteps(byteC) * 10);

 delay(100);
}
