
#include <Wire.h>
//Arbitrary
int slaveAddress = 8;
//int ledState;
boolean LS = 0;

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
  delay(50);
  if(LS){
    digitalWrite(7,HIGH);
    delay(100);
  }
  else{
    digitalWrite(7,LOW);
    delay(100);
  }
}

void LEDState(int numBytes){
  //TODO: figure out how to read in 2 bytes and convert into integer
  while(!Wire.available()){};
  uint8_t ledState = Wire.read();
  if(ledState == 1){
    LS = !LS;
  }
  else{
    LS = LS;
  }
}
