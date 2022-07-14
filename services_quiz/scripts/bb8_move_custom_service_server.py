#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse
from geometry_msgs.msg import Twist


def my_callback(request):

    repetition = 0
    while repetition < request.repetitions:

        repetition = repetition + 1
        i = 0
        while i < 4:

            move_circle.linear.x = 1
            move_circle.angular.z = 0
            my_pub.publish(move_circle)
            rospy.Rate(1/request.side).sleep()

            move_circle.linear.x = 0
            move_circle.angular.z = 0
            my_pub.publish(move_circle)
            rospy.Rate(0.5).sleep()

            move_circle.linear.x = 0
            # almost 0.7820 un poco a la derecha (casi cerca)
            move_circle.angular.z = 0.78195
            my_pub.publish(move_circle)
            rospy.Rate(0.5).sleep()

            move_circle.linear.x = 0
            move_circle.angular.z = 0
            my_pub.publish(move_circle)
            rospy.Rate(0.5).sleep()

            i = i + 1

    rospy.loginfo("Finished service move_bb8_in_square_custom")
    response = BB8CustomServiceMessageResponse()
    response.success = True

    return response


rospy.init_node('bb8_server')
my_service = rospy.Service(
    '/move_bb8_in_square_custom', BB8CustomServiceMessage, my_callback)
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_circle = Twist()
rospy.loginfo("Service /move_bb8_in_square_custom Ready")
rospy.spin()
