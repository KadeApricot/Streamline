import pygame as pg

class Main:
    def __init__(self):
        self.screen = pg.display.set_mode((640, 640))
        self.clock = pg.time.Clock()
        self.running = True

        self.scene
    
    def update(self):
        while self.running:


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    self.running = False

if __name__ == '__main__':
    main = Main()
    main.run()