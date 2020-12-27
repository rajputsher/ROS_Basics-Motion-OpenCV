#!/usr/bin/env python

import  rospy
from ros_basics_tutorials.msg import IoTSensor
import random

pub = rospy.Publisher('iot_sensor_topic', IoTSensor, queue_size=10)

rospy.init_node('iot_sensor_publisher_node',anonymous=True)

rate = rospy.Rate(1)

i=0
while not rospy.is_shutdown():
    iot_sensor = IoTSensor()
    iot_sensor.id =1
    iot_sensor.name = "iot_parking_01"
    iot_sensor.temperature = 24.5 + (random.random()*2)
    iot_sensor.humidity = 36.8 + (random.random()*2)
    rospy.loginfo("I publish:")
    rospy.loginfo(iot_sensor)
    pub.publish(iot_sensor)
    rate.sleep()
    i=i+1