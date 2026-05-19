import pygame
from interfaces.interface import Interface
from graphics.mapManager import MapManager
from graphics.sprite import Player


class Game(Interface):
    """
    Le gestionnaire de jeu, il contient la map, le joueur etc...
    """
    def __init__(self, screen_size: tuple[int, int]):
        super().__init__()
        self.nom = "game"
        self.screen_size = screen_size

        # Map + Joueur
        self.map_manager = MapManager(self.screen_size)
        self.player = Player()

        # Ajout du joueur aux éléments visibles par l'utilisateur
        self.player.rect.topleft = self.map_manager.get_spawn_point()
        self.map_manager.group.add(self.player)
        self.map_manager.focus(self.player.rect.center)

    def update(self, inputs: set):
        self.player.update(
            inputs,
            self.map_manager.get_map_size(),
            self.map_manager.walls
        )

        # Vérification qu'un portail a été franchi
        for portal in self.map_manager.portals:
            if self.player.rect.colliderect(portal[0]):
                self.map_manager.change_map(portal[1])
                print(portal[1])
                if len(portal) == 3 :
                    self.player.rect.topleft = self.map_manager.get_spawn_point(
                        self.map_manager.map_name,
                        link=portal[2]
                    )
                else:
                    self.player.rect.topleft = self.map_manager.get_spawn_point(
                        self.map_manager.map_name
                    )
                self.map_manager.map_name = portal[1]
                self.map_manager.group.add(self.player)

        self.map_manager.focus(self.player.rect.center)

    def display(self, surface: pygame.Surface):
        self.map_manager.display(surface)
