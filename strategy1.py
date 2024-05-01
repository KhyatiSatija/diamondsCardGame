# strategy.py

import random

def computer_bid(user, computer, diamond_card):
    """
    Determine the computer's bidding strategy based on the game state.
    
    Args:
        user (Player): The user player object.
        computer (Player): The computer player object.
        diamond_card (Card): The selected diamond card for the current round.
    
    Returns:
        int: Index of the selected card in the computer's hand.
    """
    # Determine if the player has played high-value cards
    player_has_high_value_cards = any(card.rank > 10 for card in user.high_value_cards_played)
    
    # Determine if the selected diamond card is high-value (> 10)
    diamond_card_is_high_value = diamond_card.rank > 10
    
    # Adjust computer's bidding strategy based on player's high-value cards and diamond card's value
    if player_has_high_value_cards and diamond_card_is_high_value:
        # If the player has played high-value cards and the selected diamond card is high-value,
        # the computer bids a high-value card higher than the expected bid by the player
        expected_player_bid = max(card.rank for card in user.high_value_cards_played)  # Expected bid by the player
        computer_bid_index = max((i for i, card in enumerate(computer.hand) if card.rank > expected_player_bid), default=-1)
        # If there's no higher-value card in the computer's hand, bid the highest-value card available
        if computer_bid_index == -1:
            computer_bid_index = random.randint(0, len(computer.hand) - 1)
    else:
        # If the player has not played high-value cards or the selected diamond card is low-value,
        # the computer bids a reasonable card
        reasonable_cards = [card for card in computer.hand if card.rank <= 8]  # Reasonable cards have rank <= 8
        if reasonable_cards:
            computer_bid_index = computer.hand.index(random.choice(reasonable_cards))
        else:
            # If there are no reasonable cards available, bid randomly
            computer_bid_index = random.randint(0, len(computer.hand) - 1)

    return computer_bid_index
