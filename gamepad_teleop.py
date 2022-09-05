#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from adafruit_motorkit import MotorKit
from sensor_msgs.msg import Joy

def callback(data):

	if ((data.axes[2]-1) / -2) != 0:
		motor1 = (data.axes[2]-1) / 2
		motor2 = (data.axes[2]-1) / -2
	else:
		motor1 = (data.axes[5]-1) / -2
		motor2 = (data.axes[5]-1) / 2

	if data.buttons[5] == 1:
		motor1 = 1
		motor2 = 1
	
	if data.buttons[4] == 1:
		motor1 = -1
		motor2 = -1
	
	kit.motor1.throttle = motor1
	kit.motor2.throttle = motor2
	

def listener():
	global kit
	kit = MotorKit()

	rospy.Subscriber("joy", Joy, callback)
	rospy.init_node('gamepad_teleop')
	rospy.spin()

if __name__ == '__main__':
	listener()
