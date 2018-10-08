#include <Servo.h>
#define pinNum 1

Servo clawServo;

void setup()
{
	clawServo.attach(pinNum);
}

void loop()
{
	// Grabbing
	for (int angle = 0; angle <= 180; angle++)
	{
		clawServo.write(angle);
		
		delay(15);
	}
	
	//Releasing
	for (int angle = 180; angle >= 0; angle--)
	{
		clawServo.write(angle);
		
		delay(15);
	}
	
	while (true) {};
}
