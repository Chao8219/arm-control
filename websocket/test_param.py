# ref: https://symfoware.blog.fc2.com/blog-entry-2288.html

import time
import roslibpy

connection_flag = True

def runMe():
    ros_client = roslibpy.Ros(host = '161.253.72.254', port=9090)
    print("Connecting...")
    param_sender = roslibpy.Param(ros_client, '/pub_joint_param')
    def set_param():
        while True:
            if not ros_client.is_connected:
                print('Wait a minute, ROS connection is down.')
                break
            pass_angels = [0.0, 47.0, 137.0, -90.0, 0.0, 90.0]
            param_sender.set(pass_angels)
            time.sleep(0.1)
    
    ros_client.on_ready(set_param, run_in_thread=True)
    ros_client.run_forever()

if __name__ == '__main__':
    runMe()