import roslibpy
ros = roslibpy.Ros(host='161.253.72.254', port=9090)
ros.on_ready(lambda: print('Is ROS connected? ', ros.is_connected))

def print_something():
    print("coool?")

def whats_the():
    print("wtf?")

ros.get_params(print_something(),whats_the())

ros.run_forever()