import random

class Bag():

    def __init__(self, bag_size=100):
        """
        Function to Initialise The Bag Class by setting tile_count and tile_score to it's initial values
        """
        # added S and T instead of two blank tiles
        self.bag_size = bag_size
        self.tile_count = {"A" : 9,"B" : 2,"C" : 2,"D" : 4,"E" : 12,"F" : 2,"G" : 3,"H" : 2,"I" : 9,"J" : 1,"K" : 1,"L" : 4,"M" : 2,"N" : 6,"O" : 8,"P" : 2,"Q" : 1,"R" : 6,"S" : 5,"T" : 7,"U" : 4,"V" : 2,"W" : 2,"X" : 1,"Y" : 2,"Z" : 1}
        self.tile_score = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10}

    def size(self):
        # use this for end_game
        """
        Function to end the game based on tile_count
        """
        return sum(self.tile_count.values())        
    
    def put_tiles(self, letter_list):
        """
        Function that takes a letter_list and adds the letter present into the bag 
        by updating tile_count for the Bag
        """
        for letter in letter_list:
            if letter in self.tile_count:
                self.tile_count[letter] += 1
            else:
                self.tile_count[letter] = 1


    def get_tiles(self, letter_amount):
        """
        Function that returns a list with letters equal to letter_amount and updates
        tile_count accordingly
        """
        assert letter_amount <= self.size()
        assert letter_amount >= 0
        final_letters = []

        # loop to repeat the letter selection process 
        for _ in range(letter_amount):
            
            # Chooses a letter from the keys present in tile_count
            letter = random.choice(list(self.tile_count.keys()))
            value = self.tile_score[letter]
            self.tile_count[letter] -= 1

            # Lowers the value of that letter and tile and removes it from the 
            # dicttionary if the resulting value happens to be zero
            if self.tile_count[letter] == 0:
                del self.tile_count[letter]
            final_letters.append((letter, value))
        
        return final_letters