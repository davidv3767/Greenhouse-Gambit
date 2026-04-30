import random
import threading
import time
import tkinter as tk
from tkinter import simpledialog

# This replaces the standard input() with a popup window so the .exe doesn't crash
def input(prompt):
    root = tk.Tk()
    root.withdraw()  # Hide the main tiny window
    answer = simpledialog.askstring("Greenhouse Gambit", prompt)
    root.destroy()
    return answer

puzzles_done = []
keys_order = []
ingame_time = [8, 0, "AM", 450]  # [Hour, Minute, AM/PM, Minutes Left]
keys_content = []

def welcome():
    print("Welcome to the Greenhouse Gambit!")
    start_menu()

def start_menu():
    print("Please choose an option: ")
    print("1. Start")
    print("2. Credits")
    # Added a try-except here to handle non-integer inputs gracefully
    try:
        start_choice = int(input("What would you like to choose (type 1-2)? "))
    except (ValueError, TypeError):
        start_choice = 0
        
    print("")
    if start_choice == 1:
        introduction()
    else:
        credits()

def introduction():
    print("Yeah, maybe the average escape room you have to do in class is easy.")
    print("Like it wasn't fun at all, just an assignment you had to do...")
    print("Well, you regret voicing that out loud (long story, don't ask) that because your teachers decided to keep you in an actually FUN escape room right before summer starts.")
    print("You're now stuck in a room of the school nobody knows, but the planners of this room.")
    print("You must use your cunningness, luckiness & skills to decipher the code before the last bell rings...")
    print("Have a great time in this awesome escape room!")
    print("")
    begin_game()

def credits():
    print("This was made by David for Flavortown.")
    print("Thanks to my colleagues (a.k.a. rubber duckies for decoding), Robert & Richard Duckington.")
    print("Last but not the least, thanks to my family & those who have inspired me to code for the past year.")
    print("")
    start_menu()


def begin_game():
    global keys_content
    # Note: Ensure "greenhousegambit_finalpasswordbank.txt" is in the same folder as your .exe
    keys_content = randomize_finallock("greenhousegambit_finalpasswordbank.txt")
    timer_thread = threading.Timer(1.0, update_ingametime)
    timer_thread.daemon = True
    timer_thread.start()
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


def waiting_event():
    print("You wait.")
    luck = random.randint(1, 100)
    if (luck == 37 or luck == 73) and ingame_time[3] >= 0:
        print("You got lucky, and your friends came to save you.")
        print("THE END: YOU WON")
    else:
        print("Nobody came to save you.\n")
        playerChoices()

def break_open():
    very_goodluck = random.randint(1, 1000)
    if very_goodluck == 737:
        print("You somehow broke through.")
        print("THE END: YOU WON")
    else:
        print("You failed to break through.\n")
        playerChoices()


def update_ingametime():
    global ingame_time
    ingame_time[1] += 1
    if ingame_time[1] >= 60:
        ingame_time[0] += 1
        ingame_time[1] = 0
    if ingame_time[0] > 12:
        ingame_time[0] = 1
        ingame_time[2] = "PM" if ingame_time[2] == "AM" else "AM"
    ingame_time[3] -= 1
    timer_thread = threading.Timer(1.0, update_ingametime)
    timer_thread.daemon = True
    timer_thread.start()

def puzzle_finder():
    # Get available puzzles that haven't been done
    available_puzzles = [i for i in range(1, 9) if i not in puzzles_done]
    puzzle_num = random.choice(available_puzzles)

    # Fetch corresponding key
    content_num = keys_order.index(puzzle_num - 1)
    puzzle_key = keys_content[content_num]

    puzzle_sorter(puzzle_num, puzzle_key)
    return puzzle_num

