import component as component
from pygame.math import Vector2

class Transform(component.Component):
    def __init__(self, position : Vector2):
        super().__init__()
        self.position = position