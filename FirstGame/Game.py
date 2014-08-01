from gamelib.Controller import Controller
from gamelib.Player import Player
from gamelib.Story import Story

p = Player()
s = Story(p)
c = Controller(s, p)

c.welcome()
c.ask_player_characteristics()
c.start_game()








