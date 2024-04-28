def computer_bid(user, computer, diamond_card):
    if diamond_card.rank <= 5:
        bid_rank = diamond_card.rank
    elif diamond_card.rank < 10:
        bid_rank = diamond_card.rank + 1
    else:
        bid_rank = max(card.rank for card in computer.hand)
    
    bid =  [card for card in computer.hand if card.rank == bid_rank][0]
    computer.hand.remove(bid)
    return bid