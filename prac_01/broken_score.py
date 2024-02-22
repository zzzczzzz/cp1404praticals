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

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")

