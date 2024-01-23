'''
anagrams.py - Asks the user to provide two separate text inputs and checks if the
given inputs are anagrams. An anagram is a word formed by rearranging the letters
of a word, using all the original letters exactly once.
Example: "Dog" is an anagram of "God".
'''


# anagrams.py - Asks the user to provide to separate text inputs and
# checks if the given inputs are anagrams. An anagram is a word
# formed by rearranging the letters of a word, using all the original
# letters exactly once.


def check_for_anagram(word_one, word_two):
    """Takes two words and checks if the words are anagrams of each other.

    Args:
        word_one (str): The first word to compare.
        word_two (str): The second word to compare.
    """
    # Create a list of characters for each word and sort it. Then,
    # join the letters of each list together into two separate
    # lists.
    word_one = ''.join(sorted(list(word_one)))
    word_two = ''.join(sorted(list(word_two)))

    # Ensure that the words are not empty and check if the words
    # are equal (contain the same characters).
    if len(word_one) > 0 and word_one == word_two:
        print("Anagrams.")
    else:
        print("Not anagrams.")


def main():
    """Main function to run the program. Asks the user for two text inputs
    to check if the texts are anagrams of each other.
    """

    # Get the 2 text inputs and change them to all lowercase letters
    # as well as replace any whitespaces with nothing.
    first = input("Enter the first word: ").lower().replace(' ', '')
    second = input("Enter the second word: ").lower().replace(' ', '')

    check_for_anagram(first, second)


if __name__ == "__main__":
    main()
