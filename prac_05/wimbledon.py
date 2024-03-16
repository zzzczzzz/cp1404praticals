"""
main function
    file name
    subfunctions

read file function
    create empty dictionary
    create empty set

    read the file
    using for loop, extract datas that are needed and store them in dictionary and set

print champions function
    prints champions using dictoinary

print countries function
    prints winner countries sorted using set,
"""
def main():
    "main function containg subfuction and file name"
    filename = "wimbledon.csv"
    champions, countries = read_wimbledon_data(filename)
    print_champions(champions)
    print_countries(countries)


def read_wimbledon_data(filename):
    """create empty dictionary, empty set, read the file, strip the file, convert to string
     then extract needed information and store as dictionary and set"""
    champion_to_win = {}
    countries = set()

    with open(filename, "r", encoding="utf-8-sig") as file:
        for line in file:
            data = line.strip().split(',')
            champion = data[2]
            countries.add(data[1])
            countries.add(data[3])

            champion_to_win[champion] = champion_to_win.get(champion, 0) + 1

    return champion_to_win, countries


def print_champions(champion_to_win):
    """prints champions, using dictionary"""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_win.items():
        print(f"{champion} {wins}")


def print_countries(countries):
    """print winner countries sorted, and tells how many countries has won"""
    print(f"These {len(countries)} countries have won Wimbledon:")
    winner_countries = ', '.join(sorted(countries))
    print(winner_countries)


main()
