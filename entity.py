from typing import Union

class Entity:
    def __init__(self, name : str = 'test_entity', tags : set[str] = {}, components : dict[str, object] = {}):
        self.name = name
        self.tags = tags
        self.components = components
    
    def add_component(self, component):
        name = type(component).__name__
        self.components[name] = component
        setattr(self, name, component)

    def get_component(self, cls : Union[type, str]):
        if self.has_component(cls):
            return self.components[cls.__name__ if isinstance(cls, type) else cls]
        return None
    
    def remove_component(self, cls : Union[type, str]):
        name = cls.__name__ if isinstance(cls, type) else cls
        if name in self.components:
            self.components.pop(name)
            delattr(self, name)
    
    def tick(self, delta : float):
        for component in self.components.values():
            component.tick(delta)