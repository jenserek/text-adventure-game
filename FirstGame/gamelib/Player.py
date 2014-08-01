from random import randrange
class Player:

    def __init__(self):
        self.name = ""
        self.gender = ""
        self.age = ""
        self.race = ""
        self.skill = ""
        self.ageConditional = ""
        self.strength = randrange(8, 10)
        self.baseStrength = self.strength
        self.intellect = randrange(8, 10)
        self.agility = randrange(8, 10)
        self.health = self.strength * 5
        
                
