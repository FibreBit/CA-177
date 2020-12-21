from Player import Player
import PIL
from Rules import Rules
import tkinter
from Board import Game

class NewGame:
    def __init__(self):
        self.players = {} #Player dictionary.
        self.total = 1 # Keeps count of the number of active players.
        self.rules = Rules()

    #This function modifys the Rules class with the input of the user.
    def rule_change(self):

        rulescreen = tkinter.Tk()
        rulescreen.title("MyScrabble")
        rulescreen.geometry('400x250+700+400')
        rulescreen.configure(background='#0F0268')
        
        def rule_confirm():
            self.rules.set_board_size(boardsize.get())
            self.rules.set_turn_time_limit(turntime.get())
            self.rules.set_game_time_limit(gametime.get())
            self.rules.set_rack_size(racksize.get())
            print(self.rules.get_details())
            rulescreen.destroy()

        tkinter.Label(rulescreen, text="Board Size:", bg='#0F0268', fg='white', font=("Segoe UI Bold", 13)).place(x=40,y=40)
        tkinter.Label(rulescreen, text="Turn Time:", bg='#0F0268', fg='white', font=("Segoe UI Bold", 13)).place(x=40,y=70)
        tkinter.Label(rulescreen, text="Game Time:", bg='#0F0268', fg='white', font=("Segoe UI Bold", 13)).place(x=40,y=100)
        tkinter.Label(rulescreen, text="Rack Size:", bg='#0F0268', fg='white', font=("Segoe UI Bold", 13)).place(x=40,y=130)
        boardsize = tkinter.Entry(rulescreen)
        boardsize.place(x=240,y=40)
        boardsize.insert(0, self.rules.board_size)
        turntime = tkinter.Entry(rulescreen)
        turntime.place(x=240,y=70)
        turntime.insert(0, self.rules.turn_time_limit)
        gametime = tkinter.Entry(rulescreen)
        gametime.place(x=240,y=100)
        gametime.insert(0, self.rules.game_time_limit)
        racksize = tkinter.Entry(rulescreen)
        racksize.place(x=240,y=130)
        racksize.insert(0, self.rules.rack_size)
        tkinter.Button(rulescreen, font=("Segoe UI Bold", 13), borderwidth=5, text="Confirm Rules", width=15, height=1,  command=rule_confirm).place(x=120, y=180)
        rulescreen.mainloop()

    def play_online(self):
        pass

    def play_local(self):
        
        homescreen.destroy()
        setup = tkinter.Tk()
        setup.title("MyScrabble")
        setup.geometry('450x600+720+200')
        setup.configure(background='#0F0268')

        
        def player_confirm():
            userlist = users.get().split(",")
            usercolours = colours.get().split(",")
            for x in range(0, len(userlist)):
                self.add_player(userlist[x], usercolours[x], "English", x+1)

            for y in range(1, len(userlist)+1):
                print(self.players[y].get_all())
            #######Commands to jump to board go here#####
            scrabble = Game()
            scrabble.run()
            setup.destroy()
        pixelVirtual = tkinter.PhotoImage(width=1, height=1)
        tkinter.Label(setup, bg="#C82323", image=pixelVirtual, width=303, height=88, compound="c").place(x=72, y=48)
        tkinter.Label(setup, text="MyScrabble", font=("Segoe UI Bold", 38), bg="#FF1717", fg="white", image=pixelVirtual, width=293, height=78, compound="c").place(x=76, y=52)
        tkinter.Label(setup, text="Player Names:", bg="#0F0268", fg="white", image=pixelVirtual, width=174, height=33, compound="c", font=("Segoe UI Bold", 20)).place(x=47,y=184)
        tkinter.Label(setup, text="Player Colours:", bg="#0F0268", fg="white", image=pixelVirtual, width=190, height=33, compound="c", font=("Segoe UI Bold", 20)).place(x=47,y=256)
        tkinter.Button(setup, font=("Segoe UI Bold", 13), borderwidth=5, text="Edit Rules",image=pixelVirtual, width=119, height=25, compound="c",  command=test.rule_change).place(x=163, y=455)
    
        users = tkinter.Entry(setup, width=30)
        users.place(x=240,y=200)
        colours = tkinter.Entry(setup, width=28)
        colours.place(x=250, y=270)
        tkinter.Button(setup, font=("Segoe UI Bold", 25), image=pixelVirtual, borderwidth=5, height=68, width=201, text="Start Game", compound="c", command = player_confirm).place(x=121, y=362)
        setup.mainloop()


    # Creates a new player and adds it to the player dictionary.
    def add_player(self, name, player_colour, language, turn):
        new_player = Player(name, player_colour, language, turn) # Creates an object for a player.
        self.players[self.total] = new_player # adds to the player_dict which is a dictionary.
        self.total = self.total + 1 # Increments the player count by one.
        return



###################################################################################################
test = NewGame()



homescreen = tkinter.Tk()
homescreen.title("MyScrabble")
homescreen.geometry('400x600+720+200')
homescreen.configure(background='#0F0268')
pixelVirtual = tkinter.PhotoImage(width=1, height=1)

tkinter.Label(homescreen, bg="#C82323", image=pixelVirtual, width=303, height=88, compound="c").place(x=43, y=48)
tkinter.Label(homescreen, text="MyScrabble", font=("Segoe UI Bold", 38), bg="#FF1717", fg="white", image=pixelVirtual, width=293, height=78, compound="c").place(x=47, y=52)

tkinter.Button(homescreen, font=("Segoe UI Bold", 20), text="Play Online", image=pixelVirtual, borderwidth=5, width=172, height=59, compound="c", command=test.play_local).place(x=102, y=181)
tkinter.Button(homescreen, font=("Segoe UI Bold", 20), text="Play Offline", borderwidth=5,image=pixelVirtual, width=172, height=59, compound="c",  command=test.play_local).place(x=102, y=266)
tkinter.Button(homescreen, font=("Segoe UI Bold", 20), text="Log Out",image=pixelVirtual, borderwidth=5, width=172, height=59, compound="c",  command=test.play_local).place(x=102, y=350)
tkinter.Button(homescreen, font=("Segoe UI Bold", 11), text="Contact Admin",image=pixelVirtual, borderwidth=5, width=129, height=35, compound="c",  command=test.play_local).place(x=129, y=437)
homescreen.mainloop()


