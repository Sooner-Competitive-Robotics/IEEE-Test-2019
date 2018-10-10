#include <RobotLib.h>

int pinStep = 0;
int pinDir = 0;
int pinEn = 0;

StepperMotor sm;

void setup() {
  // put your setup code here, to run once:
  sm.begin(pinStep, pinDir, pinEn);
  sm.setRPM(25);
}

void loop() {
  // put your main code here, to run repeatedly:
  sm.step(2000);
  delay(500);

  sm.step(-2000);
  delay(500);
}
