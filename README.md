# About The Arm-Control Repo

This repo is designed for control kinova jaco 2 remotely at any platform.

The server end is running ROS Indigo on Ubuntu 14.04 since the official kinova package supports only upto ROS Indigo, and ROS Indigo only could be installed on Ubuntu 14.04. 

The package that we use to communicate is rosbridge. To have a good communication, you may need to use another repo that I mirrored from official package.

## Contents

&nbsp;&nbsp;[1 Run Order](#1-run-order)

&nbsp;&nbsp;[2 Useful Pages for Rosbridge](#2-useful-pages-for-rosbridge)

## 1 Run Order

ROS End

1. Enter command in terminal as follow: `roslaunch arm-control sar_rosbridge_websocket.launch` to start websocket.

2. Enter command in terminal as follow: `roslaunch arm-control virtual_j2n6s300.launch` to start RViz.

3. Enter command in terminal as follow: `roslaunch arm-control moveit_remote.launch` to start movement.

Remote PC(any platform):

1. Open "arm-control/websocket/communicate_w_kinova.html" to connect with ROS end.

2. Edit the joint values, then push it to control. or just slide the range control to control it in real time.

[Back to Top](#contents)

## 2 Useful Pages for Rosbridge

http://wiki.ros.org/roslibjs/Tutorials/BasicRosFunctionality#CA-3bc839e9e2d3c2cac3f7fabffacfbda3d5c050ae_7

http://wiki.ros.org/ROS/Tutorials/UnderstandingServicesParams

https://answers.ros.org/question/273480/publish-and-subscribe-array-of-vector-as-message/

http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29

https://answers.ros.org/question/250959/connecting-different-computers-via-rosbridge/

[Back to Top](#contents)