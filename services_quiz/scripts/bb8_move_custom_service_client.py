#! /usr/bin/env python
import rospkg
import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest


rospy.init_node('bb8_client')

rospy.wait_for_service('/move_bb8_in_square_custom')

move_bb8_in_square_service_client = rospy.ServiceProxy(
    '/move_bb8_in_square_custom', BB8CustomServiceMessage)

move_bb8_in_square_request_object = BB8CustomServiceMessageRequest()

move_bb8_in_square_request_object.side = 3.0
move_bb8_in_square_request_object.repetitions = 2

rospy.loginfo("Doing 1st Service Call...")
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object)

rospy.loginfo(str(result))

move_bb8_in_square_request_object.side = 6.0
move_bb8_in_square_request_object.repetitions = 1

rospy.loginfo("Doing 2nd Service Call...")
result2 = move_bb8_in_square_service_client(move_bb8_in_square_request_object)
rospy.loginfo(str(result2))

rospy.loginfo("END of Service call...")
