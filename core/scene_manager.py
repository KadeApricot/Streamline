import core.scene as scene

class SceneManager:
    def __init__(self, scenes : dict[str, scene.Scene] = {}, current_scene : str = None):
        self.scenes = scenes
        self.current_scene = current_scene
    
    def add_scene(self, scene):
        self.scenes.append(scene)
    
    def tick(self, delta : float):
        if self.current_scene != None:
            self.scenes[self.current_scene].tick(delta)