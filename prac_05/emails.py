"""
main
    user data = empty dictionary
    get email
    while email is not empty
        get name from first part of email using extract name function
        confirm if it is their name
        if it is their name, store name as value to email

        if not, ask for their name and store name as value to email

        get email

    using for loop, print name and email
"""

def main():
    """main function get user input, create empty dictionary prints output"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation == '' or confirmation == 'y':
            email_to_name[email] = name
        else:
            name = input("Name: ").title()
            email_to_name[email] = name

        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """extract estimated name from email address"""
    name_in_email = email.split('@')[0].replace('.', ' ').title()
    return name_in_email


main()
