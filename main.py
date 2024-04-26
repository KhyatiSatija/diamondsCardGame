import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the Pygame window
screen_width = 1400  # Set your desired screen width
screen_height = 750  # Set your desired screen height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game of Diamonds")  # Set the window title

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

    '2 of Hearts': 'PNG-cards-1.3/2_of_hearts.png',
    '3 of Hearts': 'PNG-cards-1.3/3_of_hearts.png',
    '4 of Hearts': 'PNG-cards-1.3/4_of_hearts.png',
    '5 of Hearts': 'PNG-cards-1.3/5_of_hearts.png',
    '6 of Hearts': 'PNG-cards-1.3/6_of_hearts.png',
    '7 of Hearts': 'PNG-cards-1.3/7_of_hearts.png',
    '8 of Hearts': 'PNG-cards-1.3/8_of_hearts.png',
    '9 of Hearts': 'PNG-cards-1.3/9_of_hearts.png',
    '10 of Hearts': 'PNG-cards-1.3/10_of_hearts.png',
    '11 of Hearts': 'PNG-cards-1.3/jack_of_hearts.png',
    '12 of Hearts': 'PNG-cards-1.3/queen_of_hearts.png',
    '13 of Hearts': 'PNG-cards-1.3/king_of_hearts.png',
    '14 of Hearts': 'PNG-cards-1.3/ace_of_hearts.png',

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
        self.hand = []  # Initialize an empty list to store the player's cards
        self.score = 0  # Initialize the player's score to 0

# Initialize players
user = Player("User")
computer = Player("Computer")

# Initialize deck of cards
def initialize_deck(suit):
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    return [Card(rank, suit) for rank in ranks]

# Initialize decks for user and computer
user.hand = initialize_deck('Hearts')
computer.hand = initialize_deck('Spades')

# Create a deck of diamond cards
diamond_ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
diamond_cards = [Card(rank, 'Diamonds') for rank in diamond_ranks]

# Shuffle the diamond cards deck
random.shuffle(diamond_cards)

