#include <Arduino.h>
#include <Servo.h>
#include <ros.h>
#include <std_msgs/UInt16.h>
#include <std_msgs/UInt32.h>
#include<AccelStepper.h>
#define HALFSTEP 8

#define POWER_manipul 9
#define DIRECTION_manipul 8
#define front_end_switch 7
#define back_end_switch  6
#define motorPin1  10 // IN1 на 1-м драйвере ULN2003
#define motorPin2  11 // IN2 на 1-м драйвере ULN2003
#define motorPin3  12 // IN3 на 1-м драйвере ULN2003
#define motorPin4  13 // IN4 на 1-м драйвере ULN2003


AccelStepper stepper(HALFSTEP, motorPin1, motorPin3, motorPin2, motorPin4);

Servo servo44; //big
Servo servo45; //small

class NewHardware : public ArduinoHardware
{
  public:
    NewHardware():
      ArduinoHardware(&Serial1, 115200) {};
};



ros::NodeHandle  servos;          ///arduino/servo1    /arduino/servo2   Int16    /motor  Int32


void s1(const std_msgs::UInt16& cmd_msg) { // Первая серва
  servo44.write(cmd_msg.data);
}

void s2(const std_msgs::UInt16& cmd_msg) { // Вторая серва
  servo45.write(cmd_msg.data);
}

void motorRotation1(const std_msgs::UInt32& cmd_msg2) { // Мотор врашение манипулятором
  if (cmd_msg2.data == 2) { // В лево
    analogWrite(POWER_manipul, 130);
    digitalWrite(DIRECTION_manipul, LOW);
  }
  else if (cmd_msg2.data == 1) { // В право
    analogWrite(POWER_manipul, 130);
    digitalWrite(DIRECTION_manipul, HIGH);
  }
  else { // Стоп
    analogWrite(POWER_manipul, 255);
    digitalWrite(DIRECTION_manipul, HIGH);
  }
}


bool startMotorRotation2 = false;
const int speeds = 70;
int speedMotorRotation2 = speeds;

void motorRotation2(const std_msgs::UInt32& cmd_msg2) { // шаговик
  if (cmd_msg2.data == 2) {
    startMotorRotation2 = false;
  }
  else if (cmd_msg2.data == 0) {
    startMotorRotation2 = true;
    speedMotorRotation2 = speeds * -1;
    stepper.setSpeed(speedMotorRotation2);
  }
  else {
    startMotorRotation2 = true;
    speedMotorRotation2 = speeds * -1;
    stepper.setSpeed(speedMotorRotation2);
  }
}

ros::Subscriber<std_msgs::UInt16> subs1("/arduino/servo1", s1);
ros::Subscriber<std_msgs::UInt16> subs2("/arduino/servo2", s2);
ros::Subscriber<std_msgs::UInt32> subs3("/arduino/motor1", motorRotation1);
ros::Subscriber<std_msgs::UInt32> subs4("/arduino/slider", motorRotation2); // шаговик



void setup() {
  pinMode(POWER_manipul, OUTPUT);
  pinMode(DIRECTION_manipul, OUTPUT);
  analogWrite(POWER_manipul, 255);
  digitalWrite(DIRECTION_manipul, HIGH);
  servo44.attach(44);
  servo45.attach(45);
  servos.initNode();
  pinMode(front_end_switch, INPUT_PULLUP);
  pinMode(back_end_switch, INPUT_PULLUP);
  stepper.setMaxSpeed(1000);
  stepper.setSpeed(50);
  servos.subscribe(subs1);
  servos.subscribe(subs2);
  servos.subscribe(subs3);
  servos.subscribe(subs4);
}


void loop() {
  servos.spinOnce();
  if (startMotorRotation2) {
    stepper.runSpeed();
    if (speedMotorRotation2 < 0) {
      if (digitalRead(back_end_switch) == 0) {
        stepper.stop();
        startMotorRotation2 = false;
      }
    }
    else {
      if (digitalRead(front_end_switch) == 0) {
        stepper.stop();
        startMotorRotation2 = false;
      }
    }
  }
  else {
    stepper.stop();
  }
  delay(1);
}
