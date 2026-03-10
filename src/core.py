import pygame


class Core:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def display(self):
        self.screen.fill((255, 255, 255))
