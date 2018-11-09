
#include <Wire.h>
//Arbitrary
int slaveAddress = 8;
//int ledState;

void setup() {
  // put your setup code here, to run once:
  
  pinMode(7,OUTPUT);

  digitalWrite(7,LOW);
  
  Wire.begin(8);
  Wire.onReceive(LEDState);
  //delay(100);
  //Wire.onReceive(receiveFreq);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(100);
  while(true);
}

void LEDState(int ledState){
  //TODO: figure out how to read in 2 bytes and convert into integer
  if(ledState == 1){
    digitalWrite(7,HIGH);
    delay(5000);
    digitalWrite(7,LOW);
  }  
}
