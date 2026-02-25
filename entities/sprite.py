import pygame as pg

import entities.component as component
import entities.transform as transform

class Sprite(component.Component):
    def __init__(self, surf : pg.Surface, screen : pg.Surface):
        super().__init__()
        self.surf = surf
        self.screen = screen
    
    def tick(self, delta : float):
        if transform_comp := self.entity.get_component(transform.Transform):
            self.screen.blit(self.surf, transform_comp.position)