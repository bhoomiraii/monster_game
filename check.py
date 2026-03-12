from dice import selector
from gift import random_gift
from monster import monster_encounter

def check(player_storage, turn_count):
                print("check What's in front of you")
                answer=input("Press o to check...")
                print("monster might appear")
                if answer == "o":
                    player_storage=random_gift(player_storage)
#-------------------working on the random selector for gifts
                dice_roll = selector()
                if 0 == dice_roll:
                        player_storage, turn_count = monster_encounter(player_storage, turn_count)
                return player_storage, turn_count
#----------------monster appears
                        
