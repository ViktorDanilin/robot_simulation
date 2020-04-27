#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from pynput.keyboard import Key, Listener, KeyCode, Key
from geometry_msgs.msg import Twist
from std_msgs.msg import Int16
import time

class Keyboard():
    def __init__(self):
        rospy.init_node("joystick", anonymous=True)
        pub1 = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        pub2 = rospy.Publisher("/arduino/servo1", Int16, queue_size=10)  # servo up/down
        pub3 = rospy.Publisher("/arduino/servo2", Int16, queue_size=10)  # servo grab
        
        self.last = None        
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    # Функция считываеия с клавиатуры        
    def on_press(self, key):
        #print('{0} pressed'.format(key))
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
            print('go forward')
        elif (key == KeyCode(char='a')): # Проезд влево
            print('go left')
        elif (key == KeyCode(char='d')): # Проезд вправо
            print('go right')
        elif (key == KeyCode(char='s')): # Проезд назад
            print('go back')
        elif (key == KeyCode(char='t')): # Остановка ровера
            print('stop')
        elif (key == KeyCode(char='q')): # Включение режима работы с сервой 1
            self.last = key
            print('servo 1')
        elif (key == KeyCode(char='e')): # Включение режима работы с nfs
            self.last = key
            print('nfs')
        elif (key == KeyCode(char='r')): # Включение режима работы с сервой 2
            self.last = key
            print('servo 2')        
        elif (key == Key.esc): # Выход из программы
            exit()
    def spin(self): # Утилита для общения с топиками
        rospy.spin()

try:
    k = Keyboard()
    k.spin() # Запуск программы
except rospy.ROSInterruptException:
    pass
