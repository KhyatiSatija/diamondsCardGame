def get_remaining_diamonds(revealed_diamonds):
  """
  This function calculates the remaining diamond cards based on revealed diamonds.

  Args:
      revealed_diamonds: List of revealed diamond values (integers).

  Returns:
      List: Remaining diamond cards (2-14).
  """
  all_diamonds = list(range(2, 15))  # List of all diamond values
  remaining_diamonds = [diamond for diamond in all_diamonds if diamond not in revealed_diamonds]
  return remaining_diamonds

def calculate_diamond_probability(revealed_diamonds):
  """
  This function calculates the probability of each diamond value being revealed.

  Args:
      revealed_diamonds: List of revealed diamond values (integers).

  Returns:
      Dictionary: Probabilities for each diamond value (2-14).
  """
  remaining_cards = get_remaining_diamonds(revealed_diamonds)  # Call separate function
  total_diamonds = 13  # Assuming 13 diamonds in the deck initially
  diamond_probs_of_remaining_cards = { value : remaining_cards.count(value) / (total_diamonds - len(revealed_diamonds))\
                                      for value in range(2, 15) if value in remaining_cards }
  return diamond_probs_of_remaining_cards

from functools import reduce

def probability_of_winning(individual_player_cards, card_to_win):
  """
  This function calculates the probability of a card winning the trick.

  Args:
      individual_player_cards: Dictionary where keys are players and values are lists of their remaining cards (excluding diamonds).
      card_to_win: Integer value of the card that needs to win.

  Returns:
      Float: Probability of the card winning the trick.
  """

  all_cards = reduce ( lambda x,y : x + y, [ player_cards for player_cards in individual_player_cards ] )

  favorable_cards = sum([card_value < card_to_win for card_value in all_cards])

  # Total possible combinations (product of remaining cards for each player)
  total_combinations = reduce( lambda x, y : x * y, [ len(player_cards) for player_cards in individual_player_cards ] )

  return favorable_cards / total_combinations

def calculate_expected_points(hand, revealed_diamonds, other_player_cards):
  """
  This function calculates the expected points for bidding each card in your hand.

  Args:
      hand: List of card values (integers) in your hand.
      _: Placeholder argument for revealed_diamonds (not used).

  Returns:
      Dictionary: Expected points for bidding each card in your hand.
  """

  def get_expected_points_for_card ( card_in_hand, remaining_diamonds_prob ):

    expected_points_with_diamond_prob = sum( card * prob for card, prob in remaining_diamonds_prob.items()) / len ( remaining_diamonds_prob )
    expected_points_with_winning_prob = expected_points_with_diamond_prob * probability_of_winning ( other_player_cards, card_in_hand )

    return expected_points_with_winning_prob

  remaining_diamonds_prob = calculate_diamond_probability ( revealed_diamonds )

  expected_points = { card_in_hand : get_expected_points_for_card ( card_in_hand, remaining_diamonds_prob ) for card_in_hand in hand}

  return expected_points

def probabilistic_bidding(hand, revealed_diamonds, other_players_cards):
  """
  This function chooses the card to bid based on expected points.

  Args:
      hand: List of card values (integers) in your hand.
      revealed_diamonds: List of revealed diamond values (integers).

  Returns:
      Integer: The card value to bid (from your hand).
  """
  expected_points = calculate_expected_points(hand, revealed_diamonds, other_players_cards)
  best_card = max(expected_points, key=expected_points.get)
  return best_card

# Example usage (assuming revealed diamonds are tracked):
revealed_diamonds = [9, 7]  # Example: Two diamonds (9 and 7) revealed
my_hand = [5, 10, 12]  # Example hand
other_players_cards = [[1,2,3],[4,5]]

best_bid = probabilistic_bidding(my_hand, revealed_diamonds, other_players_cards)
print(f"Recommended bid (knowing all revealed diamonds): {best_bid}")

