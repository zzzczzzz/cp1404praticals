"""
import random

COUNT OF QUICK PICK = 6
MINIMUM NUMBER = 1
MAXIMUM NUMBER = 45

get number of quick picks from user

for i in number of quick picks
    generate quick pick function
    print quick function

quick pick function
    list for quick pick = []
    while len of quick pick is less than COUNT OF QUICK PICK
        generate a random number
        if generate random numer is not in list
            apeed the number to the list
        sort the list
        return list

print function
    print number in list of quick picks, align width 2


"""

import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
COUNT_OF_NUMBERS = 6

number_of_quick_picks = int(input("How many quick picks? "))

def main():
    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print_quick_pick(quick_pick)


def generate_quick_pick():
    """generate quick picks and make sure numbers do not duplicate and store numbers"""
    quick_pick_stored = []
    while len(quick_pick_stored) < COUNT_OF_NUMBERS:
        generated_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if generated_number not in quick_pick_stored:
            quick_pick_stored.append(generated_number)
        quick_pick_stored.sort()
    return quick_pick_stored


def print_quick_pick(quick_pick):
    """prints quick picks, align in 2 widths"""
    print(" ".join(f"{num:2}" for num in quick_pick))



main()
