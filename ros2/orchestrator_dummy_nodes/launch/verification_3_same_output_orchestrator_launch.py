from launch import LaunchDescription
from launch.actions import Shutdown, GroupAction
from launch_ros.actions import Node

from orchestrator.orchestrator_lib.remapping_generation import generate_remappings_from_config_file


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='orchestrator_dummy_nodes',
            executable='orchestrator',
            name='orchestrator',
            parameters=[
                {"mode": "verification_3_same_output"},
            ],
            arguments=['--ros-args', '--log-level', 'l:=warn', '--log-level', 'orchestrator:=info'],
            on_exit=Shutdown(),
        ),
        *generate_remappings_from_config_file("orchestrator_dummy_nodes",
                                         "verification_3_same_output_launch_config.json"),
        GroupAction([
            Node(
                package="orchestrator_dummy_nodes",
                executable="detector",
                name="P1",
                exec_name="P1",
                parameters=[
                    {"processing_time": 0.4},
                    {"processing_time_range": 0.3},
                    {"queue_size": 3}
                ],
                remappings=[
                    ("input", "M"),
                    ("output", "D")
                ],
                on_exit=Shutdown(),
            ),
            Node(
                package="orchestrator_dummy_nodes",
                executable="detector",
                name="P2",
                exec_name="P2",
                parameters=[
                    {"processing_time": 0.4},
                    {"processing_time_range": 0.3},
                    {"queue_size": 3}
                ],
                remappings=[
                    ("input", "M"),
                    ("output", "D")
                ],
                on_exit=Shutdown(),
            ),
            Node(
                package="orchestrator_dummy_nodes",
                executable="verification_t_subscriber",
                name="T",
                exec_name="T",
                parameters=[
                    {"processing_time": 0.2},
                ],
                remappings=[("input1", "D")],
                on_exit=Shutdown(),
            ),
        ])
    ])
