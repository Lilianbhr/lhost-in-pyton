import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill((0, 0, 255))

        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

        self.speed = 5

    def update(self, active_inputs: set):
        if "z" in active_inputs:
            self.rect.y -= self.speed
        if "s" in active_inputs:
            self.rect.y += self.speed
        if "q" in active_inputs:
            self.rect.x -= self.speed
        if "d" in active_inputs:
            self.rect.x += self.speed
