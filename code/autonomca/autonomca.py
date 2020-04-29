#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
x_start,y_start,z_start = 0,0,0

def callback1(data):
    global x_start,y_start,z_start
    x_start = data.pose.pose.position.x
    print('Start x', x_start)
    y_start = data.pose.pose.position.y
    print('Start y', y_start)
    z_start = data.pose.pose.position.z
    print('Start z', z_start)
#    return x_start,y_start,z_start

def subscriber1():
    rospy.init_node('listener')
    pub = rospy.Publisher("/move_base_simple/goall", PoseStamped, queue_size=100)
    rospy.Subscriber("/odom", Odometry, callback1)

subscriber1()

def dist():
    i = 0
    while not rospy.core.is_shutdown() and i < 2:
        rospy.rostime.wallsleep(1)
        i = i+1
        rospy.sleep(1)

#while True
x = float(input('Send x'+'\n'))
y = float(input('Send y'+'\n'))
print(x,y)
ass = PoseStamped()
ass.pose.position.x = self.x_start
ass.pose.position.y = self.y_start
ass.pose.position.z = self.z_start
print(x_start,y_start,z_start)
#dist()
print(x_start,y_start,z_start)
pub.publish(ass)