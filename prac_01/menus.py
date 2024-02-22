"""

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

MENU = """(H)ello\n(G)oodbye\n(Q)uit"""

user_name = input("Enter name : ")
print(MENU)
user_choice = input(">>> ").upper()

while user_choice != "Q":
    if user_choice == "H":
        print(f"Hello {user_name}")
        print(MENU)

    elif user_choice == "G":
        print(f"Goodbye {user_name}")
        print(MENU)

    else:
        print("Invalid choice")

    user_choice = input(">>> ").upper()
print("Finished")