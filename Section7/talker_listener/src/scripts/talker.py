#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    #Create publisher object with Topic name: chatter, message type : str_msgs/msg , buffer size of 10
    pub = rospy.Publisher('chatter', String, queue_size=10)
    #initialize the node, anonymous flag ensures that the node will be unique
    rospy.init_node('talker',anonymous=True)
    # Frequency pf 1 msg per second
    rate = rospy.Rate(1) #  1hz

    i=0
    #As long as roscore is not shutdown
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % i
        rospy.loginfo(hello_str)
        #publish the message
        pub.publish(hello_str)
        #sleep for 1 sec i.e the frequency set
        rate.sleep()
        i=i+1
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass