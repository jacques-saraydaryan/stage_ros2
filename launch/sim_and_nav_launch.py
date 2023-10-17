from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import RegisterEventHandler
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.event_handlers import OnExecutionComplete
from launch.actions import ExecuteProcess
import os

#launch tuto https://roboticscasual.com/tutorial-ros2-launch-files-all-you-need-to-know/

def generate_launch_description():
    stage_ros_location = FindPackageShare(package='stage_ros').find('stage_ros')
    world_file = os.path.join(stage_ros_location, 'world/maze.world')

    ld = LaunchDescription()


    #nav_ns = LaunchConfiguration('nav_ns')
    #nav_arg = DeclareLaunchArgument(
    #    'nav',
    #    default_value='true'
    #)
    
    #launch stage without gui
    stage_node= Node(
        package='stage_ros',
        executable='stageros',
        output='screen',
        arguments=['-g','False', world_file]
        )

    #add Navigation launch file
    rob_nav_launch = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([
                    stage_ros_location, '/launch', '/robot_launch.py']),
                    launch_arguments={'nav': 'true','use_rviz':'false'}.items()
            )

            #nav:=true

    # start the map server
    nav2_util_node= Node(
        package='nav2_util',
        executable='lifecycle_bringup',
        output='screen',
        arguments=['map_server']
        )

    #here possibility to call a service
    #ExecuteProcess(
    #        cmd=[
    #            [
    #                FindExecutable(name="ros2"),
    #                " service call ",
    #                "/spawn ",
    #                "turtlesim/srv/Spawn ",
    #                "\"{x: 2.0, y: 2.0, theta: 0.0, name: 'turtle2'}\"",
    #            ]
    #        ],
    #        shell=True,
    #    )

    
    # Wait end of the execustion in our case, end is never reach for stage_ros
    #evt_stage_node_started =RegisterEventHandler(
    #       event_handler=OnExecutionComplete(
    #           target_action=stage_node,
    #           on_completion=[rob_nav_launch],
    #       )
    #   )
    
    #ld.add_action(evt_stage_node_started)
    ld.add_action(stage_node)
    ld.add_action(rob_nav_launch)
    ld.add_action(nav2_util_node)
    return ld




    