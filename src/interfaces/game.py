import pygame
from src.interfaces.interface import Interface
from src.mapManager import MapManager
from src.sprite import Player


class Game(Interface):
    """
    Le gestionnaire de jeu, il contient la map, le joueur etc...
    """
    def __init__(self, screen_size: tuple):
        super().__init__()
        self.nom = "game"
        self.screen_size = screen_size

        # Map + Joueur
        self.map_manager = MapManager(self.screen_size)
        self.player = Player()

        # Ajout du joueur aux éléments visibles par l'utilisateur
        self.player.precise_pos = self.map_manager.get_spawn_point()
        self.map_manager.group.add(self.player)
        self.map_manager.focus(self.player.rect.center)

    def update(self, inputs: set):
        self.player.update(inputs, self.map_manager.get_map_size())
        self.map_manager.focus(self.player.rect.center)

    def display(self, surface: pygame.Surface):
        self.map_manager.display(surface)
