#include "arm-control/hello_world.hpp"

hello_kinova::hello_kinova(){
    ros_init();
    cout << "No argument input" << endl;
}

hello_kinova::hello_kinova(int& num){
    ros_init();
    ultimate_answer = num;
}

void hello_kinova::print_the_ultimate_number()
{
    cout << ultimate_answer << endl;
    return;
}

void hello_kinova::ros_init(){
    pub_hello_world = nh.advertise<std_msgs::String>("talker", 1000);
}
