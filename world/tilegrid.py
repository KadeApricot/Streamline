class TileGrid:
    def __init__(self):
        pass

    def generate_level(self, width, height):
        self.level = [[0 for _ in range(width)] for _ in range(height)]
        print(self.level)


tile_grid = TileGrid()
tile_grid.generate_level(4, 7)
