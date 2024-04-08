import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the Pygame window
screen_width = 800  # Set your desired screen width
screen_height = 600  # Set your desired screen height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game of Diamonds")  # Set the window title

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
    'Jack of Diamonds': 'PNG-cards-1.3/jack_of_diamonds.png',
    'Queen of Diamonds': 'PNG-cards-1.3/queen_of_diamonds.png',
    'King of Diamonds': 'PNG-cards-1.3/king_of_diamonds.png',
    'Ace of Diamonds': 'PNG-cards-1.3/ace_of_diamonds.png',

    '2 of Hearts': 'PNG-cards-1.3/2_of_hearts.png',
    '3 of Hearts': 'PNG-cards-1.3/3_of_hearts.png',
    '4 of Hearts': 'PNG-cards-1.3/4_of_hearts.png',
    '5 of Hearts': 'PNG-cards-1.3/5_of_hearts.png',
    '6 of Hearts': 'PNG-cards-1.3/6_of_hearts.png',
    '7 of Hearts': 'PNG-cards-1.3/7_of_hearts.png',
    '8 of Hearts': 'PNG-cards-1.3/8_of_hearts.png',
    '9 of Hearts': 'PNG-cards-1.3/9_of_hearts.png',
    '10 of Hearts': 'PNG-cards-1.3/10_of_hearts.png',
    'Jack of Hearts': 'PNG-cards-1.3/jack_of_hearts.png',
    'Queen of Hearts': 'PNG-cards-1.3/queen_of_hearts.png',
    'King of Hearts': 'PNG-cards-1.3/king_of_hearts.png',
    'Ace of Hearts': 'PNG-cards-1.3/ace_of_hearts.png',

    '2 of Spades': 'PNG-cards-1.3/2_of_spades.png',
    '3 of Spades': 'PNG-cards-1.3/3_of_spades.png',
    '4 of Spades': 'PNG-cards-1.3/4_of_spades.png',
    '5 of Spades': 'PNG-cards-1.3/5_of_spades.png',
    '6 of Spades': 'PNG-cards-1.3/6_of_spades.png',
    '7 of Spades': 'PNG-cards-1.3/7_of_spades.png',
    '8 of Spades': 'PNG-cards-1.3/8_of_spades.png',
    '9 of Spades': 'PNG-cards-1.3/9_of_spades.png',
    '10 of Spades': 'PNG-cards-1.3/10_of_spades.png',
    'Jack of Spades': 'PNG-cards-1.3/jack_of_spades.png',
    'Queen of Spades': 'PNG-cards-1.3/queen_of_spades.png',
    'King of Spades': 'PNG-cards-1.3/king_of_spades.png',
    'Ace of Spades': 'PNG-cards-1.3/ace_of_spades.png',

    '2 of Clubs': 'PNG-cards-1.3/2_of_clubs.png',
    '3 of Clubs': 'PNG-cards-1.3/3_of_clubs.png',
    '4 of Clubs': 'PNG-cards-1.3/4_of_clubs.png',
    '5 of Clubs': 'PNG-cards-1.3/5_of_clubs.png',
    '6 of Clubs': 'PNG-cards-1.3/6_of_clubs.png',
    '7 of Clubs': 'PNG-cards-1.3/7_of_clubs.png',
    '8 of Clubs': 'PNG-cards-1.3/8_of_clubs.png',
    '9 of Clubs': 'PNG-cards-1.3/9_of_clubs.png',
    '10 of Clubs': 'PNG-cards-1.3/10_of_clubs.png',
    'Jack of Clubs': 'PNG-cards-1.3/jack_of_clubs.png',
    'Queen of Clubs': 'PNG-cards-1.3/queen_of_clubs.png',
    'King of Clubs': 'PNG-cards-1.3/king_of_clubs.png',
    'Ace of Clubs': 'PNG-cards-1.3/ace_of_clubs.png',
}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []  # Initialize an empty list to store the player's cards
        self.score = 0  # Initialize the player's score to 0

# Initialize players
user = Player("User")
computer = Player("Computer")

