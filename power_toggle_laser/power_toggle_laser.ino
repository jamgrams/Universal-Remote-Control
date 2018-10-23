
#include <IRremote.h>
IRsend irsend;

void setup() {
  // put your setup code here, to run once:

Serial.begin(9600);   
}
 

void loop() {
  // put your main code here, to run repeatedly:

/*  0xFFA25D for power toggle laser   */ 
if (Serial.read() != -1){

irsend. sendNEC(0xFFA25D, 3);
Serial.println("Sent power toggle to laser");

}




}
