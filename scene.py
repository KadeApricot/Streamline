import entity as entity

class Scene:
    def __init__(self, entities : dict[str, entity.Entity]):
        self.entities = entities
    
    def add_entity(self, entity):
        self.entities[entity.name] = entity
        setattr(self, entity.name, entity)
    
    def del_entity(self, name : str):
        self.entities.pop(name)
        delattr(self, name)
    
    def tick(self, delta : float):
        for entity in self.entities:
            entity.tick(delta)