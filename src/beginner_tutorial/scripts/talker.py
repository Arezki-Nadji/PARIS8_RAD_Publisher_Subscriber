#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def PublishMethod():
	pub = rospy.Publisher('talker',String,queue_size=10) #définition du noeud publisher pour le topic et définition du type de message
	rospy.init_node('publish_node',anonymous = True) #initialisation du noeud publisher
	rate = rospy.Rate(10) #10hz #frequence de publication
	while not rospy.is_shutdown():
		publishingString = "THis is being published" #variable
		rospy.loginfo("DAta is being sent") #affichage sur le terminal
		pub.publish(publishingString) #publication sur le topic
if __name__=='__main__':
	try:
		PublishMethod()
	except rospy.ROSInterruptException:
		pass