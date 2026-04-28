import random
import threading
import time
import tkinter as tk
from tkinter import simpledialog

# --- AUTO-FIX FOR RUNTIME ERROR ---
# This replaces the standard input() with a popup window so the .exe doesn't crash
def input(prompt):
    root = tk.Tk()
    root.withdraw()  # Hide the main tiny window
    answer = simpledialog.askstring("Greenhouse Gambit", prompt)
    root.destroy()
    return answer

# --- YOUR ORIGINAL CODE BELOW (WITH MINIMAL TWEAKS) ---

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
        credits_scene()

def introduction():
    print("Yeah, maybe the average escape room you have to do in class is easy.")
    print("Like it wasn't fun at all, just an assignment you had to do...")
    print("Well, you regret that because your teachers decided to keep you in a FUN escape room right before summer starts.")
    print("You're now stuck in a room of the school nobody knows, but the planners of this room.")
    print("You must use your cunningness & skills to unlock the code before the last bell rings...")
    print("Have a great time in this awesome escape room!")
    print("")
    begin_game()

def credits_scene():
    print("This was made by David for Flavortown.")
    print("Thanks to my colleagues (a.k.a. rubber duckies for decoding), Robert & Richard Duckington.")
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

def playerChoices():
    global puzzles_done, keys_order, keys_content
    print(f"The time is {ingame_time[0]} hours and {ingame_time[1]} minutes at {ingame_time[2]}.")
    print(f"You have {ingame_time[3]} minutes to escape the greenhouse escape room.\n")
    print("Here are your choices:")
    print("1. Do a puzzle")
    print("2. Wait for someone to help you")
    print("3. Try to break open the door\n")
    
    try:
        choice = int(input("What is your choice (enter 1-3)? "))
    except (ValueError, TypeError):
        choice = 0

    while choice not in [1, 2, 3]:
        print("Answer properly...\n")
        try:
            choice = int(input("What is your choice (enter 1-3)? "))
        except (ValueError, TypeError):
            choice = 0

    print("")
    if choice == 1:
        if len(keys_order) == 0:
            keys_order = list(range(8))
            random.shuffle(keys_order)
        new_puzzle = puzzle_finder()
        puzzles_done.append(new_puzzle)
        if len(puzzles_done) >= 8:
            finallock(keys_content, ingame_time[3])
        else:
            playerChoices()
    elif choice == 2:
        waiting_event()
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
    else:
        puzzle8(puzzle_key)

def puzzle1(puzzle_key):
    numbers = []
    total_sum = 0
    product = 1
    lessThanFive = 0
    guessesUsed = 0

    for i in range(4):
        digit = random.randint(1, 9)
        numbers.append(digit)
        total_sum += digit
        product *= digit
        if digit < 5:
            lessThanFive += 1

    parity = "odd" if numbers[1] % 2 == 1 else "even"
    firstHalfAverage = (numbers[0] + numbers[1]) / 2

    print("There appears to be a safe with a 4-digit lock.")
    print("Provided on the display are 6 hints:")
    print(f"1. The sum of the digits are {total_sum}.")
    print(f"2. The product of the digits are {product}.")
    print(f"3. The number of digits below 5 are {lessThanFive}.")
    print(f"4. The second number is {parity}.")
    print(f"5. The average of the first two numbers are {firstHalfAverage}.")
    print("6. No digits are zero.\n")

    while True:
        guess = input("What is your guess? ")
        if len(guess) != 4:
            print("Please enter exactly 4 digits.")
            continue

        correct_position = 0
        for i in range(4):
            if int(guess[i]) == numbers[i]:
                correct_position += 1

        if correct_position >= 4:
            print(f"You got the code! The letter is {puzzle_key}.\n")
            break
        elif guessesUsed >= 2:
            print("The code has reset! Try again later!\n")
            break
        else:
            print(
                f"No, that's not it. You have {correct_position} digits in correct place.\n"
            )
            guessesUsed += 1