# This function sorts out the choosing of puzzles
def puzzle_sorter(puzzle_num, puzzle_key):
    if puzzle_num == 1:
        puzzle1(puzzle_key)
    elif puzzle_num == 2: 
        puzzle2(puzzle_key)
    elif puzzle_num == 3:
        puzzle3(puzzle_key)
    elif puzzle_num == 4:
        puzzle4(puzzle_key)
    elif puzzle_num == 5:
        puzzle5(puzzle_key)
    elif puzzle_num == 6:
        puzzle6(puzzle_key)
    elif puzzle_num == 7:
        puzzle7(puzzle_key)
    elif puzzle_num == 8:
        puzzle8(puzzle_key)
    elif puzzle_num == 9:
        puzzle9(puzzle_key)    
    elif puzzle_num == 10:
        puzzle10(puzzle_key)
    elif puzzle_num == 11:
        puzzle11(puzzle_key)
    elif puzzle_num == 12:
        puzzle12(puzzle_key)

# This is puzzle #1 -- a 4-digit pin guessing game
def puzzle1(puzzle_key):
    # Variables
    numbers = []
    sum = 0
    product = 1
    lessThanFive = 0
    guessesUsed = 0
    parity = ""
    # Randomization of 4-digit code
    for i in range(4):
        digit = random.randint(1, 9)
        numbers.append(digit)
        sum += digit
        product = digit * product
        if digit < 5:
            lessThanFive += 1
    if numbers[1] % 2 == 1:
        parity = "odd"
    else:
        parity = "even"
    firstHalfAverage = (numbers[0] + numbers[1]) / 2
    # Description about the puzzle
    print("There appears to be a safe with a 4-digit lock.")
    print("Well, you expect there to be one of the eight letters needed to escape inside.")
    print("")
    # Instructions & hints provided
    print("Provided on the display are 6 hints:")
    print("1. The sum of the digits are " + str(sum) + ".") 
    print("2. The product of the digits are " + str(product) + ".")
    print("3. The number of digits below 5 are " + str(lessThanFive) + ".")
    print("4. The second number is " + parity + ".")
    print("5. The average of the first two numbers are " + str(firstHalfAverage) + "." )
    print("6. No digits are zero.")
    print("")
    print("You have 3 guesses before the code resets.")
    print("Good luck!")
    # Ask for user input & give feedback
    while (True):
        guess = int(input("What is your guess? "))
        guessCorrect = guess[0] == numbers[0] and guess[1] == numbers[1] and guess[2] == numbers[2] and guess[3] == numbers[3]
        correct_position = 0
        for i in range(4):
            if int(guess[i]) == numbers[i]:
                correct_position += 1
        if correct_position >= 4:
            print("You got the code! The letter is " + puzzle_key + ".")
            break
        elif guessesUsed >= 2:
            print("The code has reset! Try again later!")
            break
        else:
            print("No, that's not it.")
            print("You have " + str(correct_position) + " digits in the correct place.")
            print("")
            guessesUsed += 1

# This is puzzle #2 -- an encrypted message (no randomization yet)
def puzzle2(puzzle_key):
    # Randomization
    pins = [3739, 2486, 4985]
    clues = ["Fma ask jcecpgq, qapgzc rpcq qcnrck rpcq lmtck.", "Uk rwgfgu nggt guvq, guetkdg fqu ewcvtq qejq ugku.", "Ex gnfxkh t ltblbk xlm jntmkx gxny anbm vbgj."]
    chosen = random.randint(0, 2)
    # Instructions printed
    print("You see a random jumble of letters on a piece of paper picked off the floor.")
    print("The jumble of letters are: ")
    print(clues[chosen])
    print("")
    print("Next to it, beside the wall, is a screen. It says: ")
    # Sets up guessing mechanic
    guess = int(input("Enter the PIN: "))
    print("")
    while (guess != pins[chosen]):
        print("Try again!")
        guess = int(input("Enter the PIN: "))
        print("")
    # After code guessed
    print("You were able to find the PIN!")
    print("The letter displayed is " + puzzle_key + ".")

