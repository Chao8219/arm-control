# ref: https://symfoware.blog.fc2.com/blog-entry-2288.html
# this python file requires you to install roslibpy module by
# `pip install roslibpy`
# 

import time
import roslibpy
import sys

connection_flag = True
input_file_name = "test_data.txt"

# print the working space location, to debug reading directory issue
import os
# Get the current working directory (cwd)
cwd = os.getcwd()  
# Get all the files in that directory
files = os.listdir(cwd)  
print("[Debug] Files in '%s': %s" % (cwd, files))

def run_me():
    ros_client = roslibpy.Ros(host = '161.253.72.254', port=9090)
    print("[INFO] Connecting...")
    pub_joint_param_mount = roslibpy.Param(ros_client, '/pub_joint_param')
    def param_rw():
        print("[INFO] ROS is connected. Hold on tight.")
        time.sleep(0.5)
        while True:
            if not ros_client.is_connected:
                print('[INFO] Wait a minute, ROS connection is down.')
                break
            updating_angles = read_data(input_file_name)
            pub_joint_param_mount.set(updating_angles)
            time.sleep(0.01)
            pub_joint_param_mount.get(lambda the_list: 
                                print("[INFO] Joint Angles: ", the_list), 
                                lambda error_msg: 
                                print("[Error] ", error_msg))
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
        
    ros_client.on_ready(param_rw, run_in_thread=True)
    ros_client.run_forever()
    if not ros_client.is_connected:
        print("[WARNING] ROS is not connected.", 
              "Please rerun this script after ROS started.")
        sys.exit()

if __name__ == '__main__':
    run_me()