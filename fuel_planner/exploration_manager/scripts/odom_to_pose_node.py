#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

def odom_callback(msg):
    pose_msg = PoseStamped()
    pose_msg.header = msg.header
    pose_msg.pose = msg.pose.pose
    pose_pub.publish(pose_msg)

if __name__ == '__main__':
    rospy.init_node('odom_to_pose_node')
    pose_pub = rospy.Publisher('/imu_pose', PoseStamped, queue_size=1)
    rospy.Subscriber('/vins_fusion/camera_pose', Odometry, odom_callback)
    rospy.spin()
