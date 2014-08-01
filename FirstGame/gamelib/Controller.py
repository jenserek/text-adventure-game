from itertools import chain
class Controller():

    def __init__(self, story, player):
        story.controller = self
        self.story = story
        self.player = player
        self.actions = {
            "show_stats": "show_stats",
            "stats": "show_stats",
            "stat": "show_stats",
            "show_stat": "show_stats",
            "exit": "exit"
            }
        self.keywords = {}

    def welcome(self):
        print("Welcome to Perfection!\n")

    def ask_player_race(self):
        while True:
            print("Race options:")
            print("Human:   {:<2}".format("Favors Strength"))
            print("Elf:     {:<2}".format("Favors Intellect"))
            print("Wolf:    {:<2}\n".format("Favors Agility"))
                  
            self.player.race = input("Which do you choose? ")
            self.player.race = self.player.race.strip().lower()
            if self.player.race.startswith("h"):
                print("You've chosen Human!\n")
                self.player.race = "human"
                self.keywords["race"] = self.player.race
                self.player.strength += 5
                break
            elif self.player.race.startswith("e"):
                print("You've chosen Elf!\n")
                self.player.race = "elf"
                self.keywords["race"] = self.player.race
                self.player.intellect += 5
                break
            elif self.player.race.startswith("w"):
                print("You've chosen Wolf!\n")
                self.player.race = "wolf"
                self.keywords["race"] = self.player.race
                self.player.agility += 5
                break
            else:
                print("That is not a supported race!")

    def ask_player_gender(self):
        while True:
            question = input("Male or Female? ").strip().lower()

            if question.startswith("m"):
                self.player.gender = "male"
                print("Yeah!!\n")
                if self.player.race == "wolf":
                    self.player.agility -= 2
                break
            elif question.startswith("f"):
                self.player.gender = "female"
                print("Oh ok, well that's fine.\n")
                if self.player.race == "human":
                    self.player.strength -= 2
                break
            else:
                print("That is not a supported gender!")
            
    def ask_player_skill(self):
        while True:
            print("Skillsets:\nAssassin\nArcher\nWarrior\nMage\n")
            self.player.skill = input("Which do you choose? ").strip().lower()
            if self.player.skill.startswith("as"):
                print("You've picked Assassin!\n")
                self.player.skill = "assassin"
                self.keywords["skill"] = self.player.skill
                self.player.agility += 5
                break
            elif self.player.skill.startswith("ar"):
                print("You've picked Archer!\n")
                self.player.skill = "archer"
                self.keywords["skill"] = self.player.skill
                self.player.agility += 3
                self.player.intellect += 3
                break
            elif self.player.skill.startswith("w"):
                print("You've picked Warrior!\n")
                self.player.skill = "warrior"
                self.keywords["skill"] = self.player.skill
                self.player.strength += 5
                break
            elif self.player.skill.startswith("m"):
                print("You've chosen Mage!\n")
                self.player.skill = "mage"
                self.keywords["skill"] = self.player.skill
                self.player.intellect += 5
                break
            else:
                print("That is not a support skillset!\n")
            
    def ask_player_name(self):
        self.player.name = input("What is your character name? ").strip()
        self.keywords["name"] = self.player.name

        if len(self.player.name) > 6:
            print("Danggg what a large name you have!")
        else:
            print("Short and sweet, I like it!")

    def ask_player_age(self):
        while True:
            self.player.age = int(input("\nHow old are you? "))
            self.keywords["age"] = self.player.age
            self.player.ageConditional = ""
            
            if  self.player.age < 25:
                print("Wow, you're starting young! That's great!")
                self.player.ageConditional = "Young"
                self.player.strength += 1
                self.player.agility += 1
                break
            elif self.player.age >= 25 and self.player.age < 50:
                print("Good! You probably have some sort of basic training then!")
                self.player.ageConditional = "Experienced"
                self.player.strength += 2
                self.player.intellect += 1
                break
            elif self.player.age >= 50:
                print("Better late than never!")
                self.player.ageConditional = "Wise"
                self.player.strength -= 1
                self.player.agility -= 1
                self.player.intellect += 2
                break
            else:
                print("That is not a supported age!")

    def ask_player_characteristics(self):
        self.ask_player_race()
        self.ask_player_gender()
        self.ask_player_skill()
        self.ask_player_name()
        self.ask_player_age()
    
    def show_stats(self):
        if self.player.strength != self.player.baseStrength:
            self.player.health = self.player.strength * 5
        print("Health:    {:>2}".format(self.player.health))
        print("Strength:  {:>2}".format(self.player.strength))
        print("Intellect: {:>2}".format(self.player.intellect))
        print("Agility:   {:>2}".format(self.player.agility))

    def tell(self, text):
        print(text.format(**self.keywords))

    def enter(self):
        while True:
            enter = input("\nSay Enter when ready to proceed: ").lower()
            if enter.startswith("e"):
                print("\n*Entering Throwback Alley*")
                break
            else:
                print("\nError")

    def ready(self):
        while True:
            ready = input("\nAre you ready? ").lower()
            if ready.startswith("y") or ready.startswith("r"):
                self.story.give_first_quest()
            else:
                print("\nError")
            

    def start_game(self):
        self.enter()
        self.story.introduce_game()
        self.story.introduce_player()
        print("\nBefore you begin, here are your base stats!")
        print("You can view stats again at any time\n")
        self.show_stats()
        self.ready()

    def prompt(self, actions = {}, string = "\nWhat would you like to do? "):
        valid_actions = dict(chain(actions.items(), self.actions.items()))
        while True:
            action = input(string).strip().lower()
            action = "_".join(action.split())
            if action not in valid_actions:
                print("Sorry, can't do that.")
            else:
                action = valid_actions[action]
                if action in self.actions:
                    method = getattr(__class__, action)
                    if not method:
                        raise Exception("Action {} not implemented".format(action))
                    method(self)

    def exit(self):
        raise SystemExit


