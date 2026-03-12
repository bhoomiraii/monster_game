
def monster_encounter(player_storage, turn_count):
    print("Monster appears! Prepare for battle!")
    if player_storage["weapon"] > 0 and player_storage["health"] > 0:
#----------------check if player has weapon and health to fight
        print("You have a weapon and health to fight the monster!")
        fight=input("Press f to fight...")
#-------------------coundition for fight or not
        if fight == "f":
            print("You fought the monster and won!")
            player_storage["weapon"] -= 1
            player_storage["health"] -= 20
        else:
            print("You chose not to fight. The monster attacks you!")
            player_storage["health"] -= 30
            turn_count-=1
            
    else:
        print("You don't have a weapon or enough health to fight the monster!")
        print("The monster attacks you!")
        player_storage["health"] -= 30
        turn_count-=1
#----------------------------------------lacking weapon or health to fight the monster
    return player_storage, turn_count