# This is puzzle #3 -- a riddle to trick
def puzzle3(puzzle_key):
    # Prints riddle
    print("An unfamiliar riddle blocks you from the next letter.")
    print("Here is the riddle: ")
    print("I measure change both fast and slow,")
    print("Where tangents touch and limits grow.")
    print("I find the curve beneath your feet,")
    print("And sum the parts where ends don’t meet.")
    print("With chains I rule, with rules I chain,")
    print("In motion's heart, I leave my stain.")
    print("From Newton’s thought to Leibniz’ pen,")
    print("I map the world again, again.")
    print("In eight strong steps, my name is spelled,")
    print("By minds where math and thought have dwelled.")
    print("Each letter builds what few can see—")
    print("The laws of change and symmetry.")
    print("")
    # Prints extra hint
    print("But another hint is scribbled on the back: ")
    print("If you’re searching for the gates to Flavortown’s domain,")
    print("Look to the math that measures instantaneous change.")
    print("")
    # Guessing mechanic
    guess = input("What's the 8-letter, all lowercase answer? ")
    while (guess != "calculus"):
        print("Try again!")
        print("")
        guess = input("What's the 8-letter, all lowercase answer?")
    print("You solved the riddle!")
    print("The letter shown is " + puzzle_key + ".")

# This is puzzle #4 -- a mix of math, art, and logic
def puzzle4(puzzle_key):
    # Uses arrays to store different questions
    questions = ["What color can be combined to purple to make blue?", "What color can be combined to red to make orange?", "What color is made from combining blue with itself?", "What color combined to itself makes green?", "What is yellow + blue?"]
    answers = ["green", "yellow", "orange", "red", "green"]
    # Randomizes for a specific question/answer pair
    chosen = random.randint(0, 4)
    # Prints introduction 
    print("Change of axioms--the level of mathematics almost no one touches knowingly, but everyone does without knowing...")
    print("Now, we study math without studying math but art... and logic... (with this worksheet you found on the floor)")
    print("")
    print("If red + blue = yellow, ")
    print("and orange + green = yellow, ")
    print("and purple + purple = yellow, ")
    print(questions[chosen])
    print("")
    print("Hint: use ROYGBP")
    guess = input("Enter your guess (red, orange, yellow, green, blue, or purple): ")
    print("")
    while (guess != answers[chosen]):
        print("Try again!")
        guess = input("Enter your guess (red, orange, yellow, green, blue, or purple): ")
        print("")
    print("Nice job!")
    print("The letter is " + puzzle_key + ".")

# This is puzzle #5 -- uses NATO to give you the secret code
def puzzle5(puzzle_key):
    # Prints letter
    print("You find a love letter (yes, in the middle of nowhere) that says the following:")
    print("")
    print("My Dearest,")
    print("I wanted to send you something a bit more off-the-menu today. Our connection is the kind of high-octane magic that most people only dream of finding. When I think about us, I feel like I'm on a permanent road trip through the soul of everything that's good.")
    print("")
    print("To keep our secrets safe, I’ve tucked a little message into this note. Just look for the lead word in each thought:")
    print("")
    print("Foxtrot through my mind whenever I close my eyes. Lima beans might be humble, but our love is a five-star feast. Alpha and omega, you are my beginning and my end. Victor is a title I claim every day just by being yours. Oscar winners couldn't act out a romance this real. Romeo would have been jealous of how we do things. Tangoing with you is the only dance I ever want to do. Oscar-worthy sunsets pale in comparison to your smile. Whiskey is bold, but you’re the kick I really need. November nights are warm as long as you're near. ")
    print("")
    print("India is a long way to go, but I’d walk it for you. Sierra mountains couldn't stand between us.")
    print("")
    print("Tango lessons are on the bucket list, right? Hotel stays and late-night talks are my favorite memories. Echoing your laughter is the best sound I know.")
    print("")
    print("Bravo to us for finding this spark. Echoing my heart's deepest wish: you're the one. Sierra mist and summer rain—you’re that refreshing. Tango forever, just you and me.")
    print("")
    print("You really are the spice of my life.")
    print("")
    print("Yours,")
    print("The Culinary Captain")
    print("")
    # Guessing mechanic
    guess = input("What's the code (all lowercase, use spaces, hint: NATO)? ")
    print("")
    while (guess != "flavortown is the best"):
        print("Try again!")
        guess = input("What's the code (all lowercase, use spaces, hint: NATO)? ")
        print("")
    print("Kudos to you!")
    print("The letter for this puzzle is " + puzzle_key + ".")

