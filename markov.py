"""Generate Markov text from text files."""

import sys
<<<<<<< HEAD
=======

>>>>>>> 02c91a5c08de88c3be4544c14138935e7ba4a0ce
file_path = sys.argv[1]
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    return open(file_path).read()


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.
file_path = sys.argv[1] + sys.argv[2]keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}

    # words = text_string.split()

    # for i in range(len(words) - 2):

    #     pair_word = (words[i], words[i+1])

    #     chains[pair_word] = chains.get(pair_word,[]) + [words[i+2]]
    n_gram = int(input("How many words in your key?> "))

    words = text_string.split()

    n_list = []

    i = 0

<<<<<<< HEAD
    for i in range(0,len(words)-1): 
        '''for every index in words'''

        if i == len(words)-n_gram:  
            '''break this loop when we arrive at the index for which, if a key was made
            with n_gram # of words, there are no longer enough words to populate a value.
            e.g. for a bigram out of 6 words, this would break at i == 5 because
            key = (5,6) and value is now out of range.'''
            break
        n_list = words[i:i+n_gram]

        '''create a key from slicing words list. slice size is determined by n_gram.'''
        n_tuple = tuple(n_list)
        '''crate a tuple out of n_list so it can be a key in a dict.'''
        chains[n_tuple] = chains.get(n_tuple,[]) + [words[i+n_gram]]
        '''add the tuple as a key in dict chains. if the key doesn't already exist,
        create an empty list as the value. Then add the next sequential word in words
        that comes after the last string in the key.'''
        i += 1
    print(chains)
=======
    while len(n_list) < n_gram:
        n_list.append("word_" + str(i))
        i+1

   #print(n_list)
    while i in range(i,i+1):#range(0+i,i+n_gram): 
        if i == len(words):
            break
        print(i,range(i,i+1), n_gram, "test")
        n_list = words[i:len(n_list)]
        print(n_list)
        if len(n_list) == n_gram:
            print("nlist",n_list)
            n_tuple = tuple(n_list)

            chains[n_tuple] = chains.get(n_tuple,[]) + [words[i+n_gram]]
        i += 1

    #print("chains",chains)

>>>>>>> 02c91a5c08de88c3be4544c14138935e7ba4a0ce
    return chains

def make_text(chains):
    """Return text from chains."""

    words = []

<<<<<<< HEAD
    pair = choice(list(chains.keys()))
    print("THIS IS THE PAIR",pair)
=======
    #print("words", words)
    pair = choice(list(chains.keys()))

    #print("pair", pair)

>>>>>>> 02c91a5c08de88c3be4544c14138935e7ba4a0ce

    while pair in chains:

        value = chains[pair]

<<<<<<< HEAD
        second_word = choice(value)

        words.append(second_word)

        pair = (pair[1], second_word)

    return " ".join(words)




# Open the file and turn it into one long st
#ring
input_text = open_and_read_file(file_path)
=======
        #print("value", value)

        second_word = choice(value)
        #print("second word", second_word)
        words.append(second_word)
        #print("words",words)
        pair = (pair[1], second_word)
        #print("pair",pair)


    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long st
#ring
input_text = open_and_read_file(input_path)
>>>>>>> 02c91a5c08de88c3be4544c14138935e7ba4a0ce

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
