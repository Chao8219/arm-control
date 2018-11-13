#ifndef HELLO_WORLD
#define HELLO_WORLD

#include <string>
#include <iostream>
#include "ros/ros.h"

using namespace std;

class hello_kinova
{
public:
    hello_kinova(); /**< Constructure */
    hello_kinova(int& num); /**< Overload with the number */
    int ultimate_answer;
    ros::NodeHandle nh;
    
    void print_the_ultimate_number();            
};


#endif