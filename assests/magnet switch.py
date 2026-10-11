import pygame
from pygame import K_a, K_d, KEYDOWN, K_s

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Magnet Switch")
bedroom = pygame.transform.scale(pygame.image.load("b-vector bedroom.png"), (810, 1000))
paper = pygame.transform.scale(pygame.image.load("paper_clip.png"), (350, 500))
magnets = pygame.image.load("magnets.png")
magnets2 = pygame.image.load("magnets2.png")

x = 266
y = 250
yb = -400

magnet_on = True
gravity = 0.5
velocity_y = 0
velocity_x = 0

left_magnets_x = 40
left_magnets_y = 200
right_magnets_x = 700
right_magnets_y = 200
magnets_strength = 3000

run =True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_s:
                magnet_on = not magnet_on

    screen.fill("light blue")
    screen.blit(bedroom, (-5, yb))
    screen.blit(paper, (x, y))
    screen.blit(magnets, (-130, -50))
    screen.blit(magnets2, (500, -50))


    clock.tick(60)

    velocity_y += gravity

    if magnet_on:
        velocity_y = 0
    else:
        velocity_y += gravity

    x += velocity_x
    y += velocity_y

    velocity_x *= 0.9

    if magnet_on:
        distance_left = x - left_magnets_x
        if distance_left > 0:
            force_left =  100 / distance_left
            velocity_x -= force_left

        distance_right = right_magnets_x - x
        if distance_right < 0:
            force_right = 100 / distance_right
            velocity_x += force_right

    keys = pygame.key.get_pressed()
    if keys[K_a]:
        velocity_x -= 4


    if keys[K_d]:
        velocity_x += 4


    if y >= 250:
        y = 250
        velocity_y = 0


    pygame.display.flip()


pygame.quit()