def puzzle2(puzzle_key):
    pins = [3739, 2486, 4985]
    clues = [
        "Fma ask jcecpgq, qapgzc rpcq qcnrck rpcq lmtck.",
        "Uk rwgfgu nggt guvq, guetkdg fqu ewcvtq qejq ugku.",
        "Ex gnfxkh t ltblbk xlm jntmkx gxny anbm vbgj.",
    ]
    chosen = random.randint(0, 2)
    print("You see a random jumble of letters on paper:")
    print(clues[chosen] + "\n")
    guess = int(input("Enter the PIN: "))
    while guess != pins[chosen]:
        print("Try again!")
        guess = int(input("Enter the PIN: "))
    print(f"You found the PIN! The letter displayed is {puzzle_key}.\n")


def puzzle3(puzzle_key):
    print("Solve the riddle about change...")
    guess = input("What's the 8-letter, all lowercase answer? ")
    while guess != "calculus":
        print("Try again!\n")
        guess = input("What's the 8-letter, all lowercase answer? ")
    print(f"You solved the riddle! The letter is {puzzle_key}.\n")


def puzzle4(puzzle_key):
    questions = [
        "What color can be combined to purple to make blue?",
        "What color can be combined to red to make yellow?",
        "What color is made from combining blue with itself?",
        "What color combined to itself makes green?",
        "What is yellow + blue?",
    ]
    answers = ["green", "yellow", "orange", "red", "green"]
    chosen = random.randint(0, 4)
    print(questions[chosen])
    guess = input(
        "Enter your guess (red, orange, yellow, green, blue, or purple): "
    )
    while guess != answers[chosen]:
        print("Try again!")
        guess = input(
            "Enter your guess (red, orange, yellow, green, blue, or purple): "
        )
    print(f"Nice job! The letter is {puzzle_key}.\n")


def puzzle5(puzzle_key):
    print("Read the love letter and extract the NATO words...")
    guess = input("What's the code (all lowercase, use spaces, hint: NATO)? ")
    while guess != "flavortown is the best":
        print("Try again!")
        guess = input(
            "What's the code (all lowercase, use spaces, hint: NATO)? "
        )
    print(f"Kudos to you! The letter is {puzzle_key}.\n")


def puzzle6(puzzle_key):
    encrypted = [
        "... .--. .-. .. -. --.",
        ".-- --- .-. -..",
        "-- --- .-. ... .",
        ".... .- -.-. -.- .. -. --.",
    ]
    decrypted = ["spring", "word", "morse", "hacking"]
    chosen = random.randint(0, 3)
    print(f"Morse code: {encrypted[chosen]}")
    guess = input("What is the decrypted message? (all lowercase) ")
    while guess != decrypted[chosen]:
        print("Try again!")
        guess = input("What is the decrypted message? (all lowercase) ")
    print(f"Congrats! The letter is {puzzle_key}.\n")


def puzzle7(puzzle_key):
    size = random.randint(1, 2)  # Simplified from your code
    answer = (
        random.randint(1, 9) if size == 1 else random.randint(10, 99)
    )
    print(f"Brute force a {size}-digit number!")
    guess = int(input("What is the number? "))
    while guess != answer:
        print("Try again!")
        guess = int(input("What is the number? "))
    print(f"Lucky duck! The letter is {puzzle_key}.\n")


def puzzle8(puzzle_key):
    encrypted = [
        "15-24-11-1-12-10-6-23-24-17-6-12-11",
        "otpeuqfkgn",
        "JiMxMTQ7JiMxMDU7JiMxMTU7JiMxMDU7JiMxMTA7JiMxMDM7",
    ]
    decrypted = ["randomization", "exposition", "rising"]
    chosen = random.randint(0, 2)
    print(f"Multistep encryption: {encrypted[chosen]}")
    guess = input("What is the code? ")
    while guess != decrypted[chosen]:
        print("Try again!")
        guess = input("What is the code? ")
    print(f"Nice job! The letter is {puzzle_key}.\n")


def randomize_finallock(filename):
    possible_locks = ["absolute", "academic", "backdrop", "balanced", "calendar", "campaign", "capacity", "daughter", "facility", "identity"]
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