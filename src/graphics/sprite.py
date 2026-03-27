import pygame


class Player(pygame.sprite.Sprite):
    """ Première version d'un personnage ocntrollable par le joueur """
    def __init__(self):
        super().__init__()

        # Visuel + collisions
        self.image = pygame.Surface((32, 64))
        self.image.fill((255, 255, 0))
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

    def set_rect_pos(self):
        self.rect.topleft = (round(self.precise_pos[0]),
                             round(self.precise_pos[1]))

    def collision(self, walls: list, movement: pygame.Vector2, axis: str):
        for wall in walls:
            if self.rect.colliderect(wall):

                if axis == "x":
                    if movement.x < 0:
                        self.precise_pos[0] = wall.right
                    elif movement.x > 0:
                        self.precise_pos[0] = wall.x - self.rect.w

                elif axis == "y":
                    if movement.y < 0:
                        self.precise_pos[1] = wall.bottom
                    elif movement.y > 0:
                        self.precise_pos[1] = wall.y - self.rect.h

            self.set_rect_pos()

    def update(self, active_inputs: set, screen_size: tuple, walls: list):
        """
        le mouvement est basé sur une somme de vecteurs,
        cela permet une gestion efficace de déplacements multidirectionnels
        notamment sur les diagonales
        """
        final_direction = pygame.math.Vector2(0, 0)
        old_pos = self.precise_pos

        # Récupération des forces actives
        for key in self.directions.keys():
            if key in active_inputs:
                final_direction.x += self.directions[key].x
                final_direction.y += self.directions[key].y

        # Normalisation
        if final_direction.xy != (0, 0):
            final_direction = final_direction.normalize()

        # déplacement précis (séparation x/y pour les collisions)
        self.precise_pos[0] += final_direction.x * self.speed
        self.collision(walls, final_direction, "x")

        self.precise_pos[1] += final_direction.y * self.speed
        self.collision(walls, final_direction, "y")

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

        self.set_rect_pos()
