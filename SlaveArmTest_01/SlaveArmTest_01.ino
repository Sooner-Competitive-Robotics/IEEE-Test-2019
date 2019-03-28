#include "RobotLib.h"
#include <Wire.h>
#include "IEEErobot2019.h"

enum State {Idle, armMove, clawMove, wristMove};
State state;

int dataA, dataB;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  state = Idle;
  armSetup();
  Wire.begin(20);
  Wire.setClock(100000);
  Wire.onReceive(testEvent);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (state == armMove)
  {
    arm.movePinion(dataB);
    delay(1500);
  }
  else if (state == clawMove)
  {
    arm.moveFist(dataB);
    delay(1500);
  }
  else if (state == wristMove)
  {
    arm.moveWrist(dataB);
    delay(1500);
  }
  else if (state == Idle){
    //don't do anything
  }
}

void testEvent()
{
  int counter = 0;

  int byteA = 0;
  int byteB = 0;

  while(Wire.available())
  {
    int number = (int)Wire.read();

    if (counter == 1) {
      byteA = number;
    }

    if (counter == 2) {
      byteB = number;
      break;
    }
    
    counter++;
  }
  dataA = byteA;
  dataB = byteB;

  Serial.println("A: " + dataA);
  Serial.println("B: " + dataB);

  if (dataA = 0) {
    state = Idle;
  }
  else if (dataA = 1) {
    state = armMove;
  }
  else if (dataA = 2) {
    state = clawMove;
  }
  else if (dataA = 3) {
    state = wristMove;
  }
}

