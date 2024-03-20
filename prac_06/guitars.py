from guitar import Guitar

def main():
    """Main function to manage the program."""
    print("My guitars!")

    guitars = []

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    new_guitar = get_guitar_details()
    guitars.append(new_guitar)

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:.2f}{vintage_string}")

def get_guitar_details():
    """Function to get details of a guitar from the user."""
    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    return guitars[0] if guitars else Guitar("", 0, 0)


main()
