#include "ros.h"
#include <std_msgs/String.h>
#include <SoftwareSerial.h> 

#define HC12SetPin 40
SoftwareSerial HC12(14, 15); 
ros::NodeHandle nh;

std_msgs::String str_msg;
ros::Publisher chatter("chatter", &str_msg);

void setup() {
  HC12.begin(9600);
  nh.getHardware()->setBaud(9600);
  nh.initNode();
  nh.advertise(chatter);
  digitalWrite(HC12SetPin, LOW); 
}



void loop() {
  //Serial1.println("Start HC-12 Config");

  //digitalWrite(HC12SetPin, LOW); //перевели в режим приема АТ
  //delay(500);

  HC12.print("AT");
  //Serial1.println ("AT"); // отправили себе
  //delay(1000);

  if (HC12.available() > 0)
  {
    str_msg.data = HC12.read();  // читаем ответ
    delay(100);
    chatter.publish( &str_msg);
    nh.spinOnce();
  }
  //delay(500); // эти задержки важны для корректной работы
  //Serial1.println("Save & Exit");
  //digitalWrite(HC12SetPin, HIGH); //вернули в обычный режим
}
