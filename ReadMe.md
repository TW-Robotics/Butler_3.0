# Butler_3.0 Package (ROS Noetic)

1. Clone the package from Github in your catkin_ws/src folder

2. Go to you catkin_ws root folder and do `$rosdep install --from-paths src --ignore-src -r -y`

3. Do `$catkin_make`

To launch the robot in rviz `$roslaunch butler_bringup butler_rviz.launch`

To launch the robot with moveit `$roslaunch butler_bringup butler_moveit.launch`

To launch moveit with the real UR5 `$roslaunch butler_bringup butler_real_ur5.launch robot_ip:=192.168.X.X` (IP from the real robot)

![alt text](https://github.com/TW-Robotics/Butler_3.0/blob/main/butler.png?raw=true)


