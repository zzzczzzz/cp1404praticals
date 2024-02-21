"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
get sales
while sales >= 0
    if sales < 1000, bonus is 10%
    elif sales >= 1000, bonus is 15%
    print bonus
    get sales
do next thing
"""

BONUS_THRESHOLD = 1000
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < BONUS_THRESHOLD:
        bonus_rate = 0.1
    elif sales >= BONUS_THRESHOLD:
        bonus_rate = 0.15
    bonus = sales * bonus_rate

    print(f"your bonus is {bonus}")

    sales = float(input("Enter sales: $"))
