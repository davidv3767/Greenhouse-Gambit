# Needed imports
import random

def endings_sorter(time):
    # Sorts out which ending based on time left
    ending = "none"
    if (time < 0):
        ending = "bad"
    elif (time < 180):
        ending = "okay"
    elif (time < 300):
        ending = "good"
    else:
        ending = "great"
    print_endings(ending, time)

# Prints endings & time left
def print_endings(ending_type, time):
    print("You escaped with " + str(time) + " minutes left. You find yourself in the greenhouse.")
    if (ending_type == "bad"):
        # Ending 1: Bad
        # Prints first half
        print("You rush to open the door, hoping school hasn't ending.")
        print("Unfortunately, the door is locked.")
        print("You know everyone rushes home, and nobody wants to stay at school.")
        print("")
        # Randomizes for second half
        lucky = random.randint(1, 7)
        # Print if safe or not
        if (lucky % 2 == 0):
            # Safe
            print("Luckily, your parents were able to find you in the greenhouse within a few hours...")
            print("")
            print("YOU WIN... kind of")
        else:
            # Not safe
            print("For the next 3 months, the greenhouse is your home...")
            print("It is your only source  of food, water, energy, and otehr things to help you live...")
            print("")
            print("Get ready for 3 months of suffering...")
            print("And 9 months of school...")
            print("Before you can finally sit back and take a break.")
            print("")
            print("YOU LOSE")
    elif (ending_type == "okay"):
        # Ending 2: Okay
        print("You got out and collided with an afternoon class.")
        print("The teacher looks unsurprised... you know he is in on the secret.")
        print("The students are surprised, though, and start chatting amongst themselves.")
        print("Taking a gambit, you pull the teacher aside.")
        print("As a reward, you receive some money ($20).")
        print("Missing all but 1 or 2 periods, your last day ends okay... and you're ready for summer to begin!")
        print("")
        print("YOU WIN")
    elif (ending_type == "good"):
        # Ending 3: Good
        print("You are able to get out by lunch time.")
        print("Your first afternoon teacher notices you in class...")
        print("...you know he is in on the plan.")
        print("Taking a gambit, you ask the teacher if he knows about the escape room.")
        print("He does, and gives you $100 as a prize!")
        print("")
        print("YOU WIN")
    elif (ending_type == "great"):
        # Ending 4: Great
        print("When you enter the greenhouse, the teacher is shocked there...")
        print("He asks you, 'Heads or tails?'")
        reply = input("You reply: ")
        print("")
        while (reply != "heads" and reply != "tails"):
            print("Answer properly...")
            reply = input("You reply: ")
            print("")
        luckiness = random.randint(1, 2)
        if (luckiness % 2 == 0 and reply == "heads"):
            print("You earn the best model laptop.")
            print("")
            print("YOU WIN")
        elif (luckiness % 2 == 1 and reply == "tails"):
            print("You earn the best model laptop.")
            print("")
            print("YOU WIN")
        else:
            print("You earn $500.")
            print("")
            print("YOU WIN")
    else:
        print("Game glitched....")