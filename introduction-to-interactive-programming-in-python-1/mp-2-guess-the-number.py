# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

secret_number = 0
guess_count = 7
game_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global guess_count
    global secret_number
    
    secret_number = random.randrange(0, game_range)
    if game_range is 100:
        guess_count = 7
    else:
        guess_count = 10
    
    print "New game. Range is [0," + str(game_range) + ")"
    print "Number of remaining guesses is " + str(guess_count)
    print
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global game_range
    
    game_range = 100
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global game_range
    
    game_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guess_count
    
    print "Guess was " + guess
    guess_number = int(guess)
    
    guess_count = guess_count - 1
    print "Number of remaining guesses is " + str(guess_count)
    
    if guess_count is 0 and secret_number is not guess_number:
        print "You ran out of guesses.  The number was " + str(secret_number)
        print
        new_game()
        return
    
    if secret_number is guess_number:
        print "Correct!"
        print
        new_game()
    elif secret_number > guess_number:
        print "Higher!"
        print
    else:
        print "Lower!"
        print
    
# create frame
frame = simplegui.create_frame('Guess The Number', 300, 300)

# register event handlers for control elements and start frame
inp = frame.add_input('Guess', input_guess, 200)
button_rand_100 = frame.add_button('Guess 0 to 100', range100, 200)
button_rand_1000 = frame.add_button('Guess 0 to 1000', range1000, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
