from guitar import Guitar

def main():
    """Main function to manage the program."""
    print("My guitars!")

    my_guitars = []

    my_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    my_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    new_guitar = get_guitar_details()
    my_guitars.append(new_guitar)

    print("These are my guitars:")
    for i, guitar in enumerate(my_guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth ${guitar.cost:.2f}{vintage_string}")

def get_guitar_details():
    """Function to get details of a guitar from the user."""

    my_guitars = []
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_made_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        print(f"{guitar_name} ({guitar_made_year}) : ${guitar_cost:.2f} added.")
        my_guitars.append(Guitar(guitar_name, guitar_made_year, guitar_cost))
        guitar_name = input("Name: ")

    return Guitar("", 0, 0)


main()
