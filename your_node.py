#!/usr/bin/env python
# -*- coding: utf-8 -*-
#this example will pub turtle1/cmd_vel topic，message type is geometry_msgs::Twist, node name is velocity_publisher_last 3 number of you SID,
#example: sid 1155135432 and the node name will be velocity_publisher_432

# TODO 0: modify the package.xml file, add rospy dependence; set eniveriment in ./bashrc file so that you do not need to source every time
# finish this task and show the result in the terminal. 
import rospy
from geometry_msgs.msg import Twist

def velocity_publisher():
    # TODO 0, ROS node initialize
	rospy.init_node('node name', anonymous=True)

	# create a Publisher, queue size is 10
    # TODO 1: finish the code below 
    # reference: rospy.Publisher(topic_name, msg_class, queue_size)
    turtle_vel_pub = rospy.Publisher( topic_name, msg_class, queue_size=10)

	#set loop rate
    rate = rospy.Rate(10) 

    while not rospy.is_shutdown():
		# init geometry_msgs::Twist
        vel_msg = Twist()
        # TOTO 2: draw a circle, the linear velocity is π m/s, and radius is 1 m
        # modify the code below and import something at the start of the file, you should use the π in math library rather than 3.14
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

		# publish
        turtle_vel_pub.publish(vel_msg)

        #TODO 3: modify the code below, let the terminal output velocity
    	rospy.loginfo("Publsh turtle velocity command[% velocity m/s, %velocity radius]", 
				vel_msg.linear.x, vel_msg.angular.z)

		# delay as loop rate
        rate.sleep()

if __name__ == '__main__':
    try:    
        velocity_publisher()
    except rospy.ROSInterruptException:
        pass


