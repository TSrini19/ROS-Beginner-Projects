#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Point

def pose_callback(data):
    rospy.loginfo("The coordinates are {}".format(data))

def listener_pose():
    rospy.init_node('listener_pose_py', anonymous=True)
    rospy.Subscriber('pose', Point, pose_callback)
    rospy.spin()

if __name__ == '__main__':
    listener_pose()