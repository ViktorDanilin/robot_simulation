import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry

class Car_barrier_detection():
    def __init__(self):
        self.x = float(input('Send x'+'\n'))
        self.y = float(input('Send y'+'\n'))

        self._pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=5)
        self._sub_3 = rospy.Subscriber('/odom', Odometry, self.callback3, queue_size=10)
    def callback3(self, odometry):

        self.position_now = [odometry.pose.pose.position.x, odometry.pose.pose.position.y]
        if self.position_now != None:
            print("hoo")
            ass = PoseStamped()
            ass.header.seq = 1
            ass.header.stamp = rospy.Time.now()
            ass.header.frame_id = "map"

            ass.pose.orientation.x = self.x
            ass.pose.orientation.y = self.y
            ass.pose.orientation.z = 0
            ass.pose.position.x = self.position_now[0]
            ass.pose.position.y = self.position_now[1]
            ass.pose.position.z = 0
            ass.pose.orientation.w = 0.0
            rospy.sleep(1)
            self._pub.publish(ass)
            exit()
    def main(self):

        rospy.spin()

if __name__ == '__main__':
    print("hi")
    rospy.init_node('car_barrier_detection')
    node = Car_barrier_detection()
    node.main()
