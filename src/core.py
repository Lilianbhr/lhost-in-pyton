import pygame


class Core:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.inputs = set()

    def add_input(self, new_input: str):
        self.inputs.add(new_input)

    def rm_input(self, old_input: str):
        self.inputs.remove(old_input)

    def display(self):
        self.screen.fill((255, 255, 255))
