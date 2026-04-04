# Needed imports
import random
from greenhousegambit_endings import endings_sorter

def randomize_finallock(filename):
    possible_locks = []
    # Trying to open file
    try:
        with open(filename, 'r') as file:
           # If the file is found
           possible_locks = [line.strip().lower() for line in file.readlines()]
    except FileNotFoundError:
        # If file isn't found
        print("The file is not found.")
    # Randomizes a password
    chosen = random.randint(0, 9)
    password = possible_locks[chosen]
    # Stores keys
    keys = []
    for i in range(8):
        new_key = password[i]
        keys.append(new_key)
    return keys

def finallock(keys, time):
    # Prints instructions
    print("Congratulations! You are almost done!")
    print("")
    print("You should have 8 letters.")
    print("They are scrambled, and your goal is to unscramble them to get an 8-letter word.")
    print("Once this is done, you escape!")
    print("")
    # Checking mechanic
    final_guess = input("What is the final lock's password? ")
    print("")
    finalguess_correct = True
    for i in range(8):
        if keys[i] != final_guess[i]:
            finalguess_correct = False
    # Providing feedback and repeating checking mechanic if needed
    while (finalguess_correct == False):
        print("You're so close...try again!")
        final_guess = input("What is the final lock's password? (8 letters only) ")
        print("")
        finalguess_correct = True
        for i in range(8):
            if keys[i] != final_guess[i]:
                finalguess_correct = False
    print("You have finished the escape room!")
    print("")
    endings_sorter(time)