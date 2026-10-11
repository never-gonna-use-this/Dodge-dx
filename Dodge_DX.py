import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dodge DX")

clock = pygame.time.Clock()

player = pygame.Rect(370, 100, 50, 50)
player_speed = 5

enemies = []
spawn_time = 0
enemy_speed = 5

game_over = False
running = True

while running:
    clock.tick(random.randint(60, 800))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                player.x = 370
                player.y = 100
                enemy_speed = 0
                enemies.clear()
                spawn_time = 0
                game_over = False

    keys = pygame.key.get_pressed()

    if not game_over:
        enemy_speed += random.randint(1, 5)

        if enemy_speed >= 6:
            enemy_speed = 0

        if keys[pygame.K_a]:
            player.x -= player_speed
        if keys[pygame.K_d]:
            player.x += player_speed
        if keys[pygame.K_w]:
            player.y -= player_speed
        if keys[pygame.K_s]:
            player.y += player_speed

        player.clamp_ip(screen.get_rect())

        spawn_time += 1

        if spawn_time >= 50:
            spawn_time = 0
            x = random.randint(0, 750)
            enemy = pygame.Rect(x, 650, 50, 50)
            enemies.append(enemy)

        for enemy in enemies:
            enemy.y -= enemy_speed
            if player.colliderect(enemy):
                game_over = True

        enemies = [enemy for enemy in enemies if enemy.top <= 650]

    screen.fill((0, 0, 90))

    pygame.draw.rect(screen, (10, 55, 200), player)

    for enemy in enemies:
        pygame.draw.rect(screen, (0, 255, 0), enemy)


    pygame.display.flip()

pygame.quit()