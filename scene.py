class Scene:
    def __init__(self, entities):
        self.entities = entities
    
    def add_entity(self, entity):
        self.entities.append(entity)
    
    def tick(self, delta : float):
        for entity in self.entities:
            entity.tick(delta)