# This is puzzle #6 -- some simple morse code
def puzzle6(puzzle_key):
    # Uses arrays to store different decrypted & encrypted messages
    encrypted = ["... .--. .-. .. -. --.", ".-- --- .-. -..", "-- --- .-. ... .", ".... .- -.-. -.- .. -. --."]
    decrypted = ["spring", "word", "morse", "hacking"]
    # Randomizes an integer between 0 & 3 to choose code
    chosen = random.randint(0, 3)
    print("On a piece of paper, it is scribbled: ")
    print(encrypted[chosen])
    print("")
    print("You realize the type of encryption.")
    print("")
    guess = input("What is the decrypted message? (all lowercase) ")
    while (guess != decrypted[chosen]):
        print("Try again!")
        guess = input("What is the decrypted message? (all lowercase) ")
        print("")
    print("Congrats!")
    print("The letter unlocked is " + puzzle_key + ".")

# This is puzzle #7 -- based on brute-force & luck
def puzzle7(puzzle_key):
    # Randomization
    answer = 0
    size = random.randint(1, 10)
    if (size != 1 and size != 2):
        size = 1
    if (size == 1):
        answer = random.randint(1, 9)
    elif (size == 2):
        answer = random.randint(10, 99)
    # Prints details
    print("Escape rooms depend on brute-forcing & luck")
    print("A(n) " + str(size) + "-digit positive number has randomly been chosen.")
    guess = int(input("What is the number? "))
    # Guessing mechanic
    while (guess != answer):
        print("Try again!")
        guess = int(input("What is the number? "))
        print("")
    print("Lucky duck!")
    print("The letter unlocked by your luckiness is " + puzzle_key + ".")

# This is puzzle #8 -- multistep encryption, very hard :)
def puzzle8(puzzle_key):
    # Storing encryted & decryted in arrays
    encrypted = ["15-24-11-1-12-10-6-23-24-17-6-12-11", "otpeuqfkgn", "JiMxMTQ7JiMxMDU7JiMxMTU7JiMxMDU7JiMxMTA7JiMxMDM7"]
    decrypted = ["randomization", "exposition", "rising"]
    # Randomizing question/answer pairs
    chosen = random.randint(0, 2)
    # Printing instructions
    print("Meet the archnemesis of escape room solvers -- multistep encryption!")
    print("")
    print("Your puzzle is: ")
    print(encrypted[chosen])
    # Guessing mechanic
    guess = input("What is the code? ")
    while (guess != decrypted[chosen]):
        print("Try again!")
        guess = input("What is the code? ")
        print("")
    print("Nice job with that hard puzzle!")
    print("The letter unlocked by solving this is " + puzzle_key + ".")

# This is puzzle #9 -- you thought school could escape you early?
def puzzle9(puzzle_key):
    # Store school questions/answers in arrays
    school_questions = ["What's 47 + 52?", "x = (4 * 2) ** 3", "The box of toys _(is/are)_ there."]
    school_answers = ["99", "512", "is"]
    # Randomize question/answer pair
    chosen_pair = random.randint(0, 2)
    # Print instructions
    print("It's the last day of school, of course everyone wouldn't be doing much...")
    print("But you, yes you, still have review to do only if you want to escape...")
    print("")
    print("Your school question is...")
    guess = input(school_questions[chosen_pair])
    print("")
    while (guess != school_answers[chosen_pair]):
        print("Try again!")
        guess = input(school_questions[chosen_pair])
    print("Kudos to you! You've unlocked the letter " + puzzle_key + ".")

# This is puzzle #10 -- the newspaper riddles
def puzzle10(puzzle_key):
    # Prints instructions
    print("You know those logic puzzles in the newspaper every week?")
    print("To unlock the letter, you've got to do one!")
    print("")
    # No randomization, sadly:
    guess = input("There were less than four kids born on the same day, hospital, & room. There were no twins. How were they related, if they were? ")
    print("")
    # Guessing mechanic
    while (guess != "triplets" and guess != "They were triplets."):
        print("Try again! Try using one lowercase word or a simple sentence.")
        guess = input("There were less than four kids born on the same day, hospital, & room. There were no twins. How were they related, if they were? ")
        print("")
    print("Congrats! The letter is " + puzzle_key + ".")

