import random

print("Welcome To My BlackJack Game House")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# For Handling Ace Value Either 1 or 11
def calculate_score(hand):
    score = sum(hand)
    num_aces = hand.count(11)
    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1
    return score


# If user got Bust initially But Dealer Score is less than 17
def dealer_turn(dealer_cards, cards):
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))
    return dealer_cards


def calculate_winner(user_score, dealer_score, user_cards, dealer_cards):
    if user_score > 21:
        return "You bust! Dealer wins."
    elif dealer_score > 21:
        return "Dealer busts! You win!"
    elif user_score == dealer_score:
        return "It's a tie!"
    elif (
        user_score == 21
        and len(user_cards) == 2
        and not (dealer_score == 21 and len(dealer_cards) == 2)
    ):
        return "Blackjack! You win!"
    elif dealer_score == 21 and len(dealer_cards) == 2:
        return "Dealer has Blackjack! You lose."
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "Dealer wins!"


# For getting valid Input
def get_valid_input(prompt, valid_options):
    while True:
        response = input(prompt).lower()
        if response in valid_options:
            return response
        print(f"Invalid input. Please type one of: {', '.join(valid_options)}")


# For Restarting The Game Again
while True:
    game_start = get_valid_input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ", ["y", "n"]
    )
    if game_start != "y":
        print("Goodbye")
        break

    print(logo)

    # Deal initial cards
    user_cards = random.sample(cards, 2)
    user_cards_value = []
    user_cards_value.extend(user_cards)
    dealers_card = random.sample(cards, 2)
    dealer_cards_value = []
    dealer_cards_value.extend(dealers_card)

    # Show initial hands
    print(
        f"Your Cards: {user_cards_value}, current score: {calculate_score(user_cards_value)}"
    )
    print(f"Computer's first card: {dealers_card[0]}")

    # Check for immediate Blackjack
    if calculate_score(user_cards_value) == 21:
        print("Blackjack! Let's check the dealer's hand...")
    else:
        # User's turn
        while calculate_score(user_cards_value) <= 21:
            new_card = get_valid_input(
                "Type 'y' to get another card, 'n' to pass: ", ["y", "n"]
            )
            if new_card == "y":
                new_card_value = random.choice(cards)
                user_cards_value.append(new_card_value)
                print(
                    f"Your Cards: {user_cards_value}, current score: {calculate_score(user_cards_value)}"
                )
            else:
                break

    # Dealer's turn
    dealer_cards_value = dealer_turn(dealer_cards_value, cards)
    print(
        f"Dealer's Cards: {dealer_cards_value}, dealer's score: {calculate_score(dealer_cards_value)}"
    )

    # Determine winner
    user_score = calculate_score(user_cards_value)
    dealer_score = calculate_score(dealer_cards_value)
    print(
        calculate_winner(user_score, dealer_score, user_cards_value, dealer_cards_value)
    )
