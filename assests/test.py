import pygame
from pygame import K_a, K_d

pygame.init()
screen = pygame.display.set_mode((800, 600))
cringe = pygame.transform.scale(pygame.image.load("cringe_paper_clip.png"), (65, 100))
magnets = pygame.image.load("magnets.png")
magnets2 = pygame.image.load("magnets2.png")
x = 365

run =True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill("light blue")
    screen.blit(cringe, (x, 400))
    screen.blit(magnets, (-100, -50))
    screen.blit(magnets2, (450, -45))


    keys = pygame.key.get_pressed()
    if keys[K_a]:
        x -= 5

    if keys[K_d]:
        x += 5




    pygame.display.flip()


pygame.quit()