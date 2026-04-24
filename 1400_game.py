
from Player import Player

def main():
    welcome_player()
    player = Player()
    player.ask_player_name()
    player.add_to_inventory("Ancient Scroll")

    print(f"Welcome, {player.name}! Your journey begins now.")


    while True:
        
        describe_area(player)

        decision = input(" What will you do (1, 2, 3, r, i, q (quit)):").lower()


        match decision:
            case "1":
                explore_the_dark_woods(player)

            case "2":
                explore_the_mountain_pass(player)
            
            case "3":
                explore_the_dark_cave(player)

            case "4":
                if player.is_item_in_inventory("Map"):
                    explore_the_hidden_valley(player)
                else:
                    print("Confused, you stand still, unsure of what to do.")
            
            case "i":
                print(f"{player.name}! This is your inventory")
                print(player.inventory)

            case "r":
                print(f"{player.name}! You read the Ancient Scroll")
                print("""
                In a forest dark and deep, the blade resides in elms tight keep.
                On a mountain high and steep, the pommel is hidden where wise ones sleep.
                In a cave where darkness dwells, avoid the path that reeks and smells.
                In a valley hidden well, the forge lies behind where blue waters fell.
                
                Forge the Hero's Sword pure and true, and the light of good shall see you through.
                """)

            case "q":
                print(f"{player.name}! Thanks for playing")
                break

            case _:
                print("Confused, you stand still, unsure of what to do.")


        print("")
        if check_win(player) or check_dead(player):
            break

def welcome_player():
    print("""
    Welcome adventurer, my name is Brenden. I'm the mayor of the township of Ogden. 
    We need your help! 
    An evil ogre is terrorizing us and we need you to defeat it. 

    You must forge the Hero's Sword to defeat this evil monster. 
    The three pieces of the sword are hidden throughout the nearby countryside.
    You must gather all pieces, take them to the hidden forge, and then make your way to the Dark Fort to battle the ogre.
    This ancient scroll will give you clues to where the pieces of the sword are hidden. 
    """)

    while True:
        answer = input("Do you accept our plea for help? (y/n): ").lower()
        if answer == "y":
            print("\nFantastic!")
            break
        elif answer == "n":
            answer = input("Are you sure? We could really use the help... (y/n): ").lower()
            if answer == "y":
                print("\nFantastic!")
                break
            else:
                print("\nEveryone in the township of Ogden was killed by the Ogre.")
                exit()
        else:
            print("We need an answer adventurer!")

def describe_area(player):
    print("""
    You find yourself at the countryside crossroads...
        1. Dark Woods
        2. Mountain Pass
        3. Cave""")
    if player.is_item_in_inventory("Map"):
        print("        4. Hidden Valley")
    print("""
        Type 'r' to read the Ancient Scroll.
        Type 'i' to view your inventory.
        Type 'q' to quit.
    """)

def get_choice(valid_options):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in valid_options:
                return choice
            else:
                print("Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def explore_the_dark_woods(player):
    while True:
        print("""
        You enter the dark woods... You a dense thicket of trees and a shallow creek bed. 
        1. Search the dense trees
        2. Search the creek bed
        """)
        choice = get_choice([1, 2])
        if choice == 1:
            print(f"{player.name} you spot a broken and rusty blade driven into the trunk of an ancient elm tree.")
            player.add_to_inventory("Broken Blade")
            break
        elif choice == 2:
            print(f"{player.name} you find yourself exploring the creek bed but slip on a rock and roll your ankle.")
            player.take_damage(10)
            break

def explore_the_mountain_pass(player):
    while True:
        print("""
        You enter the mountain pass... You see a steep cliff face and a narrow path leading to a monastary. 
        1. Follow the path to the monastary
        2. Climb the cliff face
        """)
        choice = get_choice([1, 2])
        if choice == 1:
            print(f"{player.name}, the monks welcome recognize your bravery and offer you a golden pommel that once belonged to a great hero.")
            player.add_to_inventory("Golden Pommel")
            break
        elif choice == 2:
            print(f"{player.name} as you climb the cliff face, you lose your footing and fall to the ground below.")
            player.take_damage(10)
            break

def explore_the_dark_cave(player):
    while True:
        print("""
        You enter the dark cave... You see a path that leads right and one that leads left. 
        The right path is pitch black. The left path has a faint glow but reeks of something foul.
        1. Go right
        2. Go left
        """)
        choice = get_choice([1, 2])
        if choice == 1:
            print(f"{player.name}, you fumble around in the darkness and find a hidden compartment in the wall. Inside you find a gem and a map.")
            player.add_to_inventory("Hero's Gem")
            player.add_to_inventory("Map")
            break
        elif choice == 2:
            print(f"{player.name} as you head toward the flowing light, you are ambushed by a giant rat and it bites your ankles")
            player.take_damage(10)
            break
def explore_the_hidden_valley(player):
    while True:
        print("""
        You enter the hidden valley... You see a rolling waterfall and a path deeper into the valley. 
        1. Explore the waterfall
        2. Head deeper into the valley
        """)
        choice = get_choice([1, 2])
        if choice == 1:
            print(f"{player.name}, you find a path that leads to a forge behind the waterfall.There is a blacksmith here who offers to forge the Hero's Sword for you if you have the Broken Blade, Golden Pommel, and Magic Gem.")
            if player.is_item_in_inventory("Broken Blade") and player.is_item_in_inventory("Golden Pommel") and player.is_item_in_inventory("Hero's Gem"):
                print(f"The Blacksmith takes the broken pieces of the Hero's Sword and leaves for a short while.")
                print(f"The Blacksmith returns and gives you the newly forged Hero's Sword! You are now ready to face the evil Ogre!")
                player.add_to_inventory("Hero's Sword")
            break
        elif choice == 2:
            print(f"{player.name} as you head deeper into the valley, you are ambushed by the ogres soldiers. You narrowly escape but not without injury.")
            player.take_damage(10)
            break

def check_win(player):
    if player.is_item_in_inventory("Treasure") and player.is_item_in_inventory("Rare Herbs"):
        print(f"{player.name}, you have won! Congrats")
        return True
    else:
        return False

def check_dead(player):
    if player.health <= 0:
        print(f"{player.name} has died!")
        return True
    else:
        return False

main()




