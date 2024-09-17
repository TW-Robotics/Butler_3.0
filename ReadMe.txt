Butler_3.0 Package

1.) Clone the package from Github in your catkin workspace src folder

2.) go to you catkin_ws root folder and do $rosdep install --from-paths src --ignore-src -r -y

3.) catkin_make

4a.) to launch the robot in rviz $roslaunch butler_bringup butler_rviz.launch
4b.) to launch the robot with moveit $roslaunch butler_bringup butler_moveit.launch
4c.) to launch moveit with the real UR5 $roslaunch butler_bringup butler_real_ur5.launch robot_ip:=192.168.X.X (IP from the real robot)


