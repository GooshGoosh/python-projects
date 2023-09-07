#!usr/bin/env python3


# anagrams.py - Asks the user to provide to separate text inputs and
# checks if the given inputs are anagrams. An anagram is a word
# formed by rearranging the letters of a word, using all the original
# letters exactly once.


def check_for_anagram(wordOne, wordTwo):
    # Create a list of characters for each word and sort it. Then,
    # join the letters of each list together into two separate
    # lists.
    wordOne = ''.join(sorted(list(wordOne)))
    wordTwo = ''.join(sorted(list(wordTwo)))

    # Ensure that the words are not empty and check if the words
    # are equal (contain the same characters).
    if len(wordOne) > 0 and wordOne == wordTwo:
        print("Anagrams.")
    else:
        print("Not anagrams.")


def main():
    # Get the 2 text inputs and change them to all lowercase letters
    # as well as replace any whitespaces with nothing.
    first = input("Enter the first word: ").lower().replace(' ', '')
    second = input("Enter the second word: ").lower().replace(' ', '')

    check_for_anagram(first, second)


if __name__ == "__main__":
    main()
