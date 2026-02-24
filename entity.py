class Entity:
    def __init__(self, name : str = 'test_entity', components : dict[str, object] = {}):
        self.components = components
    
    def add_component(self, component):
        name = type(component).__name__
        self.components[name] = component
        setattr(self, name, component)
    
    def has_component(self, cls):
        if cls.__name__ in self.components:
            return True
        return False
    
    def remove_component(self, cls):
        name = cls.__name__
        if name in self.components:
            self.components.pop(name)
            delattr(self, name)
    
    def tick(self, delta : float):
        for component in self.components.values():
            component.tick(delta)