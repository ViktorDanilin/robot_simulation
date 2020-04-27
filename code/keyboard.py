#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from pynput.keyboard import Key, Listener, KeyCode, Key
from geometry_msgs.msg import Twist
from std_msgs.msg import Int16
import time
forvard = 3
back = -3
right = -2
left = 2
    # Функция считываеия с клавиатуры

def main(self, key):

    rospy.init_node("joystick", anonymous=True)
    pub1 = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    vel_msg = Twist()
    pub2 = rospy.Publisher("/arduino/servo1", Int16, queue_size=10)  # servo up/down
    serv_msg = Int16
    pub3 = rospy.Publisher("/arduino/servo2", Int16, queue_size=10)  # servo grab
    while not rospy.is_shutdown():
        if key == Key.up: # Поднятие серв 1 или 2
            if self.last == KeyCode(char='q'):
                print('servo 1 up')
            elif self.last == KeyCode(char='r'):
                print('servo 2 up')
        elif key == Key.down: # Опускание серв 1 или 2
            if self.last == KeyCode(char='q'):
                print('servo 1 down')
            elif self.last == KeyCode(char='r'):
                print('servo 2 down')
        elif (key == KeyCode(char='w')): # Проезд вперед
            vel_msg.linear.x = forvard
            print('go forward')
            pub1.publish(vel_msg)
        elif (key == KeyCode(char='a')): # Проезд влево
            vel_msg.angular.z = left
            print('go left')
        pub1.publish(vel_msg)
    elif (key == KeyCode(char='d')): # Проезд вправо
        vel_msg.angular.z = right
        print('go right')
        pub1.publish(vel_msg)
    elif (key == KeyCode(char='s')): # Проезд назад
        vel_msg.linear.x = back
        print('go back')
        pub1.publish(vel_msg)
    elif (key == KeyCode(char='t')): # Остановка ровера
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        print('stop')
        pub1.publish(vel_msg)
    elif (key == KeyCode(char='q')): # Включение режима работы с сервой 1
        self.last = key
        print('servo 1')
    elif (key == KeyCode(char='e')): # Включение режима работы с nfs
        self.last = key
        print('nfs')
    elif (key == KeyCode(char='r')): # Включение режима работы с сервой 2
        self.last = key
        print('servo 2')

def __init__(self):
    with Listener(main=self.on_press) as listener:
        listener.join()
try:
    main(self,key)
except rospy.ROSInterruptException:
    pass
