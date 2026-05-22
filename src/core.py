import pygame
from interfaces.game import Game
from interfaces.menu import Menu


class Core:
    """
    Le noyaux du jeu, c'est lui qui gère les changements
    de modes et les touches
    """
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.inputs = set()
        self.current_mode = Menu()

    def add_input(self, new_input: str):
        self.inputs.add(new_input)

    def rm_input(self, old_input: str):
        self.inputs.remove(old_input)

    def change_mode(self):
        if self.current_mode.nom == "menu":
            self.current_mode = Game(self.screen.get_size())
        elif self.current_mode.nom == "game":
            self.current_mode = Menu()

    def update(self):
        if self.current_mode.nom == "game":
            self.current_mode.update(self.inputs)

    def display(self):
        self.screen.fill((255, 255, 255))
        self.current_mode.display(self.screen)
