import pygame
pygame.init()

screen = pygame.display.set_mode((1000, 1000))
image = pygame.image.load('materials/pion_blanc.png').convert()

running = True
x = 2
y = 4
pos = (200 , 200)

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        pos = (pos[0] - x, pos[1])

    if pressed[pygame.K_RIGHT]:
        pos = (pos[0] + x, pos[1])

    if pressed[pygame.K_UP]:
        pos = (pos[0], pos[1] - y)

    if pressed[pygame.K_DOWN]:
        pos = (pos[0], pos[1] + y)

    screen.fill((0, 0, 0))
    screen.blit(image, pos)
    # flip for all screen & update for special pixels
    pygame.display.flip()

pygame.quit()
