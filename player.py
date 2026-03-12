class Person:
    def __init__(self):
        print("Welcome to the Monster Game!")
        self.name = str(input("Enter your name: "))
        self.player_storage = {"weapon": 1,"health":100,"key":0}
        self.turn_count = 1
        
    def display_storage(self):
        print("\n")
        print("your storage")
        for key, value in self.player_storage.items():
            print(f"{key}: {value}")
        print("\n")
        
