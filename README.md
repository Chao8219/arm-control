### Run Order


1. ROS end: `roslaunch arm-control sar_rosbridge_websocket.launch` to start websocket.

2. Remote PC: Open "arm-control/websocket/communicate_w_kinova.html" to connect with ROS end.

3. ROS end: `roslaunch j2n6s300_moveit_config j2n6s300_virtual_robot_demo.launch` to start RViz

4. ROS end: `rosrun kinova_arm_moveit_demo sar_project` to start movement. Make sure you've typed any keys after initialization to get started.

5. Remote PC: Edit the joint values, then push it to control.

### Useful Pages for rosbridge

http://wiki.ros.org/roslibjs/Tutorials/BasicRosFunctionality#CA-3bc839e9e2d3c2cac3f7fabffacfbda3d5c050ae_7

http://wiki.ros.org/ROS/Tutorials/UnderstandingServicesParams

https://answers.ros.org/question/273480/publish-and-subscribe-array-of-vector-as-message/

http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29

https://answers.ros.org/question/250959/connecting-different-computers-via-rosbridge/