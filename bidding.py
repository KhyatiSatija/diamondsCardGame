import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the Pygame window
screen_width = 1400
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Game of Diamonds")

# Define font
font = pygame.font.SysFont(None, 30)

card_image_paths = {
    '2 of Diamonds': 'PNG-cards-1.3/2_of_diamonds.png',
    '3 of Diamonds': 'PNG-cards-1.3/3_of_diamonds.png',
    '4 of Diamonds': 'PNG-cards-1.3/4_of_diamonds.png',
    '5 of Diamonds': 'PNG-cards-1.3/5_of_diamonds.png',
    '6 of Diamonds': 'PNG-cards-1.3/6_of_diamonds.png',
    '7 of Diamonds': 'PNG-cards-1.3/7_of_diamonds.png',
    '8 of Diamonds': 'PNG-cards-1.3/8_of_diamonds.png',
    '9 of Diamonds': 'PNG-cards-1.3/9_of_diamonds.png',
    '10 of Diamonds': 'PNG-cards-1.3/10_of_diamonds.png',
    '11 of Diamonds': 'PNG-cards-1.3/jack_of_diamonds.png',
    '12 of Diamonds': 'PNG-cards-1.3/queen_of_diamonds.png',
    '13 of Diamonds': 'PNG-cards-1.3/king_of_diamonds.png',
    '14 of Diamonds': 'PNG-cards-1.3/ace_of_diamonds.png',
    '2 of Spades': 'PNG-cards-1.3/2_of_spades.png',
    '3 of Spades': 'PNG-cards-1.3/3_of_spades.png',
    '4 of Spades': 'PNG-cards-1.3/4_of_spades.png',
    '5 of Spades': 'PNG-cards-1.3/5_of_spades.png',
    '6 of Spades': 'PNG-cards-1.3/6_of_spades.png',
    '7 of Spades': 'PNG-cards-1.3/7_of_spades.png',
    '8 of Spades': 'PNG-cards-1.3/8_of_spades.png',
    '9 of Spades': 'PNG-cards-1.3/9_of_spades.png',
    '10 of Spades': 'PNG-cards-1.3/10_of_spades.png',
    '11 of Spades': 'PNG-cards-1.3/jack_of_spades.png',
    '12 of Spades': 'PNG-cards-1.3/queen_of_spades.png',
    '13 of Spades': 'PNG-cards-1.3/king_of_spades.png',
    '14 of Spades': 'PNG-cards-1.3/ace_of_spades.png',
    '2 of Clubs': 'PNG-cards-1.3/2_of_clubs.png',
    '3 of Clubs': 'PNG-cards-1.3/3_of_clubs.png',
    '4 of Clubs': 'PNG-cards-1.3/4_of_clubs.png',
    '5 of Clubs': 'PNG-cards-1.3/5_of_clubs.png',
    '6 of Clubs': 'PNG-cards-1.3/6_of_clubs.png',
    '7 of Clubs': 'PNG-cards-1.3/7_of_clubs.png',
    '8 of Clubs': 'PNG-cards-1.3/8_of_clubs.png',
    '9 of Clubs': 'PNG-cards-1.3/9_of_clubs.png',
    '10 of Clubs': 'PNG-cards-1.3/10_of_clubs.png',
    '11 of Clubs': 'PNG-cards-1.3/jack_of_clubs.png',
    '12 of Clubs': 'PNG-cards-1.3/queen_of_clubs.png',
    '13 of Clubs': 'PNG-cards-1.3/king_of_clubs.png',
    '14 of Clubs': 'PNG-cards-1.3/ace_of_clubs.png',
}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

user = Player("Player")
computer = Player("Computer")

def initialize_deck(suit):
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    return [Card(rank, suit) for rank in ranks]

user.hand = initialize_deck('Diamonds')
computer.hand = initialize_deck('Spades') + initialize_deck('Clubs')

diamond_ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
diamond_cards = [Card(rank, 'Diamonds') for rank in diamond_ranks]

def display_diamond_cards(diamond_cards):
    random_diamond_card = Card(random.randint(2, 14), 'Diamonds')
    card_image = pygame.image.load(card_image_paths[f"{random_diamond_card.rank} of {random_diamond_card.suit}"])
    card_rect = card_image.get_rect()
    card_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(card_image, card_rect)
    pygame.display.flip()

