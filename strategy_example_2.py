import random
# Function for computer bidding logic (replace with your desired strategy)
def computer_bid(player_cards, diamond_value):
  """Simulates the computer's bidding logic.

  This function implements a simple bidding strategy where the computer 
  chooses the highest card it has that is at least half the value of the 
  auctioned diamond. If there are no such cards, it returns the lowest card 
  in its hand (or None if the hand is empty).

  Args:
      player_cards: A list of cards in the computer's hand.
      diamond_value: The value of the diamond being auctioned.

  Returns:
      The card chosen by the computer for its bid, or None if the computer 
      has no cards left.
  """
  eligible_cards = [card for card in player_cards if card_values[card] >= diamond_value // 2]
  if eligible_cards:
    return random.choice(eligible_cards)
  # Otherwise, check if the hand is empty before finding the minimum
  else:
    if player_cards:  # Check if there are any cards left
      return min(player_cards, key=card_values.get)
    else:
      return None  # Player has no cards left