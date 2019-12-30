import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 32

PLAYER_SPEED = 8
JUMP_SPEED = 16
SPRITE_SCALE = 0.125
GRAVITY = 1

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

        # Set up sprite lists
        self.wall_list = None
        self.player_list = None

        # Set up player values
        self.player_sprite = None
        self.phyics_engine = None
        self.view_left = 0
        self.view_bottom = 0

    def setup(self):
        global GRASS, DIRT, STONE, CLOUD
        GRASS = arcade.load_texture(asset_path('grass.tif'))
        DIRT  = arcade.load_texture(asset_path('dirt.tif'))
        STONE = arcade.load_texture(asset_path('stone.tif'))
        CLOUD = arcade.load_texture(asset_path('cloud.tif'))

        self.wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # Draw blocks on the bottom
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            wall = arcade.Sprite(asset_path('grass.tif'), SPRITE_SCALE)
            wall.bottom = 0
            wall.left = x
            self.wall_list.append(wall)

        # Platform
        for x in range(BLOCK_SIZE * 3, BLOCK_SIZE * 8, BLOCK_SIZE):
            wall = arcade.Sprite(asset_path('cloud.tif'), SPRITE_SCALE)
            wall.bottom = BLOCK_SIZE * 3
            wall.left = x
            self.wall_list.append(wall)

        # Set up player
        self.player_sprite = arcade.Sprite(asset_path('stone.tif'), SPRITE_SCALE)
        self.player_list.append(self.player_sprite)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 256

        # Set up physics engine
        self.phyics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, gravity_constant=GRAVITY)

    def on_draw(self):
        global CURRENT_LEVEL

        arcade.start_render()
        CURRENT_LEVEL.draw()

        # Render environment objects: blocks, players, etc.
        self.player_list.draw()
        self.wall_list.draw()

    def on_update(self, delta_time):
        self.phyics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.phyics_engine.can_jump():
            self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    global CURRENT_LEVEL

    game = SunshineSuperman(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    CURRENT_LEVEL.setup()
    arcade.run()

if __name__ == "__main__":
    main()