import component as component

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import entity as entity

class Hitbox(component.Component):
    def __init__(self, shapes : list[object], objects : list[object]):
        self.shapes = shapes
        self.objects = objects
        for shape in self.shapes:
            shape.objects = objects
    
    def set_entity(self, entity : entity.Entity):
        for shape in self.shapes:
            shape.entity = entity
    
    def tick(self, delta : float):
        for shape in self.shapes:
            shape.tick(delta)