class Player:
    #Defining the data types
    #You need to pass self or any value to refer to the object
    def __init__(self,HP, Attack, Speed, Height, Width,EXP):
        #Self Represents the object
        #So by having self.HP, we say
        #When an object calls x.HP, return self(0) or self(HP)
        self.HP = HP
        #As you can see, we can change this
        #so when self.atk is called, it returns attack
        self.atk = Attack
        self.spe = Speed
        self.height = Height
        self.w = Width
        self.EXP = EXP
        
    #You can also have functions which are called and are built into this
    #class!
    #You do need to consistently refer to self though
    def stat_total(self):
        #This works because all the stats are defined above
        return self.HP+self.atk+self.spe+self.height+self.w
    def exp_give(self,EXP):
        return self.EXP + EXP
#We assign this variable the class Player defined above
player_1 = Player(50,20,10,10,10,0)
#This will print 50
print(player_1.HP)
#This will print 20
print(player_1.atk)
#This will print 100
print(player_1.stat_total())

#Increases EXP
print(player_1.exp_give(10))
print(player_1.exp_give(20))
