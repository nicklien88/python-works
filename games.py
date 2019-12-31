import random

money = 100

# Write your game of chance functions here
print("Welcome to the Game of Chance.")


def flipping_coin(guess, bet):
    print("flipping the coin, guess side. Heads or Tails.")
    print("You guess {} and bet {} dollars.".format(guess, bet))
    actual_side = random.randint(1, 2)
    # bet means how much the player is betting on the coin flip.
    if guess == "Heads":
        guess_side = 1
    elif guess == "Tails":
        guess_side = 2
    else:
        print("You enter a wrong value")
        return 0
    if bet < 0 or bet > money:
        print("Bet can not be negative or more than the money you have.")
        return 0
    else:
        if guess_side == actual_side:
            print("You win {} dollars.".format(bet))
            return bet
        else:
            print("You lose {} dollars.".format(bet))
            return -bet


def play_cho_han(guess, bet):
    print("Rolling the dice, guess if the sum of the points of dice is odd or even.")

    print("You guess: {} and bet {} dollars.".format(guess, bet))
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    if guess == "Odd":
        guess_code = 1
    elif guess == "Even":
        guess_code = 0
    else:
        print("You enter a wrong value")
        return 0

    if bet < 0 or bet > money:
        print("Bet can not be negative or more than the money you have.")
        return 0
    else:
        if (num1 + num2) % 2 == guess_code:
            print("You win {} dollars.".format(bet))
            return bet
        else:
            print("You lose {} dollars.".format(bet))
            return -bet


def pick_card(bet):  # player means the one you guess that have higher number.
    print("Picking a card, the one who got the higher number of the card wins.")
    print("You bet {} dollars".format(bet))
    if bet < 0 or bet > money:
        print("Bet can not be negative or more than the money you have.")
        return 0
    else:
        # store all the cards to the list
        card_deck = []
        for i in range(4):
            numbers = [a for a in range(1, 14)]
            card_deck += numbers
        # randomly picking a card
        myself_number = random.choice(card_deck)
        card_deck.remove(myself_number)
        opponent_number = random.choice(card_deck)
        print("You got {}, opponent got {}".format(myself_number, opponent_number))
        # distinguish who wins the game
        if myself_number > opponent_number:
            print("You win {} dollars.".format(bet))
            return bet
        elif myself_number < opponent_number:
            print("You lose {} dollars.".format(bet))
            return -bet
        elif myself_number == opponent_number:
            print("A tie")
            return 0


def roulette(guess, bet):
    print("Spaning the roulette, guess if ball is in \"Odd\" spot, \"Even\" spot or Special Number spot.")
    print("You guess \"{}\" spot and bet {} dollars.".format(guess, bet))
    special_numbers = ["0", "00"]
    numbers = [str(i) for i in range(1, 37)]
    # make all elements are string in order to use isdigit() function
    numbers += special_numbers
    ball_spot = random.choice(numbers)
    print("Ball spot is {}".format(ball_spot))

    if guess == "Odd" or guess == "Even" or guess == "0" or guess == "00":
        if bet < 0 or bet > money:
            print("Bet can not be negative or more than the money you have.")
            return 0
        else:
            if guess == "Odd":
                if ball_spot.isdigit():
                    if int(ball_spot) % 2 == 1:
                        print("You win {} dollars.".format(bet))
                        return bet
                    else:
                        print("You lose {} dollars.".format(bet))
                        return -bet
                else:
                    print("You win {} dollars.".format(bet))
                    return -bet
            elif guess == "Even":
                if ball_spot.isdigit():
                    if int(ball_spot) % 2 == 0:
                        print("You win {} dollars.".format(bet))
                        return bet
                    else:
                        print("You lose {} dollars.".format(bet))
                        return -bet
                else:
                    print("You lose {} dollars.".format(bet))
                    return -bet
            elif guess == "0":
                if ball_spot == "0":
                    print("You guessed a Special Number, You win {} dollars.".format(bet * 35))
                    return bet * 35
                else:
                    print("You lose {} dollars.".format(bet))
                    return -bet
            elif guess == "00":
                if ball_spot == "00":
                    print("You guessed a Special Number, You win {} dollars.".format(bet * 35))
                    return bet * 35
                else:
                    print("You lose {} dollars.".format(bet))
                    return -bet
    else:
        print("You enter a wrong value.")
        return 0
# Call your game of chance functions here


money += flipping_coin("Heads", 10)
money += play_cho_han("Even", 30)
money += pick_card(20)
money += roulette("Odd", 10)
print("You have {} dollars left.".format(money))
