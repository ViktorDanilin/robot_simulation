#!/usr/bin/env python3

import rospy
from pynput.keyboard import Key, Listener, KeyCode, Key
from geometry_msgs.msg import Twist
from std_msgs.msg import Int16


def main(key):

    forvard = 3
    back = -3
    right = -2
    left = 2

    rospy.init_node("joystick", anonymous=True)
    pub1 = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    vel_msg = Twist()
    pub2 = rospy.Publisher("/arduino/servo1", Int16, queue_size=10)
    serv_msg = Int16
    pub3 = rospy.Publisher("/arduino/servo2", Int16, queue_size=10)

    while not rospy.is_shutdown():
        if (key == KeyCode(char='w')):
            vel_msg.linear.x = forvard
            print('go forward')
            pub1.publish(vel_msg)
        elif (key == KeyCode(char='a')):
            vel_msg.linear.x = left
            print('go left')
            pub1.publish(vel_msg)
        elif (key == KeyCode(char='d')):
            vel_msg.linear.x = right
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
if __name__ == '__main__':
    try:
        main(Key)
    except rospy.ROSInterruptException:pass