from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    import entities.entity as entity

ComponentT = TypeVar("ComponentT", bound = "Component")

class Component:
    def __init__(self):
        self.entity : entity.Entity = None

    def set_entity(self, entity : entity.Entity):
        for shape in self.shapes:
            shape.entity = entity

    def tick(self, delta : float):
        raise NotImplementedError()