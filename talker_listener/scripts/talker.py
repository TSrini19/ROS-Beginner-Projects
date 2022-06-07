#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('talker_py', anonymous=True)
    publisher = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        hello_string = "Hello World_py"
        rospy.loginfo(hello_string)
        publisher.publish(hello_string)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
