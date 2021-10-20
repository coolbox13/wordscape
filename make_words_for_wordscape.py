import itertools
import os
import sys
import re
import streamlit as st

# --------------------------------------------------
# 1. check a list of words against an english dictionary
# 2. return a list of existing and valid english words
# --------------------------------------------------

def check_words(words):
    """
    check a list of words against an english dictionary
    :param words: list of words
    :return: list of existing and valid english words
    """
    valid_words = []
    for word in words:
        if d.check(word):
            valid_words.append(word)
    return valid_words

# --------------------------------------------------
# 1. check a list with words for duplicates and delete them
# --------------------------------------------------

def remove_duplicates(list_of_words):
    """
    :param list_of_words: list of words
    :return: list of words without duplicates
    """
    return list(set(list_of_words))

# --------------------------------------------------
# 1. check a list of words against an imported english dictionary
# 2. return a list of existing and valid english words
# 3. do not use the enchant module
# --------------------------------------------------

def check_word(word):
    """
    check if a word is in the dictionary
    """
    if word in word_list:
        return True
    else:
        return False

def check_words(words):
    """
    check if a list of words is in the dictionary
    """
    valid_words = []
    for word in words:
        if check_word(word):
            valid_words.append(word)
    return valid_words

# --------------------------------------------------
# 1. Create all possible words from 6 given letters passed in a list
# 2. words may be 3 to 6 letters long
# --------------------------------------------------

def create_words(letters, nr_letters):
    """
    Create all possible words from 6 given letters passed in a list
    """
    words = []
    for i in range(3, nr_letters):
        for word in itertools.permutations(letters, i):
            words.append(''.join(word))
    
    deduped_words = remove_duplicates(words)
            
    return deduped_words

# --------------------------------------------------
# 1. ask for a six letter word input
# 2. split the word into separate letters in a list
# --------------------------------------------------

def get_letters():
    word = st.text_input('Enter a six or seven letter word: ', 'herman')
    letters = list(word)
    
    return letters

# --------------------------------------------------
# 1. combine list values in a string variable
# 2. use comma to separate list items
# --------------------------------------------------

def combine_list_values_to_string(list_values):
    return ", ".join(list_values)    

# --------------------------------------------------
# Main:
# --------------------------------------------------

with open('word_list.txt', 'r') as f:
        word_list = f.read().splitlines()

        st.title('Words for Wordscape')

# Main function to get list of words form an input of a six or seven letter word from wordscape

letters = get_letters()
nr_letters = len(letters)+1
words = create_words(letters, nr_letters)
valid_words = check_words(words)
output = combine_list_values_to_string(valid_words)

st.write(output)