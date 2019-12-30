import arcade
import os

SCREEN_WIDTH = 1684
SCREEN_HEIGHT = 920
BLOCK_SIZE = 64
GRASS = DIRT = STONE = CLOUD = None

def asset_path(name):
    return os.getcwd() + '/assets/' + name

class Level():
    # Note: Game setup must be run before any instances of Level are created
    char_to_texture = None
    grid = []

    def __init__(self):
        pass

    def setup(self):
        global GRASS, DIRT, STONE, CLOUD # Assumption: These have been initialized to textures
        self.char_to_texture = {' ': None, 'g': GRASS, 'd': DIRT, 's': STONE, 'c': CLOUD}
        with open(asset_path('practice.txt')) as level:
            for line in level:
                self.grid.append([])
                for c in line:
                    if c == '\n': continue
                    self.grid[-1].append(self.char_to_texture[c])
        # Take the transpose of the grid due to the array initalization order causing the values to be read in the wrong order
        self.grid = [*zip(*self.grid)]

    def draw(self):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y]:
                    offset = BLOCK_SIZE / 2
                    arcade.draw_texture_rectangle(
                        offset + (x * BLOCK_SIZE),
                        SCREEN_HEIGHT - offset - (y * BLOCK_SIZE),
                        BLOCK_SIZE,
                        BLOCK_SIZE,
                        self.grid[x][y])
                    
CURRENT_LEVEL = Level()

class SunshineSuperman(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BABY_BLUE_EYES)

    def setup(self):
        global GRASS, DIRT, STONE, CLOUD
        GRASS = arcade.load_texture(asset_path('grass.tif'))
        DIRT  = arcade.load_texture(asset_path('dirt.tif'))
        STONE = arcade.load_texture(asset_path('stone.tif'))
        CLOUD = arcade.load_texture(asset_path('cloud.tif'))

    def on_draw(self):
        global CURRENT_LEVEL

        arcade.start_render()
        for x in range(0, 10):
            for y in range(0, 3):
                """arcade.draw_texture_rectangle(100 + (x * BLOCK_SIZE), 0 + (y * BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE, CLOUD)
                arcade.draw_texture_rectangle(100 + (x * BLOCK_SIZE), 200 + (y * BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE, GRASS)
                arcade.draw_texture_rectangle(100 + (x * BLOCK_SIZE), 400 + (y * BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE, DIRT)
                arcade.draw_texture_rectangle(100 + (x * BLOCK_SIZE), 600 + (y * BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE, STONE)"""
        
        CURRENT_LEVEL.draw()

    def update(self, delta_time):
        pass

def main():
    global CURRENT_LEVEL

    game = SunshineSuperman(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    CURRENT_LEVEL.setup()
    arcade.run()

if __name__ == "__main__":
    main()