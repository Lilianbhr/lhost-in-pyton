from pytmx.util_pygame import load_pygame
import pyscroll
import pygame


class MapManager:
    def __init__(self, screen_size: tuple):
        self.map_dir = "../assets/map/maps_tmx/"
        self.screen_size = screen_size

        self.tmx_data = None
        self.zoom = 1.3
        self.group = self.set_map("map_1")

        self.portals = []
        self.walls = []
        self.set_objects()

    def set_map(self, map_name: str) -> pyscroll.PyscrollGroup:
        """ Permet de charger une map """
        self.tmx_data = load_pygame(self.map_dir + map_name + ".tmx")
        map_layer = pyscroll.BufferedRenderer(
            data=pyscroll.TiledMapData(self.tmx_data),
            size=self.screen_size,
            zoom=self.zoom
        )
        group = pyscroll.PyscrollGroup(map_layer)
        return group

    def set_objects(self):
        self.portals = []
        self.walls = []

        for obj in self.tmx_data.objects:

            # Portals
            if obj.type == "portal":
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                self.portals.append((rect, obj.name))

            # Walls
            elif obj.type == "wall":
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                self.walls.append(rect)

    def get_spawn_point(self):
        for obj in self.tmx_data.objects:
            if obj.name == "spawn_point":
                return [obj.x, obj.y]
        return 0, 0

    def get_map_size(self):
        tile_size = self.tmx_data.tilewidth
        width = self.tmx_data.width
        height = self.tmx_data.height
        return width * tile_size, height * tile_size

    def change_map(self, map_name: str):
        self.group = self.set_map(map_name)
        self.set_objects()

    def focus(self, point: tuple):
        self.group.center(point)

    def display(self, surface: pygame.Surface):
        self.group.draw(surface)
