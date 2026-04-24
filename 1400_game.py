
from Player import Player

def main():
    welcome_player()
    player = Player()
    player.ask_player_name()

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
                In a forest dark and deep the blade resides in elms tight keep.
                On a mountain high and steep the pommel is hidden where wise ones sleep.
                In a cave where darkness dwells the gem is guarded by a beast that smells.
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

def explore_the_dark_woods(player):
    print(f"{player.name}! , you step into the dark woods....")
    player.add_to_inventory("Lantern")

def explore_the_mountain_pass(player):
    print(f"{player.name}! You step into the mountain pass....")
    player.add_to_inventory("Map")

def explore_the_dark_cave(player):
    if player.is_item_in_inventory("Lantern"):
        print(f"{player.name}, you enter the cave")
        player.add_to_inventory("Treasure")
    else:
        print(f"{player.name}! It looks really dark in there. You're to scared to enter.")
        player.take_damage(10)

def explore_the_hidden_valley(player):
    if player.is_item_in_inventory("Map"):
        print(f"{player.name}! You enter the hidden valley")
        player.add_to_inventory("Rare Herbs")
    else:
        print(f"{player.name}, you are unable to locate the hidden valley.")
        player.take_damage(10)

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




