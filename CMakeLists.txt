cmake_minimum_required(VERSION 2.8.3)
project(arm-control)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED roscpp std_msgs)

catkin_package(CATKIN_DEPENDS roscpp std_msgs)

## find_package(catkin REQUIRED 
##             COMPONENTS
##             roscpp
##             std_msgs
##             moveit_core
##             moveit_ros_planning
##             moveit_ros_planning_interface
##             pluginlib
##             cmake_modules
##             geometric_shapes)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_library(hello_world_lib src/hello_world.cpp)

add_executable(hello_world src/hello_world_node.cpp)
target_link_libraries(hello_world hello_world_lib ${catkin_LIBRARIES})

