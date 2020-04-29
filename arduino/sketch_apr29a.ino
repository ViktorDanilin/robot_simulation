#include "ros.h"
#include <std_msgs/String.h>

#define HC12SetPin 40
String str;

class NewHardware : public ArduinoHardware {
  public: NewHardware(): ArduinoHardware(&Serial1, 115200) {}; //57600
};


ros::NodeHandle_<NewHardware>  nh;

std_msgs::String str_msg;


ros::Publisher chatter("chatter", &str_msg);

void setup() {
  nh.initNode();
  nh.advertise(chatter);
  pinMode(HC12SetPin, OUTPUT);
  Serial3.begin(9600);
  Serial1.println("Start HC-12 Config");
   digitalWrite(HC12SetPin, LOW); //перевели в режим приема АТ
   delay(500);

   Serial3.println ("AT"); // отправили на hc12
   Serial1.println ("AT"); // отправили себе
   delay(1000);
    if(Serial3.available() > 0)
   {
       str = Serial3.readStringUntil('\n');  // читаем ответ
       Serial1.println (str); // передаем его себе
   }
   str_msg.data = "step1";
  chatter.publish(&str_msg);
  nh.spinOnce();
   delay(500); // эти задержки важны для корректной работ

   Serial3.println ("AT+V"); // отправили на hc12
   Serial1.println ("AT+V"); // отправили себе
   delay(1000);
    if(Serial3.available() > 0)
   {
       str = Serial3.readStringUntil('\n');  // читаем ответ
       Serial1.println (str); // передаем его себе
   }
   str_msg.data = "step_2";
  chatter.publish(&str_msg);
  nh.spinOnce();
   delay(500); // эти задержки важны для корректной работ

   Serial3.println ("AT+DEFAULT"); // отправили на hc12
   Serial1.println ("AT+DEFAULT"); // отправили себе
   delay(1000);
    if(Serial3.available() > 0)
   {
       str = Serial3.readStringUntil('\n');  // читаем ответ
       Serial1.println (str); // передаем его себе
   }
   str_msg.data = "step_3";
  chatter.publish(&str_msg);
  nh.spinOnce();
   delay(500); // эти задержки важны для корректной работ

   Serial3.println ("AT+P8"); // отправили на hc12
   Serial1.println ("AT+P8"); // отправили себе
   delay(1000);
    if(Serial3.available() > 0)
   {
       str = Serial3.readStringUntil('\n');  // читаем ответ
       Serial1.println (str); // передаем его себе
   }
   str_msg.data = "step_4";
  chatter.publish(&str_msg);
  nh.spinOnce();
   delay(500); // эти задержки важны для корректной работ

   Serial3.println ("AT+C030"); // отправили на hc12
   Serial1.println ("AT+C030"); // отправили себе
   delay(1000);
    if(Serial3.available() > 0)
   {
       str = Serial3.readStringUntil('\n');  // читаем ответ
       Serial1.println (str); // передаем его себе
   }
   str_msg.data = "step_5";
  chatter.publish(&str_msg);
  nh.spinOnce();
   delay(500); // эти задержки важны для корректной работ

  
  
  Serial1.println("Save & Exit");
   digitalWrite(HC12SetPin, HIGH); //вернули в обычный режим
  // put your setup code here, to run once:
  str_msg.data = "GO";
  chatter.publish(&str_msg);
  nh.spinOnce();

}

void loop() {
  byte key[16] = {0xAA,0xFA,0x03,0x14,0x01,0x03,0x75, 0xCA, 0xAA,0xFA,0x03,0x14,0x01,0x03,0x75, 0xCA};

  str_msg.data = "ok";
  chatter.publish(&str_msg);
  nh.spinOnce();
  for (int kx = 0; kx < 16; kx ++) {
    Serial3.write(key[kx]); 
    //Serial3.print((byte)hexk.data[kx], (HEX));
  }
  Serial3.println(' ');
  Serial3.println(' '); 
  delay(5000);
  // put your main code here, to run repeatedly:

}
