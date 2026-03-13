import pygame
from src.interfaces.interface import Interface
from src.mapManager import MapManager
from src.sprite import Player


class Game(Interface):
    def __init__(self, screen_size: tuple):
        super().__init__()
        self.nom = "game"
        self.screen_size = screen_size
        self.font = pygame.font.SysFont("Arial", 24)
        self.screen_text = self.font.render(self.nom, True, (0, 0, 0))

        self.map_manager = MapManager(self.screen_size)
        self.player = Player()

        self.player.precise_pos = self.map_manager.get_spawn_point()
        self.map_manager.group.add(self.player)
        self.map_manager.focus(self.player.rect.center)

    def update(self, inputs: set):
        self.player.update(inputs, self.map_manager.get_map_size())
        self.map_manager.focus(self.player.rect.center)

    def display(self, surface: pygame.Surface):
        surface.blit(self.screen_text, (0, 0))
        self.map_manager.display(surface)
