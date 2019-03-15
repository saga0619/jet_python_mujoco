#!/usr/bin/env python

from Controller import robot
import rospy
from Bridge import connection
from Bridge import configuration as cf
from Bridge import kbhit
import numpy as np

mj = connection.mujoco()

exit_flag = False
is_first = True
is_simulation_run = True
kbd = kbhit.KBHit()
qinit = np.copy(mj.q)
qdes = qinit
r = rospy.Rate(200)

robot = robot.RobotState()
robot.updateKinematics(np.matrix(np.zeros(cf.dof)).T,
                       np.matrix(np.zeros(cf.dof)).T)
robot.placement(cf.joint_names[0])

while (not exit_flag) and (not rospy.is_shutdown()):
    if kbd.kbhit():
        key = kbd.getch()
        if key == 'q':
            is_simulation_run = False
            exit_flag = True
        elif key == '\t':  # TAB
            if is_simulation_run:
                print("SIMULATION PAUSE")
                is_simulation_run = False
            else:
                print "SIMULATION RUN"
                is_simulation_run = True
        elif key == 'i':
            print "Initial Posture"
            qdes = qinit
        elif key == 'h':
            print "Home Posture"
            qdes = np.array(np.zeros(cf.dof))
    if is_simulation_run:
        if is_first:
            qdes = qinit
            is_first = False

        mj.setMototState(qdes)
    r.sleep()
