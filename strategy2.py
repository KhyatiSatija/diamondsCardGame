# strategy.py

import random

def calculate_card_probability(cards_in_play):
    """
    Calculate the probability of each card being in play based on the cards already played.
    
    Args:
        cards_in_play (list): List of cards already played in the game.
    
    Returns:
        dict: Dictionary containing the probability of each card being in play.
    """
    total_cards = 52  # Total number of cards in a standard deck
    card_count = {rank: 0 for rank in range(2, 15)}  # Initialize count for each rank (2 to Ace)
    
    # Count the number of occurrences of each card rank in the cards already played
    for card in cards_in_play:
        card_count[card.rank] += 1
    
    # Calculate the probability of each card rank being in play
    card_probability = {rank: count / total_cards for rank, count in card_count.items()}
    
    return card_probability

def computer_bid(user, computer, diamond_card, cards_in_play):
    """
    Determine the computer's bidding strategy based on the game state and card distribution probability.
    
    Args:
        user (Player): The user player object.
        computer (Player): The computer player object.
        diamond_card (Card): The selected diamond card for the current round.
        cards_in_play (list): List of cards already played in the game.
    
    Returns:
        int: Index of the selected card in the computer's hand.
    """
    # Calculate the probability of each card being in play
    card_probability = calculate_card_probability(cards_in_play)
    
    # Determine the probability threshold for considering a card as high-value
    high_value_threshold = 0.1  # Example threshold (adjust as needed)
    
    # Determine if the player has played high-value cards
    player_has_high_value_cards = any(card.rank > 10 for card in user.high_value_cards_played)
    
    # Adjust computer's bidding strategy based on player's high-value cards and card distribution probability
    if player_has_high_value_cards:
        # If the player has played high-value cards, adjust strategy to bid more conservatively
        # Consider cards with probabilities below the high-value threshold as reasonable bids
        reasonable_cards = [card for card in computer.hand if card_probability.get(card.rank, 0) < high_value_threshold]
        if reasonable_cards:
            computer_bid_index = computer.hand.index(random.choice(reasonable_cards))
        else:
            # If there are no reasonable cards available, bid randomly
            computer_bid_index = random.randint(0, len(computer.hand) - 1)
    else:
        # If the player has not played high-value cards, bid more aggressively
        # The computer may bid higher-value cards if the selected diamond card is high-value
        if diamond_card.rank > 10:
            # Bid the highest-value card available
            computer_bid_index = computer.hand.index(max(computer.hand, key=lambda card: card.rank))
        else:
            # Bid randomly
            computer_bid_index = random.randint(0, len(computer.hand) - 1)

    return computer_bid_index
