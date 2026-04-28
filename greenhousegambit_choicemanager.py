# Needed imports
from greenhousegambit_normalpuzzles import puzzle_finder
from greenhousegambit_finalpuzzle import randomize_finallock
from greenhousegambit_finalpuzzle import finallock
from greenhousegambit_endings import endings_sorter
import random
import time
import threading
puzzles_done = []
keys_content = randomize_finallock('greenhousegambit_finalpasswordbank.txt')
keys_order = []
ingame_time = [8, 0, "AM", 450] 
 

# This connects the main file to this file while starting the timer
def begin_game():
    waiting = threading.Timer(1.0, update_ingametime)
    waiting.start()
    playerChoices() 

# This is the main function for the choice menu
def playerChoices():
    print("The time is " + str(ingame_time[0]) + " hours and " + str(ingame_time[1]) + " minutes at " + str(ingame_time[2]) + ".")
    print("You have " + str(ingame_time[3]) + " minutes to escape the greenhouse escape room.")
    print("")
    print("Here are your choices:")
    print("1. Do a puzzle")
    print("2. Wait for someone to help you") 
    print("3. Try to break open the door")
    print("")
    choice = int(input("What is your choice (enter 1-3)? "))
    # Error-proof
    while (choice != 1 and choice != 2 and choice != 3):
        print("Answer properly... ")
        print("")
        choice = int(input("What is your choice (enter 1-3)? "))
    print("")
    # Doing a puzzle
    if (choice == 1):
        # Setting up keys
        if (len(puzzles_done) <= 0):
            for i in range(8):
                new_order = random.randint(0, 7)
                while (new_order in keys_order):
                    new_order = random.randint(0, 7)
                keys_order.append(new_order)
        # Choosing a puzzle to print
        new_puzzle = puzzle_finder(puzzles_done, 12, keys_content, keys_order)
        puzzles_done.append(new_puzzle)
        # If all puzzles are done, do this (else continue)
        if (len(puzzles_done) >= 8):
            finallock(keys_content, ingame_time[3])
        else:
            playerChoices()
    elif (choice == 2):
        waiting()
    else:
        break_open()

# This function helps with choice 2
def waiting():
    print("You wait.")
    luck = random.randint(1, 100)
    if ((luck == 37 or luck == 73) and time[3] >= 0):
        print("You got lucky, and your friends came to save you.")
        print("THE END: YOU WON")
    else:
        print("Nobody came to save you.")
    print("")
    playerChoices()

# This function helps with choice 3
def break_open():
    very_goodluck = random.randint(1, 1000)
    if (very_goodluck == 737):
        print("You somehow broke through.")
        print("THE END: YOU WON")
    else:
        print("You failed to break through.")
    print("")
    playerChoices()

# This function manages in-game time
def update_ingametime():
    # Minutes go up
    ingame_time[1] += 1
    # Hour reset
    if (ingame_time[1] >= 60):
        ingame_time[0] += 1
        ingame_time[1] = 0
    # AM-PM reset
    if (ingame_time[0] > 12):
        ingame_time[0] = 1
        if (ingame_time[2] == "AM"):
            ingame_time[2] = "PM"
        else:
            ingame_time[2] = "AM"
    # Minutes left
    ingame_time[3] -= 1
    # Looping timer
    waiting = threading.Timer(1.0, update_ingametime)
    waiting.start()