import pygame

# Configura��es b�sicas
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 15

# Inicializa o pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# Posi��es iniciais
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 4, 4
paddle1_y, paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2, HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle_speed = 6

# Pontua��o
score1, score2 = 0, 0
font = pygame.font.Font(None, 36)

def save_score(score1, score2):
    with open("scores.txt", "a") as file:
        file.write(f"{score1} - {score2}\n")

# Loop do jogo
running = True
while running:
    screen.fill(BLACK)
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Controles dos paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += paddle_speed
    
    # Movimento da bola
    ball_x += ball_dx
    ball_y += ball_dy
    
    # Colis�o com paredes
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_dy *= -1
    
    # Colis�o com os paddles
    if (ball_x <= PADDLE_WIDTH and paddle1_y < ball_y < paddle1_y + PADDLE_HEIGHT) or \
       (ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and paddle2_y < ball_y < paddle2_y + PADDLE_HEIGHT):
        ball_dx *= -1
    
    # Pontua��o
    if ball_x < 0:
        score2 += 1
        save_score(score1, score2)
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx *= -1
    if ball_x > WIDTH:
        score1 += 1
        save_score(score1, score2)
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx *= -1
    
    # Desenho dos elementos
    pygame.draw.rect(screen, WHITE, (0, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    
    # Exibe pontua��o
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
