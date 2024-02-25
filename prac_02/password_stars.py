#import random
#
#low = 1
#high = 100
#secret = random.randint(low, high)
#
#guess = int(input("Guess the secret number : ")
#
#while guess != secret:
#    print("Incorrect")
#    guess = int(input("Guess again: "))
#
#print("got it")

import random

def main():
    low = 1
    high = 15
    secret = random.randint(low, high)

    guess = get_password()

    while guess != secret:
        print_incorrect()
        guess = get_password()

    print("Got it!")

def get_password():
    """get user input of secret number"""
    return int(input("Guess : "))

def print_incorrect():
    """prints incorrect when guess is incorrect"""
    print("Incorrect")

if __name__ == "__main__":
    main()


