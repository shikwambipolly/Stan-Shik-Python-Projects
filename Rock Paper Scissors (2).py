import random
list1 = ['rock', 'paper', 'scissors']
players_hand = input("Rock paper or scissors?: ")
computers_hand = random.choice(list1)

while computers_hand == 'rock':
    if players_hand == "rock":
        print("It's a tie! I had rock too.")
    elif players_hand == "paper":
        print("You won! I had rock")
    elif players_hand == "scissors":
        print("You lost! I had rock")
    break

while computers_hand == 'paper':
    if players_hand == "rock":
        print("You lost! I had paper.")
    elif players_hand == "paper":
        print("It's a tie! I had paper too.")
    elif players_hand == "scissors":
        print("You won! I had paper")
    break

while computers_hand == 'scissors':
    if players_hand == 'rock':
        print("You won! I had scissors.")
    elif players_hand == "paper":
        print("You lost! I had scissors.")
    elif players_hand == "scissors":
        print("It's a tie! I had scissors too.")
    break

    input("Press enter to exit")