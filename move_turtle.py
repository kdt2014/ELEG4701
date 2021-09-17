#!/usr/bin/env python  
# -*- coding: utf-8 -*-

import sys
import rospy as ros 
# if you use "import rospy", you must use rospy.**. example: rospy.loginfo(), there is a 
# mistake in this code file related to this issue, please find and correct it  TODO 0

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

ROBOT_X = 0

def pose_callback(pose):
    global ROBOT_X
    ros.loginfo("Robot X = %f: Y=%f: Z = %f\n", pose.x, pose.y, pose.theta)
    ROBOT_X = pose.x

# TODO 0: modify the code below so that you can pub velocity and subscribe the pose
def move_turtle(modify_here, modify_here, modify_here):                              #modify code in this line
    global ROBOT_X
    ros.init_node('move_turtle', anonymous=False)
    pub = ros.Publisher( topic_name, msg_class, queue_size=10)                       #modify code in this line
    ros.Subscriber( topic_name, msg_class, pose_callback)                            #modify code in this line

    rate = rospy.Rate(10) 
    vel = Twist()
    while not ros.is_shutdown():
        # TOTO 1: draw a circle, the linear velocity is π m/s, and radius is 1 m
        # modify the code below and import something at the start of the file, you should use the π in math library rather than 3.14
        # if the x positon larger than 8, stop to draw, you need to input 3 parameters in terminal

        vel.linear.x = 0   
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        ros.loginfo("Linear Vel = %f: Angular Vel = % f", modify_here, modify_here) #modify code in this line
        if ROBOT_X >= modify_here:                                                  #modify code in this line
            ros.loginfo('Robot exercises finished.')
            ros.logwarn('stopping robot')
            break
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    except ros.ROSInterruptException:
        pass