# This is puzzle #11 -- more patterns!
def puzzle11(puzzle_key):
    # Store patterns/missing element in arrays
    patterns = ["⭕ ⭕ ⭕🔺 ⭕ ⭕ ⭕ ?", "🔺 ⭕ 🔺 🔺 ⭕ 🔺 🔺 🔺 ⭕ 🔺 🔺 🔺 🔺 ?", "🟥 🟥 🟥 ⭕ ⭕ ⭕ 🔺 🔺 🔺 🟥 🟥 ⭕ ⭕ 🔺 🔺 🟥 ⭕ ?"]
    answers = ["triangle", "circle", "triangle"]
    # Randomize question/answer pair
    chosen_pair = random.randint(0, 2)
    # Prints instructions
    print("Patterns, patterns, patterns, they are awesome!")
    print("There is a puzzle on colors, but now we're doing shapes!")
    print("")
    print("Your pattern is:")
    print(patterns[chosen_pair])
    print("")
    # Guessing mechanic
    guess = input("Type your answer (circle, square, triangle): ")
    while (guess != answers[chosen_pair]):
        print("Try again! Try using a word, NOT the emoji.")
        guess = input("Type your answer (circle, square, triangle): ")
        print("")
    print("Congrats! The letter is " + puzzle_key + ".")

# This is puzzle #12 -- one that finally fits the THEME (greenhouse)
def puzzle12(puzzle_key):
    # Stores DNA sequences/mRNA transcription in arrays
    sequences = ["ATCGCTAGC", "GCTAGCTAC", "TAGCCTGAA"]
    transcriptions = ["UAGCGAUCG", "CGAUCGAUG", "AUCGGACUU"]
    # Randomize question/answer pair
    chosen_pair = random.randint(0, 2)
    print("This is a greenhouse; let's do some DNA testing!")
    print("In all capital letters, transcribe the following:")
    print(sequences[chosen_pair])
    # Guessing mechanic
    guess = input("Type your answer (all capitals, only A U G C): ")
    while (guess != transcriptions[chosen_pair]):
        print("Try again! Try using only A U G C.")
        guess = input("Type your answer (all capitals, only A U G C): ")
        print("")
    print("Congrats! The letter unlocked by your transcribing is " + puzzle_key + ".")


def randomize_finallock(filename):
    possible_locks = ["hackclub", "breakout", "dungeons", "chambers", "instance", "cabinets", "campfire", "instruct", "absolute", "puzzling"]
    try:
        with open(filename, "r") as file:
            possible_locks = [line.strip().lower() for line in file.readlines()]
    except FileNotFoundError:
        print("File not found. Using default word list.")
    chosen_word = random.choice(possible_locks)
    return list(chosen_word[:8])


def finallock(keys, time_left):
    print("Congratulations! You should have 8 letters.")
    print("They are scrambled. Unscramble them to get an 8-letter word.")

    while True:
        final_guess = input("What is the final lock's password? ").lower()
        if len(final_guess) != 8:
            print("The password must be exactly 8 letters.")
            continue

        # Check if correct
        if list(final_guess) == keys:
            print("You have finished the escape room!\n")
            endings_sorter(time_left)
            break
        else:
            print("You're so close...try again!\n")


def endings_sorter(time_left):
    if time_left < 0:
        ending = "bad"
    elif time_left < 180:
        ending = "okay"
    elif time_left < 300:
        ending = "good"
    else:
        ending = "great"
    print_endings(ending, time_left)


def print_endings(ending_type, time_left):
    print(
        f"You escaped in {time_left} minutes remaining & find yourself in the greenhouse."
    )
    if ending_type == "bad":
        print("You took too long... (Game Over vibes)")
    elif ending_type == "okay":
        print("You got out on time. You receive $20.")
    elif ending_type == "good":
        print("Great timing! You receive $100 prize.")
    elif ending_type == "great":
        print("Amazing speed! You win a high-end laptop!")


# --- GAME START ---
welcome()