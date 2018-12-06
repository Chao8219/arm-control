# ref: https://symfoware.blog.fc2.com/blog-entry-2288.html
# this python file requires you to install roslibpy module by
# `pip install roslibpy`
# 

import time
import roslibpy

connection_flag = True
input_file_name = "test_data.txt"

# print the working space location, to debug reading directory issue
import os
# Get the current working directory (cwd)
cwd = os.getcwd()  
# Get all the files in that directory
files = os.listdir(cwd)  
print("Files in '%s': %s" % (cwd, files))

def run_me():
    ros_client = roslibpy.Ros(host = '161.253.72.254', port=9090)
    print("Connecting...")
    param_sender = roslibpy.Param(ros_client, '/pub_joint_param')
    def set_param():
        while True:
            if not ros_client.is_connected:
                print('Wait a minute, ROS connection is down.')
                break
            updating_angles = read_data(input_file_name)
            param_sender.set(updating_angles)
            time.sleep(0.01)
    def read_data(file_name):
        # use with to close file after reading automatically
        # read only
        with open(file_name, "r") as text_file:
            # read strings that are seperated with space
            # a dummy tail is needed in this txt file
            # because by default, txt file will have a \n in the end
            string_line0 = text_file.read().split(' ')
        # convert strings into float numbers
        float_line0 = [float(string_line0[0]), float(string_line0[1]), 
                        float(string_line0[2]), float(string_line0[3]),
                        float(string_line0[4]), float(string_line0[5])]
        return float_line0
        
    ros_client.on_ready(set_param, run_in_thread=True)
    ros_client.run_forever()

if __name__ == '__main__':
    run_me()