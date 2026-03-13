import pygame
from src.interfaces.interface import Interface
from src.mapManager import MapManager


class Game(Interface):
    def __init__(self, screen_size: tuple):
        super().__init__()
        self.nom = "game"
        self.screen_size = screen_size
        self.font = pygame.font.SysFont("Arial", 24)
        self.screen_text = self.font.render(self.nom, True, (0, 0, 0))
        self.map_manager = MapManager(self.screen_size)

    def display(self, surface: pygame.Surface):
        surface.blit(self.screen_text, (0, 0))
        self.map_manager.display(surface)
