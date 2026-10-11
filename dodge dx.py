import pygame
import random

pygame.init()

# Window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DODGE!")

clock = pygame.time.Clock()

# Colors
BLACK = (20, 20, 30)
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 70, 70)
GRAY = (80, 80, 90)

# Player
player = pygame.Rect(375, 520, 50, 50)
player_speed = 7

# Falling enemies
enemies = []
enemy_speed = 5
spawn_timer = 0

# Score
score = 0
font = pygame.font.Font(None, 45)
big_font = pygame.font.Font(None, 80)

game_over = False
running = True

while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                # Restart
                enemies.clear()
                score = 0
                enemy_speed = 5
                spawn_timer = 0
                game_over = False

    keys = pygame.key.get_pressed()

    if not game_over:

        # Player movement
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.x -= player_speed

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.x += player_speed

        # Keep player inside screen
        if player.left < 0:
            player.left = 0

        if player.right > WIDTH:
            player.right = WIDTH

        # Spawn enemies
        spawn_timer += 1

        if spawn_timer >= 35:
            spawn_timer = 0

            enemy_x = random.randint(0, WIDTH - 40)

            enemy = pygame.Rect(
                enemy_x,
                -40,
                40,
                40
            )

            enemies.append(enemy)

        # Move enemies
        for enemy in enemies[:]:
            enemy.y += enemy_speed

            # Player hit enemy
            if player.colliderect(enemy):
                game_over = True

            # Enemy escaped
            if enemy.top > HEIGHT:
                enemies.remove(enemy)
                score += 1

        # Slowly increase difficulty
        if score > 0 and score % 10 == 0:
            enemy_speed = 5 + score // 10

    # -------------------------
    # DRAW
    # -------------------------

    screen.fill(BLACK)

    # Player
    pygame.draw.rect(screen, BLUE, player)

    # Enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Score
    score_text = font.render(
        "Score: " + str(score),
        True,
        WHITE
    )

    screen.blit(score_text, (20, 20))

    # Game over screen
    if game_over:

        game_over_text = big_font.render(
            "GAME OVER",
            True,
            RED
        )

        restart_text = font.render(
            "Press R to restart",
            True,
            WHITE
        )

        screen.blit(
            game_over_text,
            (
                WIDTH // 2 - game_over_text.get_width() // 2,
                HEIGHT // 2 - 70
            )
        )

        screen.blit(
            restart_text,
            (
                WIDTH // 2 - restart_text.get_width() // 2,
                HEIGHT // 2 + 20
            )
        )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()