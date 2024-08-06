class Warrior:
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        print(f"{self.name} attacks with a sword!")

class Medic:
    def __init__(self, name):
        self.name = name
    
    def heal(self):
        print(f"{self.name} heals wounds.")

class Soldier(Warrior, Medic):
    def __init__(self, name):
        Warrior.__init__(self, name)
        Medic.__init__(self, name)

# Create an instance of the Soldier class
soldier = Soldier("John")

# Call methods from both parent classes
soldier.attack()  # Output: John attacks with a sword!
soldier.heal()    # Output: John heals wounds.
