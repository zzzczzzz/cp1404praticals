for i in range(1, 21, 2):
    print(i, end=' ')
print()

# question A

for i in range(0, 101, 10):
    print(i, end=' ')
print()

# question B

for i in range(20, 0, -1):
    print(i, end=' ')
print()

# queestion C

number_of_stars = int(input("Number of stars : "))
for i in range(number_of_stars):
    print('*', end=' ')
print()

# question D

number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars + 1):
    for k in range(i):
        print('*', end='')
    print()
