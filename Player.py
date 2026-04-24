
# Class is a blueprint of an object
class Player:

    #initializer consturctor
    def __init__(self): # must use self
        self.name = "" 
        self.inventory = []
        self.health = 100
        self.game_over = False

    def set_name(self, name):
        #encapsulation allows us to evaluate what the user uses for name
        if name == "":
            self.name = "Default Name"
        else:
            self.name = name 

    def ask_player_name(self):
        self.set_name(input("What is your name, adventurer?\n"))

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} was added to your inventory")
    
    def is_item_in_inventory(self, item):
        if item in self.inventory:
            return True
        return False
    
    def get_player_health(self):
        print(f"{self.name} your health is now {self.health}")

    def take_damage(self, damage_amount):
        self.health -= damage_amount
        self.get_player_health()