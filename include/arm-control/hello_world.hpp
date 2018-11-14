#ifndef HELLO_WORLD
#define HELLO_WORLD

#include <string>
#include <iostream>
#include "ros/ros.h"
#include "std_msgs/String.h"

using namespace std;

class hello_kinova
{
public:
    hello_kinova(); /**< Constructure */
    hello_kinova(int& num); /**< Overload with the number */
    int ultimate_answer;
    ros::NodeHandle nh;
    ros::Publisher pub_hello_world;
    
    void print_the_ultimate_number();
    void ros_init();      
};


#endif