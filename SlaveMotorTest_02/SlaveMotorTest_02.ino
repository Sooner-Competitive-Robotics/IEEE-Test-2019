#include "RobotLib.h"
#include <Wire.h>
#include "IEEErobot2019.h"

enum State {Idle, Move};
State state;

int dataA, dataB, dataC, dataD = 0;


void setup()
{
	state = Idle;
	driveSetup();
	Wire.begin(10);
	Wire.setClock(100000);
	Wire.onReceive(testEvent);
}

void loop()
{
	if (state == Idle)
	{
		// Don't do anything
	}
	else if (state == Move)
	{
		drivetrain.setRPM(15);
		drivetrain.strafe(dataA, dataB, drivetrain.convertInchesToSteps(dataC));
		delay(drivetrain.calculateStepWait(drivetrain.convertInchesToSteps(dataC)));
		state = Idle;
	}
	
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
		int number = (int)Wire.read();

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
			break;
		}
		counter++;
	}
	dataA = byteA;
	dataB = byteB;
	dataC = byteC;
	dataD = byteD;
	
	state = Move;
}
