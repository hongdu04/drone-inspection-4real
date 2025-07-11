This document is an extension of [HKUST/FUEL](https://github.com/HKUST-Aerial-Robotics/FUEL), which is deploy to the real drone.

# How to use

Start the realsense, vins and mavros 

`rspx4.sh`

Start planer

`roslaunch exploration_manager rviz.launch`

`roslaunch exploration_manager exploration_exp.launch`

Start Controller

start your RC and set channel 5 and 6 to down

`roslaunch px4ctrl run_ctrl.launch`

Start Monitor

# Reference Projects

1. [Fast-Drone-250](https://github.com/ZJU-FAST-Lab/Fast-Drone-250)   
The controller module comes from this project, but this project is only for real objects and a single drone.

3. [FUEL](https://github.com/HKUST-Aerial-Robotics/FUEL)   
The  planning part comes from this project.
