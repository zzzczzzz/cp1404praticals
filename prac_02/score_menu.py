"""
MENU = (G)et valid score, (P)rint result, (S)how stars, (Q)uit

print MENU
get user option

while user option != Q

    if user option == G
    get score function, get_valid_score
        while score is less than 0 or greater than 100
            print invalid score
            get score
        return score

    if user option == P
    print result function, print_result
        if score >= 90:
            result = "Excellent"
        elif score >= 50:
            result = "Passable"
        else:
            result = "Bad"
        return result

    if user option == S
    show stars function, show_stars
        stars = '*' * score
        return stars

    print MENU
    get user option

print "farewell"

"""

MENU = "(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    print(MENU)
    user_option = input("Choose your option: ").upper()
    score = ""

    while user_option != "Q":
        if user_option == "G":
            score = get_valid_score()

        elif user_option == "P":
            if score == "":
                print("Get a valid score first.")
            else:
                result = check_result(score)
                print(f"Your result is {result}")

        elif user_option == "S":
            if score == "":
                print("Get a valid score first.")
            else:
                stars = show_stars(score)
                print(stars)

        print(MENU)
        user_option = input("Choose your option: ").upper()

    print("Farewell")

def get_valid_score():
    """Get user score and error check"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def check_result(score):
    """Check result and return result"""
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

def show_stars(score):
    """Return stars based on the input score"""
    stars = '*' * score
    return stars

if __name__ == '__main__':
    main()

