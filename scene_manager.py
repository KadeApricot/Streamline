class SceneManager:
    def __init__(self, scenes : dict[str, object], current_scene : str):
        self.scenes = scenes
        self.current_scene = current_scene
    
    def add_scene(self, scene):
        self.scenes.append(scene)
    
    def tick(self, delta : float):
        self.scenes[self.current_scene].tick(delta)