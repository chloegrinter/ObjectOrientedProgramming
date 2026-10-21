class Monster:
    def __init__(self,name,energy,gold,level,keys):
        self.name = name
        self.energy = energy
        self.gold = gold
        self.level = level
        self.keys = keys

    def explore(self):
        self.energy -= 15
        self.gold += 10
        
    def rest(self):
        if self.energy == 100:
            return
        else:
            self.energy += 25
    def findKey(self):
        self.keys += 1
        
    def levelUp(self):
        if self.gold < 100:
            print("Too Little Gold")
        else:
            self.gold -= 100
            self.level += 1
    def displayStats(self):
        print("Name: " + str(self.name))
        print("Energy: " + str(self.energy))
        print("Gold: " + str(self.gold))
        print("Level: "+ str(self.level))
        print("Keys: " + str(self.keys))
        
monster_1 = Monster("Shadow", 100, 0, 1, 0)
monster_2 = Monster("Blaze", 80, 25, 2, 1)
monster_3 = Monster("Frost", 90, 10, 1, 2)

monster_1.explore()
monster_1.rest()
monster_1.findKey()
monster_1.levelUp()
monster_1.displayStats()

#Remember to include self in class functions
