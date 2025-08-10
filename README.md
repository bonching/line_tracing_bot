# line-tracing-bot


## running the robot using urdf_tutorial
```
ros2 launch urdf_tutorial display.launch.py model:=/home/ros2/ros2_ws/src/line_tracing_bot/urdf/robot.urdf
```


## visualize nodes and topics
```
ros2 run tf2_tools view_frames -o robot_frames
rqt_graph

ros2 topic list
ros2 node list
ros2 param list /robot_state_publisher
ros2 param get /robot_state_publisher robot_description
ros2 topic echo /robot_description
ros2 topic echo /joint_states
```


## running the robot via command line
```
sudo apt install ros-jazzy-xacro
ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(xacro /home/ros2/ros2_ws/src/line_tracing_bot/urdf/robot.urdf)"

sudo apt install ros-jazzy-join-state-publisher-gui
ros2 run joint_state_publisher_gui joint_state_publisher_gui

ros2 run rviz2 rviz2
```


## running the robot using a launch file
```
sudo apt install python3-colcon-common-extensions

cd ~/ros2_ws
colcon build
source install/setup.bash

ros2 launch line_tracing_bot display.launch.xml
ros2 launch line_tracing_bot display.launch.py
```



## running in gazebo simulation
```
sudo apt install ros-jazzy-ros-gz

gz topic -l

ros2 launch ros_gz_sim gz_sim.launch.py gz_args:=empty.sdf
```

https://wiki.ros.org/urdf/Tutorials/Adding%20Physical%20and%20Collision%20Properties%20to%20a%20URDF%20Model
https://jpmc.udemy.com/course/ros2-tf-urdf-rviz-gazebo/learn/lecture/49399739#overview

```
ros2 run ros_gz_sim create -topic robot_description
```

## gazebo plugins
https://github.com/gazebosim/gz-sim/tree/gz-sim9/src/systems
https://github.com/gazebosim/ros_gz/tree/ros2/ros_gz_bridge
https://app.gazebosim.org/fuel/models (search for openrobotics)

```
gz topic -l
gz topic -i -t /clock

ros2 topic list
ros2 topic info /cmd_vel
ros2 interface show geometry_msgs/msg/Twist
ros2 topic pub -r 1 /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5}, angular: {z: 0.5}}"
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```


