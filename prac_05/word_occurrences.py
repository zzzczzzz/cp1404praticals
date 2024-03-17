"""
main function
    ask for user input
    word count function
    print the text
    print count of words function

word count function
    create empty dictionary
    convert user input into lists
    using for loop, count the words then store as dictionary

print function
    sort the dictionary
    calculate max length among words
    using for loop, print each of word and their counts
    align printed text to max length
"""

def main():
    """main function get input"""
    user_string = input("Enter a string: ")
    word_to_count = count_word_occurrences(user_string)
    print("Text:", user_string)
    print_word_counts(word_to_count)


def count_word_occurrences(user_string):
    """convert string to list, count words then store as dictionary"""
    word_to_count = {}
    words = user_string.split()

    for word in words:
        word_to_count[word] = word_to_count.get(word, 0) + 1

    return word_to_count


def print_word_counts(word_to_count):
    """sort the output then prints"""
    max_length = max(len(word) for word in word_to_count.keys())
    sorted_counts = sorted(word_to_count.items())
    for word, count in sorted_counts:
        print(f"{word:<{max_length}} : {count}")


main()
