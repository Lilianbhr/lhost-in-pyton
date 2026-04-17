import pygame


class Player(pygame.sprite.Sprite):
    """ Première version d'un personnage contrôlable par le joueur """
    def __init__(self):
        super().__init__()

        # Visuel + collisions
        self.image = pygame.Surface((10, 12))
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

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)

    def collision(self, walls: list, movement: pygame.Vector2, axis: str):
        for wall in walls:
            if self.rect.colliderect(wall):

                if axis == "x":
                    if movement.x < 0:
                        self.rect.x = wall.right
                    elif movement.x > 0:
                        self.rect.right = wall.x

                elif axis == "y":
                    if movement.y < 0:
                        self.rect.y = wall.bottom
                    elif movement.y > 0:
                        self.rect.bottom = wall.y

    def update(self, active_inputs: set, screen_size: tuple, walls: list):
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

        # déplacement précis (séparation x/y pour les collisions)
        self.rect.x += final_direction.x * self.speed
        self.collision(walls, final_direction, "x")

        self.rect.y += final_direction.y * self.speed
        self.collision(walls, final_direction, "y")

        # empêcher le joueur de sortir de la carte
        # gauche
        if self.rect.x < 0:
            self.rect.x = 0

        # droite
        elif self.rect.right > screen_size[0]:
            self.rect.right = screen_size[0]

        # haut
        if self.rect.y < 0:
            self.rect.y = 0

        # bas
        elif self.rect.bottom > screen_size[1]:
            self.rect.bottom = screen_size[1]
