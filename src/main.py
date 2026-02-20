import pygame
pygame.init()

# Window
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Lhost in Pyton")
bg_color = (255, 255, 255)

# Core loop
clock = pygame.time.Clock()
running = True

while running:

    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)
