import pygame


class Interface:
    def __init__(self):
        pass

    def update(self, inputs: set):
        raise NotImplementedError(
            "Cette méthode doit être implémentée dans la classe fille."
        )

    def display(self, surface: pygame.Surface):
        raise NotImplementedError(
            "Cette méthode doit être implémentée dans la classe fille."
        )
