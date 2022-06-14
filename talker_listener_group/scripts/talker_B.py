#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker_B():
    rospy.init_node('talker_B', anonymous=True)
    publisher = rospy.Publisher('chatter_B', String, queue_size=100)
    rate = rospy.Rate(5)

    data = "Node B"
    rospy.loginfo("Publishing data to chatter_B topic")

    while not rospy.is_shutdown():
        publisher.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker_B()
    except rospy.ROSInterruptException:
        rospy.loginfo("ROS master stopped")