import random

while True:
    choices = ("rock","paper","scissors")

    CPU = random.choice(choices)
    player = None
  

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()
    
        
    if player == CPU:
        print("CPU: ", CPU)
        print("player: ", player)
        print("Tie !, Try Again")

    elif player == "rock":
        if  CPU == "paper":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You Lose, Game over !")
        if CPU == "scissors":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You Win !")

    elif player == "scissors":
        if CPU == "rock":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You Lose, Game over !")
        if CPU == "paper":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You Win !")
            
    elif player == "paper":
        if CPU == "scissors":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You Lose, Game over !")
        if CPU == "rock":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You Win !")

    play_again = input("play again? (yes/no):").lower()

    if play_again != "yes":
        break

print("Bye !")