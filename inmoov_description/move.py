#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def Move_Robot():
 rospy.init_node('Move_Robot', anonymous=True)
 vel_msg = Twist()
 pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
 rate = rospy.Rate(10)
 # Define the robot parameters required for simulation:
 r = 0.05 #the wheel radius in meters
 l = 0.26 #the wheel base distance in meters (width of robot)
 # Define the wheel velocity:
 Wr =10 #Angular velocity of the right wheel
 Wl = 5 #Angular velocity of the left wheel
 #Calculate the linear and angular velocities
 v = (r/2) * (Wr + Wl) #Linear Velocity
 w = (r/l) * (Wr - Wl) #Angular Velocity

 vel_msg.linear.x = v #Linear Velocity
 vel_msg.linear.y = 0.0
 vel_msg.linear.z = 0.0
 vel_msg.angular.x = 0.0
 vel_msg.angular.y = 0.0
 vel_msg.angular.z = w #Angular Velocity

 while not rospy.is_shutdown():
        pub.publish(vel_msg)
 

if __name__ == '__main__':
        Move_Robot()
