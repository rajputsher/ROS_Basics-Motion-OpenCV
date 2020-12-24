#!/usr/bin/env python

#subscriber for the topic that will show the location of the robot


#publisher to the topic that will make the robot move



import rospy
from geometry_msgs.msg import Twist 

def move():
    #Create publisher object with Topic name: /turtle1/cmd_vel, message type : geometry_msgs/msg , buffer size of 10
    speed_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    #initialize the node, anonymous flag ensures that the node will be unique
    rospy.init_node('speed_publisher',anonymous=True)
    # Frequency pf 1 msg per second
    rate = rospy.Rate(1) #  1hz

    #As long as roscore is not shutdown
    while not rospy.is_shutdown():
        twist = Twist()
        # use rosmsg show geometry_msgs/Twist to find the msg structure
        twist.linear.x = 1.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0

        twist.angular.x =0.0
        twist.angular.y =0.0
        twist.angular.z =0.0

        #publish the message
        speed_publisher.publish(twist)
        #sleep for 1 sec i.e the frequency set
        rate.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass