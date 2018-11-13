#include "arm-control/hello_world.hpp"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "hello_world");

    hello_kinova obj;

    obj.print_the_ultimate_number();
    ros::spin();
    
    return 0;
}