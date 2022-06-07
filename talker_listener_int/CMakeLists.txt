cmake_minimum_required(VERSION 3.0.2)
project(talker_listener_int)

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

add_executable(talker_cpp src/talker_int.cpp)
target_link_libraries(talker_cpp ${catkin_LIBRARIES})

add_executable(listener_cpp src/listener_int.cpp)
target_link_libraries(listener_cpp ${catkin_LIBRARIES})

