import random
possible_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Please note that the dealer stands at 16.")

while True:
    players_hand = ""
    dealers_hand = ""
    while players_hand == "" and dealers_hand == "":
        players_hand = random.choice(possible_cards) + random.choice(possible_cards)
        dealers_hand = random.choice(possible_cards)
        print("Your hand is " + str(players_hand))
        print("Dealers first card is " + str(dealers_hand))

    while players_hand > 0 and dealers_hand > 0:
        action = input("Hit or Stand?: ")
        dealers_second_face = random.choice(possible_cards)
        dealers_hand = dealers_hand + dealers_second_face
        if action == "hit":
            drew1 = random.choice(possible_cards)
            players_hand = players_hand + drew1
            print("Your drew a " + str(drew1))
            if players_hand == 21:
                print("Your hand is 21. You have blackjack!")
                break
            elif players_hand > 21:
                print("Your hand is " + str(players_hand) + " . Unlucky!. You busted!")
                break
            elif players_hand < 21:
                print("Your hand is " + str(players_hand))
                second_action = input("Hit or Stand?: ")
                if second_action == "stand":
                    print("Dealer's second card is " + str(dealers_second_face))
                    print("Dealer's hand is " + str(dealers_hand))
                    while dealers_hand < 16:
                        drewd2 = random.choice(possible_cards)
                        dealers_hand = dealers_hand + drewd2
                        print("The dealer drew a " + str(drewd2))
                        print("The dealer's hand is now " + str(dealers_hand))
                    if dealers_hand > 21:
                        print("Dealer's hand is " + str(dealers_hand) + ". The dealer busted. You win!")
                        break
                    if dealers_hand > players_hand:
                        print("The dealer has " + str(dealers_hand) + ". You have " + str(
                            players_hand) + ". Unlucky. You lose.")
                    elif players_hand > dealers_hand:
                        print("The dealer has " + str(dealers_hand) + ". You have " + str(players_hand) + ". You win.")
                        break
                    elif dealers_hand == 21 and players_hand == 21:
                        print("Both got Blackjack. Push.")
                        break
                    elif dealers_hand == 21 and players_hand < 21:
                        print("Dealer got Blackjack. You lose.")
                        break
                elif second_action == "hit":
                    drew2 = random.choice(possible_cards)
                    players_hand = players_hand + drew2
                    print("Your drew a " + str(drew2))
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
                            print("Dealer's second card is " + str(dealers_second_face))
                            print("Dealer's hand is " + str(dealers_hand))
                            while dealers_hand < 16:
                                drewd3 = random.choice(possible_cards)
                                dealers_hand = dealers_hand + drewd3
                                print("The dealer drew a " + str(drewd3))
                                print("The dealer's hand is now " + str(dealers_hand))
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
                            elif dealers_hand == 21 and players_hand == 21:
                                print("Both got Blackjack. Push.")
                                break
                            elif dealers_hand == 21 and players_hand < 21:
                                print("Dealer got Blackjack. You lose.")
                                break
                        if third_action == "hit":
                            drew3 = random.choice(possible_cards)
                            players_hand = players_hand + drew3
                            print("Your drew a " + str(drew3))
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
            print("Dealer's second card is " + str(dealers_second_face))
            print("Dealer's hand is " + str(dealers_hand))
            while dealers_hand < 16:
                drewd1 = random.choice(possible_cards)
                dealers_hand = dealers_hand + drewd1
                print("The dealer drew a " + str(drewd1))
                print("The dealer's hand is now " + str(dealers_hand))
            if dealers_hand > 21:
                print("Dealer's hand is " + str(dealers_hand) + ". The dealer busted. You win!")
                break
            if dealers_hand > players_hand and dealers_hand < 21:
                print(
                    "The dealer has " + str(dealers_hand) + ". You have " + str(players_hand) + ". Unlucky. You lose.")
                break
            elif players_hand > dealers_hand:
                print("The dealer has " + str(dealers_hand) + ". You have " + str(players_hand) + ". You win.")
                break
            elif dealers_hand == 21 and players_hand == 21:
                print("Both got Blackjack. Push.")
                break
            elif dealers_hand == 21 and players_hand < 21:
                print("Dealer got Blackjack. You lose.")
                break