# Initialize deck of cards (excluding diamonds)
suits = ['Hearts', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = [Card(rank, suit) for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Create a deck of diamond cards
diamond_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
diamond_cards = [Card(rank, 'Diamonds') for rank in diamond_ranks]

# Shuffle the diamond cards deck
random.shuffle(diamond_cards)

# Distribute cards to each player's hand
num_initial_cards = 5  # Number of cards each player starts with
for _ in range(num_initial_cards):
    user.hand.append(deck.pop())
    computer.hand.append(deck.pop())

def display_diamond_cards(diamond_cards):
    for card in diamond_cards:
        # Render and display the card on the screen using Pygame's drawing functions
        # You can use text or images to represent the cards
        # For example:
        card_image = pygame.image.load(card_image_paths[f"{card.rank} of {card.suit}"])
        card_rect = card_image.get_rect()
        card_rect.center = (screen_width // 2, screen_height // 2)  # Center the card on the screen
        screen.blit(card_image, card_rect)  # Draw the card on the screen
        pygame.display.flip()  # Update the display
        pygame.time.delay(1000)  # Pause for 1 second before displaying the next card

def bid_phase(screen, user, computer, diamond_card):
    # User bids
    print("User's turn to bid:")
    print("Your hand:", [card.rank for card in user.hand])
    user_bid_index = get_user_bid(user)  # Get user's bid index
    user_bid = user.hand.pop(user_bid_index)  # Remove the selected card from the user's hand
    print("You bid with:", user_bid.rank)
    # Update the user's score (assuming the card rank represents the points)
    user.score += diamond_card.rank

    # Computer bids (assuming random bidding)
    print("Computer's turn to bid:")
    computer_bid_index = random.randint(0, len(computer.hand) - 1)  # Randomly select a card index from the computer's hand
    computer_bid = computer.hand.pop(computer_bid_index)  # Remove the selected card from the computer's hand
    print("Computer bids with:", computer_bid.rank)
    # Update the computer's score (assuming the card rank represents the points)
    computer.score += diamond_card.rank

    return user_bid, computer_bid

def resolve_bids(user_bid, computer_bid, diamond_card):
    # Determine the winning bid
    if user_bid.rank > computer_bid.rank:
        winning_player = "User"
    elif user_bid.rank < computer_bid.rank:
        winning_player = "Computer"
    else:
        winning_player = "Tie"

    # If there's a tie, divide the points of the diamond card equally among tied players
    if winning_player == "Tie":
        points_per_player = diamond_card.rank // 2  # Divide points equally among tied players
        user.score += points_per_player
        computer.score += points_per_player
    else:
        # The winning player gets all the points of the diamond card
        if winning_player == "User":
            user.score += diamond_card.rank
        else:
            computer.score += diamond_card.rank

    # Print the result of the bid resolution
    print("Winner:", winning_player)
    print("Points distributed:", diamond_card.rank)
    print("User's score:", user.score)
    print("Computer's score:", computer.score)

def display_game_state(screen, user, computer, diamond_cards):
    # Clear the screen
    screen.fill((0, 0, 0))

    # Display player scores
    font = pygame.font.SysFont(None, 30)
    user_score_text = font.render(f"User Score: {user.score}", True, (255, 255, 255))
    computer_score_text = font.render(f"Computer Score: {computer.score}", True, (255, 255, 255))
    screen.blit(user_score_text, (20, 20))
    screen.blit(computer_score_text, (20, 50))

    # Display diamond cards auctioned
    diamond_card_text = font.render("Diamond Cards Auctioned:", True, (255, 255, 255))
    screen.blit(diamond_card_text, (20, 100))
    y_offset = 130
    for card in diamond_cards:
        card_image = pygame.image.load(card_image_paths[f"{card.rank} of {card.suit}"])
        card_rect = card_image.get_rect()
        card_rect.topleft = (20, y_offset)
        screen.blit(card_image, card_rect)
        y_offset += 30

    # Display user's hand
    user_hand_text = font.render("Your Hand:", True, (255, 255, 255))
    screen.blit(user_hand_text, (screen.get_width() // 2, 20))
    x_offset = screen.get_width() // 2
    y_offset = 50
    for card in user.hand:
        card_image = pygame.image.load(card_image_paths[f"{card.rank} of {card.suit}"])
        card_rect = card_image.get_rect()
        card_rect.topleft = (x_offset, y_offset)
        screen.blit(card_image, card_rect)
        y_offset += 30

    # Update the display
    pygame.display.flip()

def check_end_game(diamond_cards, user, computer):
    if len(diamond_cards) == 0:
        # All diamond cards have been auctioned
        # Determine the winner based on total points accumulated by each player
        if user.score > computer.score:
            print("Congratulations! You win!")
        elif user.score < computer.score:
            print("Computer wins!")
        else:
            print("It's a tie!")
        return True  # End the game
    else:
        return False  # Continue the game

def get_user_bid(user):
    selected_card = None
    while selected_card is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check if the mouse click is on one of the user's cards
                for i, card in enumerate(user.hand):
                    card_rect = pygame.Rect((i * 120 + 20, 80), (100, 150))  # Assuming card dimensions are 100x150
                    if card_rect.collidepoint(mouse_x, mouse_y):
                        selected_card = i
                        break
        # Draw the game state after each iteration to update the display
        display_game_state(screen, user, computer, diamond_cards)
    return selected_card

# Display player scores
def display_scores(user_score, computer_score):
    font = pygame.font.SysFont(None, 30)
    user_score_text = font.render(f"User Score: {user_score}", True, (255, 255, 255))
    computer_score_text = font.render(f"Computer Score: {computer_score}", True, (255, 255, 255))
    screen.blit(user_score_text, (20, 20))
    screen.blit(computer_score_text, (20, 50))

# Display player hand
def display_hand(player, x_offset):
    font = pygame.font.SysFont(None, 30)
    user_hand_text = font.render(f"{player.name}'s Hand:", True, (255, 255, 255))
    screen.blit(user_hand_text, (x_offset, 20))
    y_offset = 50
    for card in player.hand:
        card_image = pygame.image.load(card_image_paths[f"{card.rank} of {card.suit}"])
        card_rect = card_image.get_rect()
        card_rect.topleft = (x_offset, y_offset)
        screen.blit(card_image, card_rect)
        y_offset += 30

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 128, 0))

    # Display player scores
    display_scores(user.score, computer.score)

    # Display player hands
    display_hand(user, 120)
    display_hand(computer, 320)

    # Update the display
    pygame.display.flip()
