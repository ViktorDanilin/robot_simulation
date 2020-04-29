#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped

rospy.init_node("final")
goal_publisher = rospy.Publisher("move_base_simple/goal", PoseStamped, queue_size=5)
