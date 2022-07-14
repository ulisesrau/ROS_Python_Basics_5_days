#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def callback(msg):
    my_data = msg.ranges

    if (my_data[360] > 1):
        vel_data.linear.x = 0.5
        vel_data.angular.z = 0
    elif ((my_data[360] < 1) or (my_data[-1] < 1)):
        vel_data.linear.x = 0.05
        vel_data.angular.z = 3.2
    elif (my_data[0] < 1):
        vel_data.linear.x = 0.05
        vel_data.angular.z = -3.2


rospy.init_node('topics_quiz_node')

vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
laser_sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)

rate = rospy.Rate(2)

vel_data = Twist()

while not rospy.is_shutdown():

    vel_pub.publish(vel_data)

    rate.sleep()
