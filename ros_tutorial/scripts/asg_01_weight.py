#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from ros_tutorial.msg import Cylinder

density = 0

density_found = False

def density_callback(data):
    global density
    global density_found
    density = data.data
    density_found = True

def calculate_weight():
    if density_found:
        global density
        weight = density * 9.81 
        weight_pub.publish(weight)
        
rospy.init_node("weight")
rospy.Subscriber("/density", Float64, density_callback)
weight_pub = rospy.Publisher('/weight', Float64, queue_size=10)

while not rospy.is_shutdown():      
	calculate_weight()
	rospy.sleep(0.1)
