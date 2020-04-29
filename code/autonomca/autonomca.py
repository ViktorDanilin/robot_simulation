import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

class Autonomca():
    def callback(self, data):
        self.x_start = Odometry.pose.pose.position.x
        print('Start x',x_start)
        self.y_start = Odometry.pose.pose.position.y
        print('Start y',y_start)
        self.z_start = Odometry.pose.pose.position.z
        print('Start z',z_start)
        self.w_start = Odometry.pose.pose.position.z
        print('Start w',w_start)        
        Data = PoseStamped(pose.position.x = self.x_start,pose.position.y = self.y_start,pose.position.z = self.z_start,pose.position.w = self.w_start)
        pub.publish(Data)
        exit()
    def spin(self): 
        rospy.spin()
    def __init__(self):
        self.x_start, self.y_start, self.z_start, self.w_start =0.0,0.0,0.0,0.0
        rospy.init_node("autonomca", anonymous=True)
        self.pub = rospy.Publisher("/move_base_simple/goall", PoseStamped, queue_size=100)
        self.x = float(input('Send x'+'\n'))
        self.y = float(input('Send y'+'\n'))
        rospy.Subscriber("/odom", Odometry, callback)
        spin()
        
Autonomca()
