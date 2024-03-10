"""
list of numbers = []
get 5 numbers from user
list of numbers.append number
print first number
print last number
print smallest number
print largest number
print average
"""

list_of_numbers = []
for i in range(5):
    number = int(input("Enter number : "))
    list_of_numbers.append(number)

print(f"The first number is {list_of_numbers[0]}")
print(f"The last number is {list_of_numbers[-1]}")
print(f"The smallest number is {min(list_of_numbers)}")
print(f"The largest number is {max(list_of_numbers)}")
print(f"The average of the numbers is {sum(list_of_numbers) / len(list_of_numbers)}")




usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name_of_user = input("Enter your name : ")

if name_of_user in usernames:
    print("Access granted")
else:
    print("Access denied")