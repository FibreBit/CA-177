import random, string
import pygame
from Bag import *
from Rack import *

white = (255, 255, 255)

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

class Game:

   """
   Class that starts the game
   """

   def __init__(self):
      # Title of window
      self.title = "My Scrabble"
      # Width of window
      self.width = 1200
      # Height of window
      self.height = 840
      # List of things to update every frame
      self.components = []
      # Game over condition
      self.game_over = False

      # Initialise pygame module
      pygame.init()
      # Create window
      self.game_display = pygame.display.set_mode((self.width, self.height))
      # Set title
      pygame.display.set_caption(self.title)
      self.clock = pygame.time.Clock()

   def start(self):
      
      """
      Function to start game
      """

      tile_size = 40
      board_size = 15

      # Make Bag
      bag = Bag()
      board = Board(15, self.width/2-(tile_size*board_size/2), 40)
      board.start()
      self.components.append(board)

      # Make Rack (will have to do one per player)
      rack = Rack(board, 7, bag, self.width/2-(tile_size*board_size/2), self.height-(tile_size*2))
      rack.start()
      self.components.append(rack)

   def run(self):

      """
      Function to run the game
      """

      self.start()

      self.game_over = False
      # While game is not over, keep going
      while not self.game_over:

         # Update all components
         self.update()
         # Draw all components onto screen
         self.draw()

         # Update screen
         pygame.display.update()
         self.clock.tick(30)

   def update(self):

      """
      Function to update components
      """
      # For every event in thr window
      for event in pygame.event.get():
         # pygame.QUIT = Red X at top of window
         if event.type == pygame.QUIT:
            self.game_over = True

      for c in self.components:
         c.update()

   def draw(self):

      """
      Function to draw game
      """
      # Colour background blue
      self.game_display.fill((0, 0, 255))

      # Draw all components
      for c in self.components:
         c.draw(self.game_display)


class Board(GameObject):

   """
   Class to create the board object
   """


   def __init__(self, board_size, x=0, y=0):
      super().__init__(x, y)
      self.board_size = board_size
      self.components = []

   def start(self):

      """
      Function to make the board   
      """
      # Lists of all the bonus squares

      # Red
      triple_word = [   (0,0), (7, 0), (14, 0),
                        (0,7), (14, 7),
                        (0, 14), (7, 14), (14, 14)]
      # Dark blue 
      triple_letter = [ (5, 1), (9, 1),
                        (1, 5), (5, 5), (9, 5), (13, 5), 
                        (1, 9), (5, 9), (9, 9), (13, 9),
                        (5, 13), (9, 13)]
      # Orange
      double_word = [   (1, 1), (2, 2), (3, 3), (4, 4), (10, 10), (11, 11), (12, 12), (13, 13),
                        (13,1), (12, 2), (11, 3), (10, 4), (4, 10), (3, 11), (2, 12), (1, 13)]
      # Light blue
      double_letter = [ (3, 0), (11, 0),
                        (6, 2), (8, 2),
                        (0, 3), (7, 3), (14, 3),
                        (2, 6), (6, 6), (8, 6), (12, 6),
                        (3, 7), (11, 7),
                        (2, 8), (6, 8), (8, 8), (12, 8),
                        (0, 11), (7, 11), (14, 11),
                        (6, 12), (8, 12),
                        (3, 14), (11, 14)]

      center_square = [(7,7)]

      tile_size = 40


      # For loops to draw the board line by line
      for x in range(self.board_size):
         for y in range(self.board_size):

            # Checking for special square

            if (x, y) in triple_word:
               colour = (255, 0, 0)
            elif (x, y) in triple_letter:
               colour = (0, 0, 255)
            elif (x, y) in double_word:
               colour = (255, 150, 150)
            elif (x, y) in double_letter:
               colour = (150, 150, 255)
            elif (x, y) in center_square:
               colour = (255, 255, 0)
            else:
               colour = (220, 200, 190)

            # Creating Square class

            square = Square(colour, tile_size, tile_size, (self.x + x*tile_size), (self.y + y*tile_size))
            # Adding each square to components
            self.components.append(square)


   def update(self):
      for c in self.components:
         c.update()

   def draw(self, game_display):
      for c in self.components:
         c.draw(game_display)

   def add_tile(self, tile):
      for square in self.components:
         if square.rect.collidepoint((tile.x + tile.width/2, tile.y + tile.height/2)):
            tile.x = square.x
            tile.y = square.y


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

class Square(GameObject):

   """
   Class that creates Squares for the game
   """

   def __init__(self, colour, width, height, x=0, y=0):

      super().__init__(x, y)
      self.colour = colour
      self.width = width
      self.height = height

   def draw(self, game_display):

      """
      Function to draw the squares onto the screen
      """

      # Defining size of rectangle
      self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

      # Draw rectangle
      pygame.draw.rect(game_display, self.colour, self.rect)
      # Draw black outine around rectangle
      pygame.draw.rect(game_display, (0,0,0), self.rect, 1)


class Tile(Square):

   """
   Class to create the letter tiles
   """

   def __init__(self, rack, letter, value, width, height, x=0, y=0):
      super().__init__((225, 150, 0), width, height, x, y)
      self.letter = letter
      self.value = value
      self.font = pygame.font.Font("freesansbold.ttf", 20)
      # We bring the rack class in so that we don't accidently drag multiple tiles as once.
      # This hopefully makes more sense after reading the update function
      self.rack = rack

   def update(self):

      """
      Function to update the position of the tiles, which can be moved by drag and drop
      """
      
      # Get the mound position
      mouse = pygame.mouse.get_pos()
      # Get the mouse click status
      click = pygame.mouse.get_pressed()
      # Defining self.rect, a rectangle
      self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

      # If the click is being pressed
      if click[0] == 1:
         # If mouse collides with a rectangle, i.e. if mouse is inside tile and If the Tile is not already being dragged
         if self.rect.collidepoint(mouse) and self.rack.dragging == None:
               self.rack.dragging = self
      # Else, if the click is not being pressed
      elif self.rack.dragging == self:
            # Stop dragging the tile
            self.rack.drop_tile(self)

      # Voodoo magic that makes the snapping into place work
      if self.rack.dragging == self:
         self.x = mouse[0] - self.width/2
         self.y = mouse[1] - self.height/2



   def draw(self, game_display):
      super().draw(game_display)

      """
      Function to draw the Tiles
      """

      # Set the font
      text_surface = self.font.render(self.letter, True, white)
      # Draw image to screen
      game_display.blit(text_surface, (self.x, self.y))

      text_surface = self.font.render(str(self.value), True, white)
      game_display.blit(text_surface, (self.x+20, self.y+20))
