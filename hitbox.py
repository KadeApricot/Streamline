import component as component

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import entity as entity

class Hitbox(component.Component):
    def __init__(self, shapes : list[object]):
        self.shapes = shapes
    
    def set_entity(self, entity : entity.Entity):
        for shape in self.shapes:
            shape.entity = entity