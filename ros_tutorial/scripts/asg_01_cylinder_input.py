#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

rospy.init_node("cylinder_input")
radius_pub = rospy.Publisher("/radius", Float64, queue_size=10)
height_pub = rospy.Publisher("/height", Float64, queue_size=10)
density_pub = rospy.Publisher("/density", Float64, queue_size=10)

radius = float(input("enter radius: "))
height = float(input("enter height: "))
density = float(input("enter density: "))

while not rospy.is_shutdown():
	radius_pub.publish(radius)
	height_pub.publish(height)
	density_pub.publish(density)
	rospy.sleep(0.1)
	
	

