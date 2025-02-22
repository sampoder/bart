/* 
Structure is based on https://github.com/loopstick/ArduinoTutorial/blob/master/examples/06_RGB_LED/06a_RGB_Test/06a_RGB_Test.ino
*/

const int redLED_1 = 11;  
const int greenLED_1 = 9;  
const int blueLED_1 = 10;  

const int redLED_2 = 3;  
const int greenLED_2 = 6;  
const int blueLED_2 = 5; 

int delaytime = 100;

int delaytime_2 = 1000;
 
void setup(){
  pinMode(redLED_1, OUTPUT);
  pinMode(greenLED_1, OUTPUT);
  pinMode(blueLED_1, OUTPUT);
  pinMode(redLED_2, OUTPUT);
  pinMode(greenLED_2, OUTPUT);
  pinMode(blueLED_2, OUTPUT);
  Serial.begin(9600);
}

String incoming;

void loop(){
    if (Serial.available() > 0) {
      String read = Serial.readString();
      read.trim();
      if(!read.equals("")) {
        incoming = read;
      }
    }
    if(incoming.equals("RED")) {
      analogWrite(redLED_1, 255);
      analogWrite(greenLED_1, 0);
      analogWrite(blueLED_1, 0);
      analogWrite(redLED_2, 255);
      analogWrite(greenLED_2, 0);
      analogWrite(blueLED_2, 0);
      delay(delaytime);
    }

    if(incoming.equals("BLUE")) {
      analogWrite(redLED_1, 0);
      analogWrite(greenLED_1, 0);
      analogWrite(blueLED_1, 255);
      analogWrite(redLED_2, 0);
      analogWrite(greenLED_2, 0);
      analogWrite(blueLED_2, 255);
      delay(delaytime);
    }

    if(incoming.equals("GREEN")) {
      analogWrite(redLED_1, 0);
      analogWrite(greenLED_1, 255);
      analogWrite(blueLED_1, 0);
      analogWrite(redLED_2, 0);
      analogWrite(greenLED_2, 255);
      analogWrite(blueLED_2, 0);
      delay(delaytime);
    }

    if(incoming.equals("YELLOW")) {
      analogWrite(redLED_1, 255);
      analogWrite(greenLED_1, 70);
      analogWrite(blueLED_1, 0);
      analogWrite(redLED_2, 255);
      analogWrite(greenLED_2, 70);
      analogWrite(blueLED_2, 0);
      delay(delaytime);
    }

    if(incoming.equals("ORANGE")) {
      analogWrite(redLED_1, 255);
      analogWrite(greenLED_1, 20);
      analogWrite(blueLED_1, 0);
      analogWrite(redLED_2, 255);
      analogWrite(greenLED_2, 20);
      analogWrite(blueLED_2, 0);
      delay(delaytime);
    }

    if(incoming.equals("BLANK")) {
      analogWrite(redLED_1, 0);
      analogWrite(greenLED_1, 0);
      analogWrite(blueLED_1, 0);
      analogWrite(redLED_2, 0);
      analogWrite(greenLED_2, 0);
      analogWrite(blueLED_2, 0);
      delay(delaytime);
    }
}
