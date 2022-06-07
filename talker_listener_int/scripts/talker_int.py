#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def talker_int():
    rospy.init_node('talker_int_py', anonymous=True)
    Pub_int = rospy.Publisher('int_chatter', Int32, queue_size=100)
    rate = rospy.Rate(10)


    while not rospy.is_shutdown():
        data = 19
        rospy.loginfo(data)
        Pub_int.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker_int()
    except rospy.ROSInterruptException:
        pass