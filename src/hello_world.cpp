#include "arm-control/hello_world.hpp"

hello_kinova::hello_kinova(){}

hello_kinova::hello_kinova(int& num){
    ultimate_answer = num;
}

void hello_kinova::print_the_ultimate_number()
{
    cout << ultimate_answer << endl;
    return;
}

