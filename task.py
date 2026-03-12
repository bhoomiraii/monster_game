from gift import random_gift

def task(player_storage):
    print("write 'darling' to win task")
    task_input = input("Here baby!: ")
    if task_input == "darling":
        print("Congratulations! You win the task!")
        print("gift time!")
        return random_gift(player_storage)
    else:
        print("Sorry, that's not correct.... bye!")
        return player_storage
        
    