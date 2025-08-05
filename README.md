# line-tracing-bot


ros2 launch urdf_tutorial display.launch.py model:=/home/ros2/ros2_ws/src/line_tracing_bot/urdf/robot.urdf

ros2 run tf2_tools view_frames -o robot_frames

rqt_graph

ros2 topic list
ros2 node list
ros2 param list /robot_state_publisher
ros2 param get /robot_state_publisher robot_description
ros2 topic echo /robot_description
ros2 topic echo /joint_states
