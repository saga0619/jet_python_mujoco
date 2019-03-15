# jet_python_mujoco
dyros jet python controller for mujoco

## Installation
* clone this Repository and [mujoco_ros Repository](https://github.com/saga0619/mujoco_ros_sim) to your ros workspace (commonly at catkin_ws)
* install [pinocchio library](https://github.com/stack-of-tasks/pinocchio)
* then build (catkin_make )

## Mujoco License file 
For mujoco user, you need to edit the position of license in launch/sim.launch with your license file's location
(vmjkey.txt at Home folder is default configuration)

## How to run
roslaunch jet_python_mujoco sim.launch

'i' -> initial posture

'h' -> home posture

'tab' -> pause/run --> notworking

'q' -> exit
