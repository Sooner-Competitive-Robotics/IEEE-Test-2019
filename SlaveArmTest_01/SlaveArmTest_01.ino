#include "RobotLib.h"
#include <Wire.h>
#include "IEEErobot2019.h"

// 120   
// 130 is facing down

enum State {Idle, armMove, clawMove, wristMove};
State state;

int dataA, dataB;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(11520);
  state = Idle;
  armSetup();
  arm.moveWrist(140);    // Default state of 0 dgs
  arm.moveFist(180);
  Wire.begin(20);
  Wire.setClock(100000);
  Wire.onReceive(testEvent);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (state == armMove)
  {
    Serial.println("moving pinion");
    arm.movePinion(dataB);
    state = Idle;
  }
  else if (state == clawMove)
  {
    Serial.println("moving claw");
    arm.moveFist(dataB);
    state = Idle;
  }
  else if (state == wristMove)
  {
    Serial.print("moving wrist");
    arm.moveWrist(dataB);
    state = Idle;
  }
  else if (state == Idle){
    //don't do anything
  }
  delay(10);
}

void testEvent()
{
  int counter = 0;

  int byteA = 0;
  int byteB = 0;

  while(Wire.available())
  {
    int number = (int)Wire.read();
    Serial.println(number);

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

  if (dataA == 0) {
    state = Idle;
  }
  else if (dataA == 1) {
    state = armMove;
  }
  else if (dataA == 2) {
    state = clawMove;
  }
  else if (dataA == 3) {
    state = wristMove;
  }
}

