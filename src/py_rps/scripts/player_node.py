#!/usr/bin/env python
import random
import rospy
from std_msgs.msg import String

def player():
    pub = rospy.Publisher('topic_rps', String, queue_size=1)
    rospy.init_node('node_player', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        opts = ['rock', 'paper', 'scissors']
        choice = random.choice(opts)
        rospy.loginfo("player sending: {}".format(choice))
        pub.publish(choice)
        rate.sleep()

if __name__ == '__main__':
    try:
        player()
    except rospy.ROSInterruptException:
        pass
