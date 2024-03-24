from guitar import Guitar

def main():
    """Read file of guitar.csv, save as Guitar objects and print"""
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    for guitar in guitars:
        print(guitar)

    new_guitar = add_new_guitar()
    guitars.append(new_guitar)

    print("guitar list with new guitar")
    for guitar in guitars:
        print(guitar)

    write_guitars_to_csv('guitars.csv', guitars)


def add_new_guitar():
    """add new guitar to my guitar list"""
    name = input("Enter guitar name: ")
    year = int(input("Enter year: "))
    cost = float(input("Enter cost: "))
    return Guitar(name, year, cost)

def write_guitars_to_csv(file_name, guitars):
    """Write list of guitars to a CSV file."""
    out_file = open('guitars.csv', 'w')
    out_file.write("Name,Year,Cost\n")
    for guitar in guitars:
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    out_file.close()


main()
