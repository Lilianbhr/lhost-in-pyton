import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill((0, 0, 255))

        self.rect = self.image.get_rect()

        self.directions = {
            "z": pygame.math.Vector2(0, -1),
            "s": pygame.math.Vector2(0, 1),
            "q": pygame.math.Vector2(-1, 0),
            "d": pygame.math.Vector2(1, 0)
        }
        self.speed = 5
        self.precise_pos = [0, 0]

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)

    def update(self, active_inputs: set, screen_size: tuple):
        final_direction = pygame.math.Vector2(0, 0)

        for key in self.directions.keys():
            if key in active_inputs:
                final_direction.x += self.directions[key].x
                final_direction.y += self.directions[key].y

        if final_direction.xy != (0, 0):
            final_direction = final_direction.normalize()

        self.precise_pos[0] += final_direction.x * self.speed
        self.precise_pos[1] += final_direction.y * self.speed

        if self.precise_pos[0] < 0:
            self.precise_pos[0] = 0

        elif self.precise_pos[0] + self.rect.width > screen_size[0]:
            self.precise_pos[0] = screen_size[0] - self.rect.width

        if self.precise_pos[1] < 0:
            self.precise_pos[1] = 0

        elif self.precise_pos[1] + self.rect.height > screen_size[1]:
            self.precise_pos[1] = screen_size[1] - self.rect.height

        self.rect.topleft = (round(self.precise_pos[0]),
                             round(self.precise_pos[1]))
