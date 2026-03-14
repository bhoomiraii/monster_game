from player import Person

from dice import selector

from task import task
from monster import monster_encounter
from check import check

from result import win_or_loss




game_on = True
#---------------------------Player customization
person=Person()
player_storage=person.player_storage
turn_count=person.turn_count
#[monster,check,task]
events = [0, 1, 2]
#important for the random selector for gifts
weights = [30, 40, 30]

while game_on:
    #---------------A blinking mesg for what u have
    person.display_storage()
    
    dice_roll = selector(events, weights)

#---------------------------------------------------maintask -------------------          
#-----------dice roll for sudden situations -(event)classssssssssssssssssssssssssssss
    if 0 == dice_roll:
#-----------monster appears
                player_storage, turn_count = monster_encounter(player_storage, turn_count)
                
    elif dice_roll == 1:
                player_storage, turn_count = check(player_storage, turn_count)
                        
    else:
                player_storage = task(player_storage)
#---------------improve_task-
#---------------------------------------------------maintask -----------------------------------

#-------no helth -- chance reduced -- health reset
    if player_storage["health"] <= 0 and turn_count > 0:
            print(f"chance left: {turn_count-1}")
            turn_count-=1
            player_storage["health"] = 100
#___its for the stopping of the game when you win(keys got) or lose(count turns)
    game_on = win_or_loss(player_storage, turn_count)
    



