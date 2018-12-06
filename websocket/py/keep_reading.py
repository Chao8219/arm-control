# ref: https://symfoware.blog.fc2.com/blog-entry-2288.html
# this python file requires you to install roslibpy module by
# `pip install roslibpy`
# 

import time
import roslibpy

connection_flag = True

def run_me():
    ros_client = roslibpy.Ros(host = '161.253.72.254', port=9090)
    print("Connecting...")
    param_test = roslibpy.Param(ros_client, '/wtf')
    def get_param():
        while True:
            if not ros_client.is_connected:
                print('Wait a minute, ROS connection is down.')
                break
            # pass whatever is passing into here to somewhere else
            param_test.get(lambda test_value: print("[Callback Value] ", 
                                                    test_value), 
                           lambda error_msg: print("[Error] ", 
                                                   error_msg))
            time.sleep(0.01)
    ros_client.on_ready(get_param, run_in_thread=True)
    ros_client.run_forever()

if __name__ == '__main__':
    run_me()