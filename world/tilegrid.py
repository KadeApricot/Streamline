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
        for i in range(self.height):
            for j in range(self.width):
                print(self.level[i][j], end=" ")
            print()



tile_grid = TileGrid()
tile_grid.generate_level(50, 20)
tile_grid.display_level()