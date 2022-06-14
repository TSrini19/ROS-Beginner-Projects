cmake_minimum_required(VERSION 3.0.2)
project(talker_listener_group)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

catkin_package()

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(listener_C src/listener_C.cpp)
target_link_libraries(listener_C ${catkin_LIBRARIES})

