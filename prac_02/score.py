"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

#score = float(input("Enter score: "))
#if score < 0:
#    print("Invalid score")
#else:
#    if score > 100:
#        print("Invalid score")
#    if score > 50:
#        print("Passable")
#    if score > 90:
#    print("Excellent")
#if score < 50:
#    print("Bad")

"""
get score

if score is less than 0 or greater than 100
    print invalid

else if score is greater than 90
    print excellent

else if score is greater than 50
    print passable

else
    print bad
"""

import random
def main():
    score = float(input("Enter score: "))
    result = check_result(score)
    print(result)

    """generate random score"""
    random_score = random.randint(0, 100)
    print(f"random score is : {random_score}")

    """additional function for result of random score"""
    result_of_random_score = check_result(random_score)
    print(f"result of random score is : {result_of_random_score}")


def check_result(score):
    """checks result and returns result"""
    if score < 0 or score > 100:
        result = "Invalid"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
