#include "ros/ros.h"
#include "std_msgs/Int32.h"

int main(int argc, char **argv)
{
 ros::init(argc,argv, "talker_int");
 ros::NodeHandle n;
 
 ros::Publisher int_chat_topic = n.advertise<std_msgs::Int32>("int_chatter", 1000);
 
 ros::Rate loop_rate(10);
 
 while (ros::ok())
 {
  std_msgs::Int32 msg;
  msg.data = 10;
  
  ROS_INFO("%d", msg.data);
  int_chat_topic.publish(msg);
  ros::spinOnce();
  loop_rate.sleep();
 }
 
 return 0;
}
  
