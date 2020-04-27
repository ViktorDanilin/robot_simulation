#!/usr/bin/env python3

import rospy
from pynput.keyboard import Key, Listener, KeyCode, Key
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt16
from std_msgs.msg import UInt32

def on_press(key):
    global forvard,back,left,right,vel_msg,serv_msg,pub1,pub2,pub3
    if not rospy.is_shutdown():

        if (key == KeyCode(char='w')):
            vel_msg.linear.x = forvard
            print('go forvard')
            pub1.publish(vel_msg)
        elif (key == KeyCode(char='a')):
            vel_msg.angular.z = left
            print('go left')
            pub1.publish(vel_msg)
        elif (key == KeyCode(char='d')):
            vel_msg.angular.z = right
            print('go right')
            pub1.publish(vel_msg)
        elif (key == KeyCode(char='s')):
            vel_msg.linear.x = back
            print('go back')
            pub1.publish(vel_msg)
        elif (key == KeyCode(char='t')):
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            print('stop')
            pub1.publish(vel_msg)
        elif (key == Key.esc):
            exit()
            
def main(key):
    global forvard, back, left, right,vel_msg,serv_msg,pub1,pub2,pub3
    forvard = 3
    back = -3
    right = -2
    left = 2

    rospy.init_node("joystick", anonymous=True)
    pub1 = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    vel_msg = Twist()
    pub2 = rospy.Publisher("/arduino/servo1", UInt16, queue_size=10)
    serv_msg = UInt16
    pub3 = rospy.Publisher("/arduino/servo2", UInt16, queue_size=10)
    pub4 = rospy.Publisher("/arduino/motor1", UInt32, queue_size=10)
    motor_msg = UInt32
    pub5 = rospy.Publisher("/arduino/slider",UInt16, queue_size=10)
    slider_msg = UInt16
    with Listener(on_press=on_press) as listener:
        listener.join()
            
if __name__ == '__main__':
    try:
        main(Key)
    except rospy.ROSInterruptException:pass
