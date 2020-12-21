from Player import Player
import pandas as pd

#from Player import Player
#from NewGame import NewGame



score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
          "x": 8, "z": 10}


class Word:
    def __init__(self, word):
        self.is_valid = False
        self.word_value = 0
        self.word = word

    def is_valid(self):
        word = self
        with open("words_alpha.txt") as f:
            wordlist = f.read().splitlines()
        wordlist = set(wordlist)
        if word in wordlist:
            print("True")
        else:
            print("This word is not in our dictionary, Try again.")

        
    def set_value(self):
        return sum(score[letter] for letter in self)
