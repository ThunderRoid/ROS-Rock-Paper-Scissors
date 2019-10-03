#!/usr/bin/env python
import random
import rospy
from std_msgs.msg import String

def callback(data):
    computer = random.choice(opts)
    player = data.data

    rospy.loginfo('Player: {}, computer: {}'.format(player, computer))

    if computer == player:
        rospy.loginfo('Tie!')

    elif player == "rock":
        if computer == "paper":
            rospy.loginfo("Player lose! {} covers {}".format(computer, player))
        else:
            rospy.loginfo("Player win! {} smashes {}".format(player, computer))

    elif player == "paper":
        if computer == "scissors":
            rospy.loginfo("Player lose! {} cut {}".format(computer, player))
        else:
            rospy.loginfo("Player win! {} covers {}".format(player, computer))

    elif player == "scissors":
        if computer == "rock":
            rospy.loginfo("Player lose! {} smashes {}".format(computer, player))
        else:
            rospy.loginfo("Player win! {} cut {}".format(player, computer))

    else:
        rospy.loginfo("That's not a valid play. Check your spelling!")

    rospy.loginfo("")

def rock_paper_scissor():
    rospy.init_node('computer_node', anonymous=True)
    rospy.Subscriber('topic_rps', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    opts = ['rock', 'paper', 'scissors']
    rock_paper_scissor()
