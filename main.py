import pygame as pg
import scene_manager as scene_manager
import scene as scene
import entity as entity

class Main:
    def __init__(self):
        self.screen = pg.display.set_mode((640, 640))
        self.clock = pg.time.Clock()
        self.running = True

        self.scene_manager = scene_manager.SceneManager()

    def get_main_scene(self):
        main_scene = scene.Scene([])

        grid = entity.Entity(name = 'grid')
        self.add_entity(grid)
    
    def add_entity(self, entity):
        if self.scene_manager.current_scene:
            self.scene_manager.scenes[self.scene_manager.current_scene].add_entity(entity)
        setattr(self, entity.name, entity)
    
    def del_entity(self, name):
        if self.scene_manager.current_scene:
            self.scene_manager.scenes[self.scene_manager.current_scene].del_entity(name)
        delattr(self, name)

    def tick(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.running = False

if __name__ == '__main__':
    main = Main()
    
    while main.running:
        main.tick()