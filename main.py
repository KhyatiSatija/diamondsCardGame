import pygame
import random
import sys
import time
import gameflow
import interface
import strategy
pygame.init()

screen_width = 1400 
screen_height = 750 
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Game of Diamonds") 
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
        self.hand = [] 
        self.score = 0  

user = Player("User")
computer = Player("Computer")


def initialize_deck(suit):
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    return [Card(rank, suit) for rank in ranks]

user.hand = initialize_deck('Hearts')
computer.hand = initialize_deck('Spades')
diamond_ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
diamond_cards = [Card(rank, 'Diamonds') for rank in diamond_ranks]



def display_game_screen(screen, user, computer, diamond_cards):
    # Display user's hand horizontally from left to right, ensuring the left half is visible
    user_hand_text = font.render("Your Hand:", True, (255, 255, 255))
    screen.blit(user_hand_text, (20, screen_height - 100))
    x_offset = 20
    y_offset = screen_height - 300
    card_width = 100  # Width of each card image
    spacing = 4 # Spacing between cards
    for card in user.hand:
        card_image = pygame.image.load(card_image_paths[f"{card.rank} of {card.suit}"])
        # Resize the card image to desired dimensions (e.g., 80x120)
        resized_card_image = pygame.transform.scale(card_image, (100, 180))
        card_rect = resized_card_image.get_rect()
        card_rect.topleft = (x_offset, y_offset)
        screen.blit(resized_card_image, card_rect)
        x_offset += card_width + spacing # Adjust spacing between cards

    # Display user's score on the top right of the pygame window
    user_score_text = font.render(f"Your Score: {user.score}", True, (255, 255, 255))
    screen.blit(user_score_text, (screen_width - user_score_text.get_width() - 100, 20))
    computer_score_text = font.render(f"Computer's Score: {computer.score}", True, (255, 255, 255))
    screen.blit(computer_score_text, (screen_width - user_score_text.get_width() - 100, 50))
    # Buttons on the top left of the pygame window
    start_button_text = font.render("Start", True, (255, 255, 255))
    stop_button_text = font.render("Stop", True, (255, 255, 255))
    quit_button_text = font.render("Quit", True, (255, 255, 255))
    screen.blit(start_button_text, (20, 20))
    screen.blit(stop_button_text, (90, 20))
    screen.blit(quit_button_text, (160, 20))

    # Update the display
    pygame.display.flip()

def generate_random_diamond(screen, user, computer, diamond_cards):
    screen.fill((0, 0, 0))
    diamond_card_text = font.render("Diamond Card:", True, (255, 255, 255))
    screen.blit(diamond_card_text, (screen_width // 2 - diamond_card_text.get_width() // 2, 20))
    random.shuffle(diamond_cards)
    card = diamond_cards.pop()
    card_image = pygame.image.load(card_image_paths[f"{card.rank} of {card.suit}"])
    resized_card_image = pygame.transform.scale(card_image, (160, 240))
    card_rect = resized_card_image.get_rect()
    card_rect.centerx = screen_width // 2
    card_rect.top = 100
    screen.blit(resized_card_image, card_rect)
    pygame.display.flip()
    return card, diamond_cards
def bid_phase(screen, user, computer, diamond_card):
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # User bids
    user_bid_text = font.render("Your turn to bid:", True, (255, 255, 255))
    screen.blit(user_bid_text, (screen_width // 2, (screen_height // 2 ) - 5))
    pygame.display.flip()

    # Get user's bid index
    user_bid_index = get_user_bid(user)
    user_bid = user.hand.pop(user_bid_index)  # Remove the selected card from the user's hand


    # Display the user's bid
    user_bid_display = font.render(f"You bid with: {user_bid.rank}", True, (255, 255, 255))
    screen.blit(user_bid_display, (20, 100))
    pygame.display.flip()

    # Computer bids
    computer_bid_text = font.render("Computer's turn to bid:", True, (255, 255, 255))
    screen.blit(computer_bid_text, (20, 130))
    pygame.display.flip()

    # computer_bid = strategy.computer_bid(user, computer,diamond_card)  

    # Randomly select a card index from the computer's hand
    computer_bid_index = random.randint(0, len(computer.hand) - 1)
    computer_bid = computer.hand.pop(computer_bid_index)  # Remove the selected card from the computer's hand

    # Display the computer's bid
    computer_bid_display = font.render(f"Computer bids with: {computer_bid.rank}", True, (255, 255, 255))
    screen.blit(computer_bid_display, (20, 160))
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
        points_per_player = diamond_card.rank / 2  # Divide points equally among tied players
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
    screen.blit(winning_player_text, (20, 250))
    screen.blit(points_distributed_text, (20, 280))
    screen.blit(user_score_text, (20, 310))
    screen.blit(computer_score_text, (20, 340))

    # Update the display
    pygame.display.flip()

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
                    card_x = 20 + i * 104  # Calculate the x-coordinate of the card dynamically
                    card_rect = pygame.Rect((card_x, screen_height - 300), (100, 180))  # Assuming card dimensions are 160x240
                    if card_rect.collidepoint(mouse_x, mouse_y):
                        selected_card = i
                        break
        # Draw the game state after each iteration to update the display
        display_game_screen(screen, user, computer, diamond_cards)
    return selected_card
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

def main(diamond_cards):
    
    running = True
    while diamond_cards:
        display_game_screen(screen, user, computer, diamond_cards)
        random_diamond, diamond_cards = generate_random_diamond(screen, user, computer, diamond_cards)
        pygame.time.delay(2000)
        user_bid, computer_bid = bid_phase(screen, user, computer, random_diamond)
        resolve_bids(user_bid, computer_bid, random_diamond)
        pygame.time.delay(5000)
        if check_end_game(screen, diamond_cards, user, computer):
            break

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main(diamond_cards)