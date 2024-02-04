# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name is "rock":
        return 0
    elif name is "Spock":
        return 1
    elif name is "paper":
        return 2
    elif name is "lizard":
        return 3
    elif name is "scissors":
        return 4
    else:
        print "Invalid name"
        return -1


def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number is 0:
        return "rock"
    elif number is 1:
        return "Spock"
    elif number is 2:
        return "paper"
    elif number is 3:
        return "lizard"
    elif number is 4:
        return "scissors"
    else:
        print "Invalid number"
        return -1
    

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ""

    # print out the message for the player's choice
    print "Player chooses", player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", comp_choice

    # compute difference of comp_number and player_number modulo five
    comp_diff = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if comp_diff is 1 or comp_diff is 2:
        print "Computer wins!"
    elif comp_diff is 3 or comp_diff is 4:
        print "Player wins!"
    else:
        print"Player and computer tie!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


