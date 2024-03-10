"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    subject_detail = print_subject_detail(data)
    print(subject_detail)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    list_of_lists = [] # create empty list to append parts
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        list_of_lists.append(parts) # append parts creating list of lists
    input_file.close()
    return list_of_lists

def print_subject_detail(data):
    """retrieve lists of subject from data, prints details of each"""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")





main()