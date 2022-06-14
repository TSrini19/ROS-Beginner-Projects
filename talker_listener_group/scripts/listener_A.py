#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Hi {}".format(data.data))
    rospy.loginfo("subscribed to chatter_A topic")

# def new_callback(data):
#     rospy.loginfo("Received {}".format(data.data))
#     # rospy.loginfo("subscribed to chatter_A topic")

def listener_A():
    rospy.init_node('listener_A', anonymous=True)
    rospy.Subscriber('chatter_A', String, callback)
    # rospy.Subscriber('feedback', String, new_callback)
    rospy.spin()

if __name__ == '__main__':
    listener_A()