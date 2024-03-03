# tasak 1
"""
get name
open file name.txt as write
write user name on name.txt
close name.txt
"""

user_name = input("Enter name : ")

out_file = open("name.txt", "w")
print(user_name, file=out_file)
out_file.close()

# task 2

"""
open name.txt as read
user_name = read name.txt
print hello user name
"""

in_file = open("name.txt", "r")
user_name = in_file.read()
in_file.close()
print(f"Your name is {user_name}")

# task 3

"""
open file number.txt as read
first line number = file.readline
second line number = file.readline
total = first line number + second line number
print total
"""

in_file = open("numbers.txt", "r")

first_line_number = int(in_file.readline())
second_line_number = int(in_file.readline())
in_file.close()

total = first_line_number + second_line_number
print(total)

# task 4

"""
open numbers.txt as read
total = 0
for line in numbers.txt
    total += i
print total
"""

in_file= open("numbers.txt", "r")

total = 0
for line in in_file:
    total += int(line)
in_file.close()

print(total)