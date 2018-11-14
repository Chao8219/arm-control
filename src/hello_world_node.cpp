#include "arm-control/hello_world.hpp"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "hello_world");

    int num = 42;
    hello_kinova obj(num);
    obj.print_the_ultimate_number();
    while(ros::ok()){
        ROS_INFO("This is an example of ROS Info");
        ros::spinOnce();

        cout << "test" << endl;
    }
    return 0;
}