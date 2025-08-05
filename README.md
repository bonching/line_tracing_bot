# line-tracing-bot


## running the robot using urdf_tutorial
ros2 launch urdf_tutorial display.launch.py model:=/home/ros2/ros2_ws/src/line_tracing_bot/urdf/robot.urdf


## visualize nodes and topics
ros2 run tf2_tools view_frames -o robot_frames
rqt_graph

ros2 topic list
ros2 node list
ros2 param list /robot_state_publisher
ros2 param get /robot_state_publisher robot_description
ros2 topic echo /robot_description
ros2 topic echo /joint_states


## running the robot via command line
sudo apt install ros-jazzy-xacro
ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:="$(xacro /home/ros2/ros2_ws/src/line_tracing_bot/urdf/robot.urdf)"

sudo apt install ros-jazzy-join-state-publisher-gui
ros2 run joint_state_publisher_gui joint_state_publisher_gui

ros2 run rviz2 rviz2


## running the robot using a launch file
sudo apt install python3-colcon-common-extensions

cd ~/ros2_ws
colcon build
source install/setup.bash


