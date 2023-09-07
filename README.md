# Stage for Ros2
 
## Environment
**Ubuntu 20.04 ROS2 Galactic/Humble**

## Reference
https://github.com/n0nzzz/stage_ros2

## Installation
- Stage dependencies
    ```bash
    $ sudo apt-get install git cmake g++ libjpeg8-dev libpng-dev libglu1-mesa-dev libltdl-dev libfltk1.1-dev
    ```
- Stage_Ros dependecies

    ```bash
    $ sudo apt install ros-humble-laser-filters
    $ sudo apt install ros-humble-joint-state-publisher
    $ sudo apt install ros-humble-xacro
    ```

- Build Stage and Stage_Ros

    ```bash
    $ mkdir -p stage_ros2_ws/src
    $ cd stage_ros2_ws/src
    $ git clone --branch ros2 git@github.com:tuw-robotics/Stage.git
    $ git clone https://github.com/woawo1213/stage_ros2.git
    $ cd..
    $ colcon build --symlink-install --cmake-args -DOpenGL_GL_PREFERENCE=LEGACY
    $ source install/setup.bash
    $ colcon build
    $ colcon build --symlink-install --packages-select stage_ros
    ```

## Quick Start

### Start Stage Simulator wirh a robot
    
    ```
    ros2 run stage_ros stageros src/ros_general_planner_tuto/woawo/stage_ros2/world/maze.world
    ```

### Start robot Navigation
- Launch  stage_ros

    ```
    ros2 launch stage_ros robot_launch.py nav:=true
    ```
- Start the map_server node
    ```
    ros2 run nav2_util lifecycle_bringup map_server
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