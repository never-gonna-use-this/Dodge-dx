import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Color Pick DX")

# colors
BLACK = (20, 20, 41)
red = 0
green = 0
blue = 0
gray = (55, 55, 55)
gray2 = (33, 33, 33)
light_gray = (150, 150, 150)

# sliders
slider = pygame.Rect(270, 550, 301, 25)
handle = pygame.Rect(270, 535, 45, 50)
slider2 = pygame.Rect(270, 450, 301, 25)
handle2 = pygame.Rect(270, 435, 45, 50)
slider3 = pygame.Rect(270, 350, 301, 25)
handle3 = pygame.Rect(270, 335, 45, 50)


slider_min = slider.x + 1
slider_max = slider.x + slider.width - 1


clock = pygame.time.Clock()
run = True
while run:

    clock.tick(100)
    mouse_held = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        screen.fill(BLACK)
        pygame.draw.rect(screen, (red, green, blue), (50, 50, 700, 150))
        pygame.draw.rect(screen, gray2, (0, 250, 800, 500))
        pygame.draw.rect(screen, gray, slider)
        pygame.draw.rect(screen, light_gray, handle)
        pygame.draw.rect(screen, gray, slider2)
        pygame.draw.rect(screen, gray, slider3)
        pygame.draw.rect(screen, light_gray, handle3)
        pygame.draw.rect(screen, light_gray, handle2)

    # blue
    if mouse_held[0]:
        if mouse_x in range(handle.x, handle.x + handle.width) and mouse_y in range(handle.y, handle.y + handle.height):
            handle.x = mouse_x - handle.width / 5

    if handle.x < slider_min:
        handle.x = slider_min + 1
    if handle.x + handle.width > slider_max:
        handle.x = slider_max - handle.width

    # green
    if mouse_held[0]:
        if mouse_x in range(handle2.x, handle2.x + handle2.width) and mouse_y in range(handle2.y, handle2.y + handle2.height):
            handle2.x = mouse_x - handle2.width / 5

    if handle2.x < slider_min:
        handle2.x = slider_min + 1
    if handle2.x + handle.width > slider_max:
        handle2.x = slider_max - handle2.width

    # red
    if mouse_held[0]:
        if mouse_x in range(handle3.x, handle3.x + handle3.width) and mouse_y in range(handle3.y, handle3.y + handle3.height):
            handle3.x = mouse_x - handle3.width / 5

    if handle3.x < slider_min:
        handle3.x = slider_min + 1
    if handle3.x + handle.width > slider_max:
        handle3.x = slider_max - handle3.width

    if handle.x - 270:
        blue = handle.x - 270

    if handle2.x - 270:
        green = handle2.x - 270

    if handle3.x - 270:
        red = handle3.x - 270

    pygame.display.flip()

pygame.quit()