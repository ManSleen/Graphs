from util import Stack, Queue  # These may come in handy
import string


# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None

# Build our graph!

# Load word list
f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())
# words are nodes, one-letter-apart words are edges

# Do a BFS from start word to end word


def get_neighbors(word):
    string.ascii_lowercase
    alphabet = list(string.ascii_lowercase)
    # Return all words from word list that are 1 letter different
    neighbors = []
    # For each letter int he word,
    # For each letter in the alphabet
    # Change the word letter to the alhpabet letter
    # If the new word is in the word_set:
    # Add it to neighbors
    string_word = list(word)
    for i in range(len(string_word)):
        for letter in alphabet:
            list_word = list(string_word)
            list_word[i] = letter
            w = "".join(list_word)
            if w != word and w in word_set:
                neighbors.append(w)

    return neighbors


def find_ladders(begin_word, end_word):
    # Create a queue
    q = Queue()
    # Enqueue A PATH TO the starting_word
    q.enqueue([begin_word])
    # Create a visited set
    visited = set()
    # While queue is not empty,
    while q.size() > 0:
        # Dequeue the next path
        path = q.dequeue()
        # Grab the last word from the path
        v = path[-1]
        # If it's not been visited:
        if v not in visited:
            if v == end_word:
                return path
            visited.add(v)
            for neighbor in get_neighbors(v):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
        # Check if word is the end_word
        # If so, return path
        # If it's not been visited:
        # Mark it as visited
        # Enqueue a path to each neighbor


print(find_ladders("happy", "angry"))
# print(get_neighbors("sail"))
