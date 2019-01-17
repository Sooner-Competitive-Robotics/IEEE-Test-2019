#include "RobotLib.h"
#include <Wire.h>
#include "IEEErobot2019.h"

void setup()
{
  Wire.begin(002);
  Wire.onRecieve(testEvent);
  
  robotSetup();
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
  
  drivetrain.step(byteA, byteA);
}
