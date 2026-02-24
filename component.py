from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import entity as entity

class Component:
    def __init__(self):
        self.entity : entity.Entity = None

    def tick(self, delta : float):
        raise NotImplementedError()