#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo(data)

def listener_int():
    rospy.init_node('listener_int_py', anonymous=True)
    rospy.Subscriber('int_chatter', Int32, callback)

    rospy.spin()

if __name__ == "__main__":
    listener_int()

