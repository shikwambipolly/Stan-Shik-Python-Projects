import random

players_hand = ""
dealers_hand = ""
possible_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]

print("Please note that the dealer stands at 16")

while players_hand == "" and dealers_hand == "":
    players_hand = random.choice(possible_cards) + random.choice(possible_cards)
    dealers_hand = random.choice(possible_cards)
    print("Your hand is " + str(players_hand))
    print("Dealers first card is " + str(dealers_hand))

while players_hand > 0 and dealers_hand > 0:
    action = input("Hit or Stand?: ")
    dealers_hand += random.choice(possible_cards)
    if action == "hit":
        players_hand += random.choice(possible_cards)
        if players_hand == 21:
           print("Your hand is 21. You've got blackjack!")
           break
        elif players_hand > 21:
           print("Your hand is " + str(players_hand) +" . Unlucky!. You busted!")
           break
        elif players_hand < 21:
           print("Your hand is " + str(players_hand))
           second_action = input("Hit or Stand?: ")
           if second_action == "stand":
               while dealers_hand < 16:
                   dealers_hand += random.choice(possible_cards)
                   if dealers_hand > 21:
                       print("Dealer's hand is " + str(dealers_hand) + ". The dealer busted. You win!")
                   break
               if dealers_hand > players_hand:
                   print("The dealer has " + str(dealers_hand) + ". You have " + str(players_hand) + ". Unlucky. You lose.")
               elif players_hand > dealers_hand and dealers_hand > 16:
                   print("The dealer has " + str(dealers_hand) + ". You have " + str(players_hand) + ". You win.")
               break
           elif second_action == "hit":
                players_hand += random.choice(possible_cards)
                if players_hand == 21:
                    print("Your hand is 21. You've got blackjack!")
                    break
                elif players_hand > 21:
                    print("Your hand is " + str(players_hand) + " . Unlucky!. You busted!")
                    break
                elif players_hand < 21:
                    print("Your hand is " + str(players_hand))
                    third_action = input("Hit or Stand?: ")
                    if third_action == "stand":
                        while dealers_hand < 16:
                            dealers_hand += random.choice(possible_cards)
                            if dealers_hand > 21:
                                print("Dealer's hand is" + str(dealers_hand) + ". The dealer busted. You win!")
                            break
                        if dealers_hand > players_hand:
                            print("The dealer has " + str(dealers_hand) + ". You have " + str(
                                players_hand) + ". Unlucky. You lose.")
                            break
                        elif players_hand > dealers_hand and dealers_hand > 16:
                            print("The dealer has " + str(dealers_hand) + ". You have " + str(
                                players_hand) + ". You win.")
                            break
                    if third_action == "hit":
                        players_hand += random.choice(possible_cards)
                        if players_hand == 21:
                            print("Your hand is 21. You've got blackjack!")
                            break
                        elif players_hand > 21:
                            print("Your hand is " + str(players_hand) + " . Unlucky!. You busted!")
                            break
                        elif players_hand < 21:
                            print("You have " + str(players_hand))
                            if dealers_hand > players_hand and dealers_hand > 16:
                                print("The dealer has " + str(dealers_hand) + ". You have " + str(
                                    players_hand) + ". Unlucky. You lose.")
                                break
                            elif players_hand > dealers_hand:
                                print("The dealer has " + str(dealers_hand) + ". You have " + str(
                                    players_hand) + ". You win.")
                                break
    if action == "stand":
        while dealers_hand < 16:
           dealers_hand += random.choice(possible_cards)
        if dealers_hand > 21:
           print("Dealer's hand is " + str(dealers_hand) + ". The dealer busted. You win!")
           break
        if dealers_hand > players_hand and dealers_hand < 21:
            print("The dealer has " + str(dealers_hand) + ". You have " + str(players_hand) + ". Unlucky. You lose.")
            break
        elif players_hand > dealers_hand:
            print("The dealer has " + str(dealers_hand) + ". You have " + str(players_hand) + ". You win.")
            break

input("Press enter to exit......")