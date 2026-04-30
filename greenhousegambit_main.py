# Needed imports
from greenhousegambit_choicemanager import begin_game

# This function introduces you to the game, making sure the welcome message doesn't repeat
def welcome():
    print("Welcome to the Greenhouse Gambit!")
    start_menu()

# This function makes a menu, allowing you to start the game or explore a little bit
def start_menu():
    print("Please choose an option: ")
    print("1. Start")
    print("2. Credits")
    start_choice = int(input("What would you like to choose (type 1-2)? "))
    print("")
    if start_choice == 1:
        introduction()
    else:
        credits()

# This prints out the introduction (some LORE)
def introduction():
    print("Yeah, maybe the average escape room you have to do in class is easy.")
    print("Like it wasn't fun at all, just an assignment you had to do...")
    print("Well, you regret voicing that out loud (long story, don't ask) that because your teachers decided to keep you in an actually FUN escape room right before summer starts.")
    print("You're now stuck in a room of the school nobody knows, but the planners of this room.")
    print("You must use your cunningness, luckiness & skills to decipher the code before the last bell rings...")
    print("Have a great time in this awesome escape room!")
    print("")
    begin_game()

# This prints out the credits, pretty boring here
def credits():
    print("This was made by David for Flavortown.")
    print("Thanks to my colleagues (a.k.a. rubber duckies for decoding), Robert & Richard Duckington.")
    print("Last but not the least, thanks to my family & those who have inspired me to code for the past year.")
    print("")
    start_menu()

welcome()