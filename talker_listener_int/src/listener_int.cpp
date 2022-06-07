#include "ros/ros.h"
#include "std_msgs/Int32.h"

void callback(std_msgs::Int32 msg)
{
 ROS_INFO("data is : [%d]", msg.data);
}

int main(int argc, char **argv)
{
 ros::init(argc, argv, "listener_int");
 ros::NodeHandle n;
 
 ros::Subscriber sub = n.subscribe("int_chatter", 1000, callback);
 ros::spin();
 
 return 0;
}