def display_diamond_cards(diamond_cards):
    for card in diamond_cards:
        card_image = pygame.image.load(card_image_paths[f"{card.rank} of {card.suit}"])
        card_rect = card_image.get_rect()
        card_rect.center = (screen_width // 2, screen_height // 2)  # Center the card on the screen
        screen.blit(card_image, card_rect)  # Draw the card on the screen
        pygame.display.flip()  # Update the display
        # pygame.time.delay(4000)  # Pause for 1 second before displaying the next card

def bid_phase(screen, user, computer, diamond_card):
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # User bids
    user_bid_text = font.render("Your turn to bid:", True, (255, 255, 255))
    screen.blit(user_bid_text, (screen_width // 2, (screen_height // 2 )+ 100))
    pygame.display.flip()

    # Get user's bid index
    user_bid_index = get_user_bid(user)
    user_bid = user.hand.pop(user_bid_index)  # Remove the selected card from the user's hand

    # Update the user's score
    user.score += diamond_card.rank

    # Display the user's bid
    user_bid_display = font.render(f"You bid with: {user_bid.rank}", True, (255, 255, 255))
    screen.blit(user_bid_display, (20, 50))
    pygame.display.flip()

    # Computer bids (assuming random bidding)
    computer_bid_text = font.render("Computer's turn to bid:", True, (255, 255, 255))
    screen.blit(computer_bid_text, (20, 80))
    pygame.display.flip()

    # Randomly select a card index from the computer's hand
    computer_bid_index = random.randint(0, len(computer.hand) - 1)
    computer_bid = computer.hand.pop(computer_bid_index)  # Remove the selected card from the computer's hand

    # Update the computer's score
    computer.score += diamond_card.rank

    # Display the computer's bid
    computer_bid_display = font.render(f"Computer bids with: {computer_bid.rank}", True, (255, 255, 255))
    screen.blit(computer_bid_display, (20, 110))
    pygame.display.flip()

    # Display the selected cards
    display_selected_cards(screen, user_bid, computer_bid)

    return user_bid, computer_bid


def display_selected_cards(screen, user_card, computer_card):
    # Adjust the vertical offset for displaying the cards
    vertical_offset = 200
    # Adjust the horizontal offset for displaying the user's card
    user_horizontal_offset = 200
    # Adjust the horizontal offset for displaying the computer's card
    computer_horizontal_offset = 250

    # Display the user's selected card shifted to the left
    user_selected_text = font.render("You chose:", True, (255, 255, 255))
    screen.blit(user_selected_text, (screen_width - 250 - user_horizontal_offset, screen_height // 2 - 50 - vertical_offset))
    display_card(user_card, screen_width - 250 - user_horizontal_offset, screen_height // 2 - vertical_offset)

    # Display the computer's selected card shifted to the right
    computer_selected_text = font.render("Computer chose:", True, (255, 255, 255))
    screen.blit(computer_selected_text, (50 + computer_horizontal_offset, screen_height // 2 - 50 - vertical_offset))
    display_card(computer_card, 50 + computer_horizontal_offset, screen_height // 2 - vertical_offset)



def display_card(card, x, y):
    card_image = pygame.image.load(card_image_paths[f"{card.rank} of {card.suit}"])
    resized_card_image = pygame.transform.scale(card_image, (160, 240))
    card_rect = resized_card_image.get_rect()
    card_rect.topleft = (x, y)
    screen.blit(resized_card_image, card_rect)   

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

    # Display the result of the bid resolution
    winning_player_text = font.render(f"Winner: {winning_player}", True, (255, 255, 255))
    points_distributed_text = font.render(f"Points distributed: {diamond_card.rank}", True, (255, 255, 255))
    user_score_text = font.render(f"User's score: {user.score}", True, (255, 255, 255))
    computer_score_text = font.render(f"Computer's score: {computer.score}", True, (255, 255, 255))

    # Blit the text onto the screen
    screen.blit(winning_player_text, (20, 140))
    screen.blit(points_distributed_text, (20, 170))
    screen.blit(user_score_text, (20, 200))
    screen.blit(computer_score_text, (20, 230))

    # Update the display
    pygame.display.flip()

def display_game_state(screen, user, computer, diamond_cards):
    # Clear the screen
    screen.fill((0, 0, 0)) #black color

    # Display diamond card at the top center of the screen
    diamond_card_text = font.render("Diamond Card:", True, (255, 255, 255))
    screen.blit(diamond_card_text, (screen_width // 2 - diamond_card_text.get_width() // 2, 20))
    if diamond_cards:
        card = diamond_cards[0]  # Assuming only one diamond card is auctioned at a time
        card_image = pygame.image.load(card_image_paths[f"{card.rank} of {card.suit}"])
        resized_card_image = pygame.transform.scale(card_image, (160, 240))
        card_rect = resized_card_image.get_rect()
        card_rect.centerx = screen_width // 2
        card_rect.top = 100
        screen.blit(resized_card_image, card_rect)

    # Display user's hand horizontally from left to right, ensuring the left half is visible
    user_hand_text = font.render("Your Hand:", True, (255, 255, 255))
    screen.blit(user_hand_text, (20, screen_height - 100))
    x_offset = 20
    y_offset = screen_height - 300
    for card in user.hand:
        card_image = pygame.image.load(card_image_paths[f"{card.rank} of {card.suit}"])
        # Resize the card image to desired dimensions (e.g., 80x120)
        resized_card_image = pygame.transform.scale(card_image, (160, 240))
        card_rect = resized_card_image.get_rect()
        card_rect.topleft = (x_offset, y_offset)
        screen.blit(resized_card_image, card_rect)
        x_offset += 95  # Adjust spacing between cards

    # Display user's score on the top right of the pygame window
    user_score_text = font.render(f"Your Score: {user.score}", True, (255, 255, 255))
    screen.blit(user_score_text, (screen_width - user_score_text.get_width() - 20, 20))

    # Buttons on the top left of the pygame window
    start_button_text = font.render("Start", True, (255, 255, 255))
    stop_button_text = font.render("Stop", True, (255, 255, 255))
    quit_button_text = font.render("Quit", True, (255, 255, 255))
    screen.blit(start_button_text, (20, 20))
    screen.blit(stop_button_text, (20, 50))
    screen.blit(quit_button_text, (20, 80))

    # Update the display
    pygame.display.flip()


def check_end_game(screen, diamond_cards, user, computer):
    if len(diamond_cards) == 0:
        # All diamond cards have been auctioned
        # Determine the winner based on total points accumulated by each player
        if user.score > computer.score:
            message = "Congratulations! You win!"
        elif user.score < computer.score:
            message = "Computer wins!"
        else:
            message = "It's a tie!"
        
        # Display the winning message in big font at the center of the screen
        font = pygame.font.SysFont(None, 60)  # You can adjust the font size as needed
        text = font.render(message, True, (255, 255, 255))  # White color text
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Display the winning message
        screen.blit(text, text_rect)
        pygame.display.flip()
        
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
                    card_x = 20 + i * 95  # Calculate the x-coordinate of the card dynamically
                    card_rect = pygame.Rect((card_x, screen_height - 300), (160, 240))  # Assuming card dimensions are 160x240
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

# Main game loop
def main():
    running = True

    # Auction diamond cards one by one
    for diamond_card in diamond_cards:
        # Display the diamond card being auctioned
        display_diamond_cards([diamond_card])

        # Bid phase
        user_bid, computer_bid = bid_phase(screen, user, computer, diamond_card)
        
        # Resolve bids and display result
        resolve_bids(user_bid, computer_bid, diamond_card)

        # Check if the game has ended
        if check_end_game(screen, diamond_cards, user, computer):
            break

        # Pause for a moment before proceeding to the next auction
        pygame.time.delay(5000)

    # Display final scores
    display_scores(user.score, computer.score)

    # Keep the window open until the user closes it
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
