import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define paddle properties
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PLAYER_X, PLAYER_Y = 50, (HEIGHT - PADDLE_HEIGHT) // 2
COMPUTER_X, COMPUTER_Y = WIDTH - 50 - PADDLE_WIDTH, (HEIGHT - PADDLE_HEIGHT) // 2
PADDLE_SPEED = 5

# Define ball properties
BALL_SIZE = 20
BALL_X, BALL_Y = WIDTH // 2, HEIGHT // 2
BALL_X_SPEED, BALL_Y_SPEED = 5, 5

# Define fonts
FONT = pygame.font.SysFont('comicsans', 40)

# Initialize scores
player_score = 0
computer_score = 0

def draw_window():
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, (PLAYER_X, PLAYER_Y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(WIN, WHITE, (COMPUTER_X, COMPUTER_Y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(WIN, WHITE, (BALL_X, BALL_Y, BALL_SIZE, BALL_SIZE))
    
    # Draw scores
    player_text = FONT.render(f"Player: {player_score}", 1, WHITE)
    computer_text = FONT.render(f"Computer: {computer_score}", 1, WHITE)
    WIN.blit(player_text, (WIDTH // 4 - player_text.get_width() // 2, 20))
    WIN.blit(computer_text, (3 * WIDTH // 4 - computer_text.get_width() // 2, 20))
    
    pygame.display.update()

def handle_player_movement(keys):
    global PLAYER_Y
    if keys[pygame.K_UP] and PLAYER_Y - PADDLE_SPEED > 0:
        PLAYER_Y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and PLAYER_Y + PADDLE_SPEED + PADDLE_HEIGHT < HEIGHT:
        PLAYER_Y += PADDLE_SPEED

def handle_computer_movement():
    global COMPUTER_Y, BALL_Y
    if COMPUTER_Y + PADDLE_HEIGHT // 2 < BALL_Y + BALL_SIZE // 2:
        COMPUTER_Y += PADDLE_SPEED
    if COMPUTER_Y + PADDLE_HEIGHT // 2 > BALL_Y + BALL_SIZE // 2:
        COMPUTER_Y -= PADDLE_SPEED

def handle_ball_movement():
    global BALL_X, BALL_Y, BALL_X_SPEED, BALL_Y_SPEED, player_score, computer_score
    BALL_X += BALL_X_SPEED
    BALL_Y += BALL_Y_SPEED

    # Ball collision with top and bottom walls
    if BALL_Y <= 0 or BALL_Y + BALL_SIZE >= HEIGHT:
        BALL_Y_SPEED *= -1

    # Ball collision with player paddle
    if PLAYER_X < BALL_X < PLAYER_X + PADDLE_WIDTH and PLAYER_Y < BALL_Y < PLAYER_Y + PADDLE_HEIGHT:
        BALL_X_SPEED *= -1

    # Ball collision with computer paddle
    if COMPUTER_X < BALL_X + BALL_SIZE < COMPUTER_X + PADDLE_WIDTH and COMPUTER_Y < BALL_Y < COMPUTER_Y + PADDLE_HEIGHT:
        BALL_X_SPEED *= -1

    # Ball goes out of bounds
    if BALL_X <= 0:
        computer_score += 1
        reset_ball()
    elif BALL_X + BALL_SIZE >= WIDTH:
        player_score += 1
        reset_ball()

def reset_ball():
    global BALL_X, BALL_Y, BALL_X_SPEED, BALL_Y_SPEED
    BALL_X, BALL_Y = WIDTH // 2, HEIGHT // 2
    BALL_X_SPEED *= -1

def main():
    global PLAYER_Y, COMPUTER_Y
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)  # 60 frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        handle_player_movement(keys)
        handle_computer_movement()
        handle_ball_movement()
        draw_window()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
