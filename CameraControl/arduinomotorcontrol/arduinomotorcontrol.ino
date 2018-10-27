int servoPin = 13;   // Servo signal pin connected to digital PWM pin 13
int inPin = 7;     // wifi module connected to digital pin 7
int servoPos = 0;       // variable to store the read value

void setup()
{
  pinMode(servoPin, OUTPUT);      // sets the digital pin 13 as output
  pinMode(inPin, INPUT);        // sets the digital pin 7 as input
}

void loop()
{
  servoPos = digitalRead(inPin);     // read the input pin
  digitalWrite(servoPin, servoPos);    // sets the servo position
}
