from Board import *
import pygame
import random

class GameObject:

   """
   Parent class
   """

   def __init__(self, x=0, y=0):

      self.x = x
      self.y = y

   def update(self):
      pass

   def draw(self):
      pass


class Rack(GameObject):

   """
   Class to create the rack
   """

   def __init__(self, board, rack_size, bag, x=0, y=0):

      super().__init__(x, y)
      self.board = board
      self.rack_size = rack_size
      self.components = []
      self.bag = bag
      # self.rack_list in the old money
      self.tiles = []
      # To check if letter is being dragged
      self.dragging = None

   def start(self):

      """
      Function to start the rack
      """

      self.fill_rack()
      # For loop to space the tiles in rack out side by side
      for i in range(len(self.components)):
         self.components[i].x = i*50 + self.x

   # Taken from V1.0
   def fill_rack(self):
      
      # Calculate amount of tiles needed for full rack
      missing_tiles = self.rack_size - len(self.tiles)
      # Get tiles from bag
      new_tiles = self.bag.get_tiles(missing_tiles)
      # Add tiles to rack
      for tile in new_tiles:
         self.add_tile(tile[0], tile[1])

   def add_tile(self, tile, value):

      # Add tiles to rack
      self.tiles.append(tile)
      # Add tiles to components
      self.components.append(Tile(self, tile, value, 40, 40, self.x, self.y))

   def update(self):
      for c in self.components:
         c.update()

   def draw(self, game_display):
      for c in self.components:
         c.draw(game_display)

   def drop_tile(self, tile):
      self.dragging = None
      dropped = self.board.add_tile(tile)