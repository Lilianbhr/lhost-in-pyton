import pygame


class Player(pygame.sprite.Sprite):
    """ Première version d'un personnage ocntrollable par le joueur """
    def __init__(self):
        super().__init__()

        # Visuel + collisions
        self.image = pygame.Surface((32, 64))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()

        # Position + Déplacements
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
        """
        le mouvement est basé sur une somme de vecteurs,
        cela permet une gestion efficace de déplacements multidirectionnels
        notamment sur les diagonales
        """
        final_direction = pygame.math.Vector2(0, 0)

        # Récupération des forces actives
        for key in self.directions.keys():
            if key in active_inputs:
                final_direction.x += self.directions[key].x
                final_direction.y += self.directions[key].y

        # Normalisation
        if final_direction.xy != (0, 0):
            final_direction = final_direction.normalize()

        # déplacement précis
        self.precise_pos[0] += final_direction.x * self.speed
        self.precise_pos[1] += final_direction.y * self.speed

        # empêcher le joueur de sortir de la carte
        # gauche
        if self.precise_pos[0] < 0:
            self.precise_pos[0] = 0

        # droite
        elif self.precise_pos[0] + self.rect.width > screen_size[0]:
            self.precise_pos[0] = screen_size[0] - self.rect.width

        # haut
        if self.precise_pos[1] < 0:
            self.precise_pos[1] = 0

        # bas
        elif self.precise_pos[1] + self.rect.height > screen_size[1]:
            self.precise_pos[1] = screen_size[1] - self.rect.height

        # convertion en coordonnées entières
        self.rect.topleft = (round(self.precise_pos[0]),
                             round(self.precise_pos[1]))
