class Story:
    
    def __init__(self, player):
        self.player = player
        self.controller = None
        
    def introduce_game(self):
        self.controller.tell('''
Welcome {name} to Throwback Alley! You have come a long ways in order to
finally enter the battle of the Decades! These aren't your typical
decades though. These decades include many mythological creatures;
some that have never been seen before. It will take a lot of
dedication, but you can do it if you just believe! The world depends
on you. You must not fail!''')

    def introduce_player(self):
         if self.player.ageConditional == ("Young"):
             self.controller.tell('''
Since you are {age} years old, this will be new for you, but since you are keen
and adept, you should be able to fit in very nicely. You're a {race} {skill},
which we specifically looked for to fight in this war. In a few moments,
you'll receive your first quest!''')

         elif self.player.ageConditional == ("Experienced"):
             self.controller.tell('''
It looks like you are {age} years old. Although you are not as spry as you used
to be, you are still a great asset to this war. As a {race} {skill}, you'll be
able to bring something to this war that no other person can bring! Get
ready! You will soon receive your first quest!''')

         else:
            self.controller.tell('''
Wow you are {age} years old! You must be one of our older fighters. Don't worry,
for you have had a lot of experience in this cruel world, and you are far more
wise than others in our ranks. You are a {race} {skill} which is perfect for
this war and it should be alot of fun! Prepare to receive your first quest!
''')

    def give_first_quest(self):
        self.controller.tell('''
*A man in a fine looking, silver hooded cloak walks up to you*
Hello {name}. My name is Bruce and I am here to lead you on your journey.

''')
        self.controller.prompt()
