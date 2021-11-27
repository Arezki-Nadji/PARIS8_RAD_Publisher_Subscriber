#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def PublishMethod():
	pub = rospy.Publisher('talker',Float64,queue_size=10) #defining the publisher by topic message type
	rospy.init_node('publish_node',anonymous = True) #defining the ros node -publisher node
	rate = rospy.Rate(10) #10hz #frequency at witch the publishing
	while not rospy.is_shutdown():
		publishingString = 32  #variable
		rospy.loginfo("DAta is being sent") #to print on the terminal
		pub.publish(publishingString) #publishin
if __name__=='__main__':
	try:
		PublishMethod()
	except rospy.ROSInterruptException:
		pass