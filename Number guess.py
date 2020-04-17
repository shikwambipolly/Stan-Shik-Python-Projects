import random

list_of_numbers = [1, 2, 3, 4, 5]

while 0 == 0:
    guess = input("Enter your number guess: ")
    actual_number = random.choice(list_of_numbers)
    if int(actual_number) == int(guess):
        print("You guessed " + str(guess) + ". The actual number is " + str(actual_number) + ". You guessed right!")
    else:
        print("You guessed " + str(guess) + ". The actual number is " + str(actual_number) + ". You guessed wrong!")
