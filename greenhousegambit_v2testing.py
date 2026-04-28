import random

# This is puzzle #9 -- you thought school could escape you early?
def puzzle9():
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
    print("Kudos to you! You've unlocked the letter...")

# This is puzzle #10 -- the newspaper riddles
def puzzle10():
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
    print("Congrats! The letter is... ")

# This is puzzle #11 -- more patterns!
def puzzle11():
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
    print("Congrats! The letter is... ")

# This is puzzle #12 -- one that finally fits the THEME (greenhouse)
def puzzle12():
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
    print("Congrats! The letter is... ")
