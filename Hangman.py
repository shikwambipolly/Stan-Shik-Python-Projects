secret_word = "Unlucky"
guessing_count = 0
guess = ""
guess_limit = input("How many guesses do you want?: ")
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guessing_count < int(guess_limit):
       guess = input("Enter your guess: ")
       guessing_count += 1
       print("That's not it! Try again!")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lost!")
else:
    print("You win!")
input("Press enter to exit")
