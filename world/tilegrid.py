class TileGrid:
    def __init__(self):
        self.level = None
        self.width = None
        self.height = None

    def generate_level(self, width, height):
        self.width = width
        self.height = height
        self.level = [[(1 if w * h == 0 or w == self.width - 1 or h == self.height - 1 else 0) for w in range(self.width)] for h in range(self.height)]
        print(self.level)

    def display_level(self):
        for i in range(self.width):
            pass



tile_grid = TileGrid()
tile_grid.generate_level(4, 7)