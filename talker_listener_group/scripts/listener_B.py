#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Hi {}".format(data.data))
    rospy.loginfo("subscribed to chatter_B topic")

def listener_B():
    rospy.init_node('listener_B', anonymous=True)
    rospy.Subscriber('chatter_B', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener_B()