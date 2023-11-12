def print_upper_words(words_list, starting_letter_set):
    """
    Parameters:
    words_list: an array of words
    starting_letter_set: a set of letters that the words may begin with

    Output:
    Each word printed in uppercase followed by a new line if word's first letter belongs in letter set
    """
    for word in words_list:
        if word[0] in starting_letter_set:
            print(word.upper() + "\n")

# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "bowser", "cat"], {"h", "y", "c"})