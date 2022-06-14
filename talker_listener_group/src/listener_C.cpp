#include "ros/ros.h"
#include "std_msgs/String.h"

void chatterCallback(std_msgs::String msg)
{

  ROS_INFO("Hi: [%s]", msg.data.c_str());

}

void new_talker()
{
ros::NodeHandle n;
ros::Publisher chatter_topic1 = n.advertise<std_msgs::String>("feedback", 1000);
  ros::Rate loop_rate(10);
  int count = 0;
  while (ros::ok())
  {
    std_msgs::String msg1;
    
    std::string new_data = "Node C to source";
         
    msg1.data = new_data;
    ROS_INFO("%s", msg1.data.c_str());
    chatter_topic1.publish(msg1);
    ros::spinOnce();
    loop_rate.sleep();
    ++count;
  }
}


int main(int argc, char **argv)
{

  ros::init(argc, argv, "listener_C");

  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("chatter_A", 1000, chatterCallback);
  ros::Subscriber sub1 = n.subscribe("chatter_B", 1000, chatterCallback);
  new_talker();
  ros::spin();
  
  

  return 0;
}
