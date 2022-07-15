#! /usr/bin/env python

import rospy
import time
import actionlib
from actions_quiz.msg import CustomActionMsgAction, CustomActionMsgFeedback, CustomActionMsgResult
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist


class MoveUpDownClass(object):

    _feedback = CustomActionMsgFeedback()
    _result = CustomActionMsgResult()

    def __init__(self):
        self.action_server = actionlib.SimpleActionServer(
            '/action_custom_msg_as', CustomActionMsgAction, self.goal_callback, False)
        self.action_server.start()
        self.ctrl_c = False
        self.rate = rospy.Rate(10)

    def goal_callback(self, goal):
        action_drone = goal.goal
        success = True

        self.move_vel = Twist()
        self.move_vel.linear.x = 0
        self.move_vel.linear.y = 0
        self.move_vel.linear.z = 0

        self.takeoff_pub = rospy.Publisher(
            '/drone/takeoff', Empty, queue_size=1)
        self.land_pub = rospy.Publisher('/drone/land', Empty, queue_size=1)

        self.stay_pub = rospy.Publisher('/cmb_vel', Twist, queue_size=1)

        self.takeoff_msg = Empty()
        self.land_msg = Empty()

        i = 0

        if action_drone == "TAKEOFF":
            while not i == 3:
                self.takeoff_pub.publish(self.takeoff_msg)
                self._feedback.feedback = action_drone
                self.action_server.publish_feedback(self._feedback)
                time.sleep(1)
                i = i + 1
        if action_drone == "LAND":
            while not i == 3:
                self.land_pub.publish(self.land_msg)
                self._feedback.feedback = action_drone
                self.action_server.publish_feedback(self._feedback)
                time.sleep(1)
                i = i + 1

        if success:
            self.action_server.set_succeeded(self._result)


if __name__ == '__main__':
    rospy.init_node('up_down_drone')
    MoveUpDownClass()
    rospy.spin()
