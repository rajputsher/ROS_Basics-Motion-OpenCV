#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def chatter_callback(message):
    #This method is called everytime the new message is received
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", message.data) 

def listener():
    #initialize the node and make it unique
    rospy.init_node('listener', anonymous=True)
    # create a object to subscribe as done while creating publisher object
    rospy.Subscriber("chatter",String, chatter_callback)
    # To listen , we need to use spin() method
    rospy.spin()


if __name__ == '__main__':
    listener()