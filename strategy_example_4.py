class Strategies:
    @staticmethod
    def comp_strategy(computer_hand, round, auction_card):
        points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 10}

        if not computer_hand:  # Check if computer_hand is empty
            return None  # Return None if computer_hand is empty

        if auction_card.split('_')[0] in ['10', 'jack', 'queen', 'king', 'ace']:
            for card in computer_hand:
                if card.split('_')[0] == auction_card.split('_')[0]:
                    return card

        elif auction_card.split('_')[0] in ['2', '3', '4', '5', '6', '7', '8', '9']:
            for card in computer_hand:
                if points[card.split('_')[0]] == points[auction_card.split('_')[0]] + 1:
                    return card

        return max(computer_hand, key=lambda card: points[card.split('_')[0]])

