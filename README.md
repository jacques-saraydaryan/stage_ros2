# Stage for Ros2
 
## Environment
**Ubuntu 20.04 ROS2 Galactic/Humble**

## Reference
https://github.com/n0nzzz/stage_ros2

## Installation
```bash
$ mkdir -p stage_ros2_ws/src
$ cd stage_ros2_ws/src
$ git clone https://github.com/woawo1213/stage_ros2.git
#$ sudo apt-get install ros-noetic-stage # for FLTK
$ sudo apt install ros-humble-laser-filters
$ sudo apt install ros-humble-joint-state-publisher
$ sudo apt install ros-humble-xacro
$ cd ..
$ colcon build
```

## Quick Start

### Robot Stage
```
ros2 run stage_ros stageros src/stage_ros2/world/wonik_4th.world
ros2 run stage_ros stageros src/ros_general_planner_tuto/woawo/stage_ros2/world/maze.world
```

- start the map_server node
```
ros2 run nav2_util lifecycle_bringup map_server
```

### Robot Navigation
Launch 

```
# Navigation
ros2 launch stage_ros robot_launch.py nav:=true
```
2D Pose Estimate, 2D Goal Pose

<img src="doc/nav.png" width="1000" height="500">

### Robot SLAM
Launch 
```
# Terminal 1
ros2 launch stage_ros robot_launch slam:=true

# Terminal 2
ros2 run teleop_twist_keyboard teleop_twist_keyboard

# Terminal 3
ros2 launch teleop_twist_joy teleop-launch.py joy_config:='xbox'
```
<img src="doc/slam.png" width="700" height="700">