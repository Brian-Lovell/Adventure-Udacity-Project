import time
import random


# Prints strings one character at time, with a slower pause between lines.
def print_slow(string):
    time.sleep(3)
    for char in string:
        print(char, end='', flush=True)
        time.sleep(0.03)


# Prints strings all at once, with a faster pause between lines.
def print_fast(string):
    time.sleep(2)
    print(string)


# Validates user input
def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_fast("You don't have any other choice!")


# Location functions
def wreckage_location(items):
    print_fast("You searched the wreckage, but there are no survivors. \n")
    if "Blaster_Rifle" in items:
        print_fast("You don't find anything else.")
    else:
        print_fast("You find a functional blaster rifle!")
        items.append("Blaster_Rifle")


def canyon_location(items):
    print_slow("You explore the canyon cautiously...\n")
    print_fast("You are ambushed by enemy droids! \n")
    response = valid_input("Do you fight or retreat? \n",
                           ["fight", "retreat"])
    if "fight" in response:
        fight(items)
    elif "retreat" in response:
        ground_location(items)


# Introduction string.
def get_intro():
    print_slow("You and your fellow troopers are riding in an airship, hanging"
               " on tightly to the overhead handle bars. \n")
    print_slow("The side doors open, and wind whips by as your"
               " ship flies into the battefield! \n")
    print_slow("Enemy fire causes your ship to shudder! \n")
    print_slow("Suddenly your pilot yells: \n"
               """ "We're hit, prepare for impact!" \n""")
    print_slow("Your ship crashes! \n")
    print_slow("You get knocked out!\n")
    time.sleep(5)
    print_slow("You wake up on the ground with none of your gear. \n")
    print_slow("You look around,"
               " you see the wreckage of your ship close by.\n")
    print_slow("Thick black smoke billows from the wreckage. \n")


# Exploration, player has to choose where to go.
def ground_location(items):
    print_fast("You are in a canyon,"
               " one way is blocked by your ship. \n")
    print_fast("The other way looks clear,"
               " but several large rocks could be hiding the enemy.\n")
    response = valid_input("Search the wreckage or explore the canyon? \n",
                           ["search", "explore"])
    if "search" in response:
        wreckage_location(items)
    elif "explore" in response:
        canyon_location(items)
    print_fast("Where do you want to go now?")
    ground_location(items)


def fight(items):
    # Combat! Need the blaster rifle to win!
    enemy_list = ["Small Droid", "Large Droid", "Medium Droid"]
    enemy = random.choice(enemy_list)
    attack_string = "A {} appears from behind a rock!"
    victory_string = "You fire your Blaster Rifle and defeat the {}!"
    defeat_string = "You attempt martial combat but the {} defeats you!"
    print_fast(attack_string.format(enemy))
    if "Blaster_Rifle" in items:
        print_fast(victory_string.format(enemy))
        print_fast("You have escaped the canyon and find rescue!")
        play_again()
    else:
        print_fast(defeat_string.format(enemy))
        print_fast("You have been defeated!")
        play_again()


# Asks the player if they would like to play again
def play_again():
    time.sleep(2)
    response = valid_input("Would you like to try again? (y/n)", ["y", "n"])
    if "y" in response:
        main()
    elif "n" in response:
        exit()


# Engage!
def main():
    items = []
    get_intro()
    ground_location(items)


main()