def bid_phase(screen, user, computer, diamond_card):
    screen.fill((0, 0, 0))
    user_bid_text = font.render("Your turn to bid:", True, (255, 255, 255))
    screen.blit(user_bid_text, (screen_width // 2, (screen_height // 2) - 5))
    pygame.display.flip()

    user_bid_index = get_user_bid(user)

    user_bid = user.hand.pop(user_bid_index)
    user_bid_value = card_value(user_bid.rank)

    user_bid_display = font.render(f"You bid with: {user_bid.rank}", True, (255, 255, 255))
    screen.blit(user_bid_display, (20, 100))
    pygame.display.flip()

    computer_bid_text = font.render("Computer's turn to bid:", True, (255, 255, 255))
    screen.blit(computer_bid_text, (20, 130))
    pygame.display.flip()

    computer_bid_index = random.randint(0, len(computer.hand) - 1)
    computer_bid = computer.hand.pop(computer_bid_index)
    computer_bid_value = card_value(computer_bid.rank)

    computer_bid_display = font.render(f"Computer bids with: {computer_bid.rank}", True, (255, 255, 255))
    screen.blit(computer_bid_display, (20, 160))
    pygame.display.flip()

    return user_bid_value, computer_bid_value

def card_value(rank):
    if rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
        return int(rank)
    elif rank == '11':
        return 10
    elif rank == '12':
        return 11
    elif rank == '13':
        return 12
    elif rank == '14':
        return 14
    else:
        return 0

def resolve_bids(user_bid, computer_bid, diamond_card):
    if user_bid > computer_bid:
        user.score += card_value(diamond_card.rank)
    elif user_bid < computer_bid:
        computer.score += card_value(diamond_card.rank)
    else:
        user.score += card_value(diamond_card.rank) // 2
        computer.score += card_value(diamond_card.rank) // 2

def display_points(screen, user, computer):
    points_distributed_text = font.render("Points Distributed", True, (255, 255, 255))
    user_score_text = font.render(f"Your Score: {user.score}", True, (255, 255, 255))
    computer_score_text = font.render(f"Computer's Score: {computer.score}", True, (255, 255, 255))

    screen.blit(points_distributed_text, (20, 280))
    screen.blit(user_score_text, (20, 310))
    screen.blit(computer_score_text, (20, 340))

    pygame.display.flip()

def display_game_state(screen, user, computer, diamond_cards):
    screen.fill((0, 0, 0))

    diamond_card_text = font.render("Diamond Card:", True, (255, 255, 255))
    screen.blit(diamond_card_text, (screen_width // 2 - diamond_card_text.get_width() // 2, 20))
    if diamond_cards:
        card = diamond_cards[0]
        card_image = pygame.image.load(card_image_paths[f"{card.rank} of {card.suit}"])
        resized_card_image = pygame.transform.scale(card_image, (160, 240))
        card_rect = resized_card_image.get_rect()
        card_rect.centerx = screen_width // 2
        card_rect.top = 100
        screen.blit(resized_card_image, card_rect)

    user_hand_text = font.render("Your Hand:", True, (255, 255, 255))
    screen.blit(user_hand_text, (20, screen_height - 100))
    x_offset = 20
    y_offset = screen_height - 300
    card_width = 104
    spacing = 0
    for card in user.hand:
        card_image = pygame.image.load(card_image_paths[f"{card.rank} of {card.suit}"])
        resized_card_image = pygame.transform.scale(card_image, (100, 180))
        card_rect = resized_card_image.get_rect()
        card_rect.topleft = (x_offset, y_offset)
        screen.blit(resized_card_image, card_rect)
        x_offset += card_width + spacing

    user_score_text = font.render(f"Your Score: {user.score}", True, (255, 255, 255))
    screen.blit(user_score_text, (screen_width - user_score_text.get_width() - 100, 20))
    computer_score_text = font.render(f"Computer's Score: {computer.score}", True, (255, 255, 255))
    screen.blit(computer_score_text, (screen_width - user_score_text.get_width() - 100, 50))

    start_button_text = font.render("Start", True, (255, 255, 255))
    stop_button_text = font.render("Stop", True, (255, 255, 255))
    quit_button_text = font.render("Quit", True, (255, 255, 255))
    screen.blit(start_button_text, (20, 20))
    screen.blit(stop_button_text, (90, 20))
    screen.blit(quit_button_text, (160, 20))

    pygame.display.flip()

def check_end_game(screen, diamond_cards, user, computer):
    if len(diamond_cards) == 0:
        if user.score > computer.score:
            message = "Congratulations! You win!"
        elif user.score < computer.score:
            message = "Computer wins!"
        else:
            message = "It's a tie!"
        
        font = pygame.font.SysFont(None, 60)
        text = font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        
        screen.fill((0, 0, 0))
        
        screen.blit(text, text_rect)
        pygame.display.flip()
        
        return True
    else:
        return False

def get_user_bid(user):
    selected_card = None
    while selected_card is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i, card in enumerate(user.hand):
                    card_x = 20 + i * 104
                    card_rect = pygame.Rect((card_x, screen_height - 300), (100, 180))
                    if card_rect.collidepoint(mouse_x, mouse_y):
                        selected_card = i
                        break
        display_game_state(screen, user, computer, diamond_cards)
    return selected_card

def main():
    running = True

    for diamond_card in diamond_cards:
        display_diamond_cards([diamond_card])
        user_bid, computer_bid = bid_phase(screen, user, computer, diamond_card)
        resolve_bids(user_bid, computer_bid, diamond_card)

        if check_end_game(screen, diamond_cards, user, computer):
            break

        pygame.time.delay(8000)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
