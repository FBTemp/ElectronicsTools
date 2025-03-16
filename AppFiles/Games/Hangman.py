"""
Hangman
Made for ElectronicsTools.
Made by: Fast-Blast

ElectronicsTools:
https://github.com/FBTemp/ElectronicsTools/tree/main
Fast-Blast:
https://linktr.ee/fast_blast

©2025 Fast-Blast. All rights reserved.
"""

# imports
import random

# HANGMAN states
HANGMAN = [
    """
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
"""]

# imports words from a text file
with open("AppFiles/GameAssets/words.txt", 'r') as file:
    num_lines = sum(1 for line in file)
WORDS = []
wordsFile = open("AppFiles/GameAssets/words.txt", "r")
wordsFile.seek(0)
wordsFile.readline()  # skip the first line (comment line)
for x in range(num_lines-1):
    WORDS.append(wordsFile.readline().strip())
wordsFile.close()

# initialise variables
word = random.choice(WORDS) # the word to be guessed
so_far = "-" * len(word) # one dash for each letter in word to be guessed
wrong = 0 # counter to keep track of number of wrong guesses
used = [] # list to keep track of letters already guessed
max_wrong = 7
