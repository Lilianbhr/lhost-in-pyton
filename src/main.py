import pygame
from core import Core
pygame.init()

# Window
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Lhost in Pyton")

# Core loop
mode = Core(screen)
clock = pygame.time.Clock()
running = True

while running:

    mode.update()
    mode.display()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            mode.add_input(key)

            if key == "space":
                mode.change_mode()

        elif event.type == pygame.KEYUP:
            key = pygame.key.name(event.key)
            mode.rm_input(key)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
