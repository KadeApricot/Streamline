import entities.component as component
from pygame.math import Vector2

class Transform(component.Component):
    def __init__(self, position : Vector2):
        self.position = position