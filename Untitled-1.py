
import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set the game window dimensions
window_width = 640
window_height = 480

# Create the game window
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Super Mario Clone')

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set fonts
font = pygame.font.SysFont(None, 25)

# Define the player
player_width = 50
player_height = 50
player_x = 50
player_y = window_height - player_height - 50
player_speed = 10

# Define the obstacles
obstacle_width = 50
obstacle_height = 50
obstacle_x = window_width + obstacle_width
obstacle_y = window_height - obstacle_height - 50
obstacle_speed = 5

# Set the game clock
clock = pygame.time.Clock()

# Define a function to draw the player
def draw_player(x, y):
    pygame.draw.rect(game_display, white, [x, y, player_width, player_height])

# Define a function to draw the obstacle
def draw_obstacle(x, y):
    pygame.draw.rect(game_display, black, [x, y, obstacle_width, obstacle_height])

# Define a function to display text messages
def message_display(text):
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.center = (window_width/2, window_height/2)
    game_display.blit(text_surface, text_rect)

    # Update the screen
    pygame.display.update()

    # Wait for a short time
    time.sleep(2)

# Define the game loop
def game_loop():
    game_exit = False
    game_over = False

    # Loop until the player chooses to exit the game
    while not game_exit:
        # If the game is over, wait for the player to choose to play again or exit
        while game_over == True:
            message_display('Game over! Press C to play again, or Q to quit.')
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        game_loop()
                    elif event.key == pygame.K_q:
                        game_exit = True
                        game_over = False

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_y -= player_speed * 2

        # Update the player position
        player_y += player_speed

        # Move the obstacle
        obstacle_x -= obstacle_speed

        # If the obstacle goes offscreen, move it back and change its height
        if obstacle_x < 0:
            obstacle_x = window_width + obstacle_width
            obstacle_y = random.randint(0, window_height - obstacle_height - 50)

        # Draw the player and obstacle
        game_display.fill(black)
        draw_player(player_x, player_y)
        draw_obstacle(obstacle_x, obstacle_y)

        # Check for collisions
        if player_y > window_height - player_height or player_y < 0:
            game_over = True

        if obstacle_x < player_x + player_width < obstacle_x + obstacle_width and obstacle_y < player_y + player_height < obstacle_y + obstacle_height:
            game_over = True

        # Update the screen
        pygame.display.update()

        # Set the game clock speed
        clock.tick(60)

    pygame.quit()
    quit()

# Start the game loop
game_loop()