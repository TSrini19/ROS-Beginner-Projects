#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Point

def talker_geo():
    rospy.init_node('talker_pose_py', anonymous=True)
    pub_pose = rospy.Publisher('pose', Point, queue_size=1000)
    rate = rospy.Rate(5)

    point = Point()
    point.x = 5.0
    point.y = 4.0
    point.z = 0.0

    rospy.loginfo("Coordinates are published")

    while not rospy.is_shutdown():
        pub_pose.publish(point)
        rate.sleep()
        

if __name__ == '__main__':
    try:
        talker_geo()
    except rospy.ROSInterruptException:
        rospy.loginfo("ROS Master stopped")

