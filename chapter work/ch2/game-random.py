import random

def playGame():
    x = random.random()
    if (x < 0.5):
        print("Loser! :(")
    else:
        print("You're a winner!")
    
playGame() # call the function