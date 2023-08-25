#include <Servo.h>

Servo x;
Servo y;
Servo z;
Servo e;
int button = 10;

int xval = 0;
int yval = 0;
int pos = 0;
int pos1 = 0;



void setup() {
  pinMode(button, INPUT);
  x.attach(6);
  y.attach(7);
  z.attach(8);
  e.attach(9);
  z.write(90);
  e.write(90);
  Serial.begin(9600);

}

void loop() {
  if (digitalRead(button) == LOW){
    z.write(180);
    e.write(0);
    delay(500);
    z.write(90);
    e.write(90);
    delay(50);
  }
  
  xval=analogRead(A1);
  pos=map(xval, 0, 1024, 0, 180);
  x.write(pos);
  delay(50);

  xval=analogRead(A2);
  pos1=map(xval, 0, 1024, 0, 180);
  y.write(pos1);
  delay(50);

}
