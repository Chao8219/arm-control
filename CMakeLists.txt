cmake_minimum_required(VERSION 2.8.3)
project(arm-control)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED roscpp std_msgs)

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
             
catkin_package()
