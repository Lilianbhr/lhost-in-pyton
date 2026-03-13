import pygame
from src.interfaces.interface import Interface


class Menu(Interface):
    """
    Interface de base du jeu
    """
    def __init__(self):
        super().__init__()
        self.nom = "menu"
        self.font = pygame.font.SysFont("Arial", 24)
        self.screen_text = self.font.render(self.nom, True, (0, 0, 0))

    def display(self, surface: pygame.Surface):
        surface.blit(self.screen_text, (0, 0))
