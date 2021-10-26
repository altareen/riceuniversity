"""
|-------------------------------------------------------------------------------
| word_wrangler.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Oct 04, 2021
|
| Run:      python3 word_wrangler.py
|
| Description:
| This program implements a simple word scrambling game.
|
"""


#import urllib2
#import codeskulptor
#import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    result = []
    for item in list1:
        if item not in result:
            result.append(item)
    return result

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    result = []
    idx = 0
    jdx = 0
    while idx < len(list1) and jdx < len(list2):
        if list1[idx] < list2[jdx]:
            result.append(list1[idx])
            idx += 1
        else:
            result.append(list2[jdx])
            jdx += 1
    if idx < len(list1):
        result.extend(list1[idx:])
    elif jdx < len(list2):
        result.extend(list2[jdx:])
    return result

def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) == 0:
        return []
    elif len(list1) == 1:
        return list1
    else:
        mid = len(list1)//2
        left = merge_sort(list1[:mid])
        right = merge_sort(list1[mid:])
        return merge(left, right)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return [""]
    else:
        first = word[0]
        rest = word[1:]
        rest_strings = gen_all_strings(rest)
        new_strings = []
        for item in rest_strings:
            letters = list(item)
            for pos in range(len(item)+1):
                letters.insert(pos, first)
                new_strings.append("".join(letters))
                letters = list(item)
        rest_strings.extend(new_strings)
        return rest_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

    
    
