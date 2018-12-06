# About The Arm-Control Repo

This repo is designed for control Kinova Jaco2 remotely at any platform.

The server end is running ROS Indigo on Ubuntu 14.04 since the official kinova package supports only upto ROS Indigo, and ROS Indigo only could be installed on Ubuntu 14.04. 

The package that we use to communicate is rosbridge. To have a good communication, you may need to use another repo that I mirrored from official package.

## Contents

&nbsp;&nbsp;[0 General Environment Requirement](#0-general-environment-requirement)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0.1 ROS End](#01-ros-end)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0.2 Remote End](#02-remote-end)

&nbsp;&nbsp;[1 Run Order](#1-run-order)

&nbsp;&nbsp;[2 Useful Pages for Rosbridge](#2-useful-pages-for-rosbridge)

&nbsp;&nbsp;[3 Todo List](#3-todo-list)

## 0 General Environment Requirement

### 0.1 ROS End

On ROS end, the Kinova official package [kinova-ros](https://github.com/Kinovarobotics/kinova-ros) is tested in ROS Indigo. Therefore, you need to have the ROS Indigo installed. Although, I believe, there is a way to run this package on ROS Kinect or even higher, I didn't give it a try due to limited time.

Once you have ROS Indigo fully installed, you can follow the instruction on that github page to run real robot control or simulation in gazebo or moveit.

Once you are totally familiar with it, you need to clone a mirrored repo [here](https://github.com/Chao8219/kinova-ros-mirror). **The License issue should be dealed with.**

Please don't put the original kinova-ros and the mirrored one in the same `catkin_ws/src/`, becasue I did not change the node's names, and it will cause some complie issues.

[Back to Top](#contents)

### 0.2 Remote End

If you want to use the web page that is based on javascript, there is nothing you need to prepare. Oh yes, maybe a Firefox or Chrome would be better for debug.

For the use of python script, you need to use `pip install roslibpy` to obtain that module. See [here](https://github.com/gramaziokohler/roslibpy) to see the details of this module.

[Back to Top](#contents)

## 1 Run Order

ROS End

1. Enter command in terminal as follow: `roslaunch arm-control sar_rosbridge_websocket.launch` to start websocket.

2. Enter command in terminal as follow: `roslaunch arm-control virtual_j2n6s300.launch` to start RViz.

3. Enter command in terminal as follow: `roslaunch arm-control moveit_remote.launch` to start movement.

Remote PC (any platform):

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

## 3 Todo List

- [x] Add end-effector coordinate control
- [ ] Complete automatic file reading in JS page.(for .txt)
- [ ] Complete automatic file reading in JS page.(for .csv)
- [x] Update initial position to "Starting Pose" in JS page
- [ ] License issue with the kinova-ros pacakge
- [x] Complete constantly reading and writting files in py script.

[Back to Top](#contents)