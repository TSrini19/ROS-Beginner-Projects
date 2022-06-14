#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def new_callback(data):
    rospy.loginfo("Received {}".format(data.data))
    # rospy.loginfo("subscribed to chatter_A topic")

def talker_A():
    rospy.init_node('talker_A', anonymous=True)
    publisher = rospy.Publisher('chatter_A', String, queue_size=100)
    rate = rospy.Rate(5)

    data = "Node A"
    rospy.loginfo("Publishing data to chatter_A topic")

    while not rospy.is_shutdown():
        publisher.publish(data)
        rospy.Subscriber('feedback', String, new_callback)
        rospy.spin()
        rate.sleep()



if __name__ == '__main__':
    try:
        talker_A()
    except rospy.ROSInterruptException:
        rospy.loginfo("ROS master stopped")