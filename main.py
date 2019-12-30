import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 32

PLAYER_SPEED = 4
JUMP_SPEED = 12
SPRITE_SCALE = BLOCK_SIZE / 256 # All textures are 256 x 256
GRAVITY = 1

def asset_path(name):
    return os.getcwd() + '/assets/' + name

class SunshineSuperman(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BABY_BLUE_EYES)

        # Set up sprite lists
        self.block_list = None
        self.player_list = None

        # Set up player values
        self.player_sprite = None
        self.phyics_engine = None
        self.view_left = 0
        self.view_bottom = 0

    def setup(self):
        self.block_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        
        char_to_path = {'g': 'grass.tif', 'd': 'dirt.tif', 's': 'stone.tif', 'c': 'cloud.tif'}
        with open(asset_path('practice.txt')) as level:
            for y, line in enumerate(level):
                for x, c in enumerate(line):
                    if c == '\n' or c == ' ': continue
                    block = arcade.Sprite(asset_path(char_to_path[c]), SPRITE_SCALE)
                    block.bottom = SCREEN_HEIGHT - ((y + 1) * BLOCK_SIZE) # Add one to y since looking at block bottom
                    block.left = x * BLOCK_SIZE
                    self.block_list.append(block)
                    
        # Set up player
        self.player_sprite = arcade.Sprite(asset_path('stone.tif'), SPRITE_SCALE / 2)
        self.player_list.append(self.player_sprite)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = SCREEN_HEIGHT + BLOCK_SIZE

        # Set up physics engine
        self.phyics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.block_list, gravity_constant=GRAVITY)

    def on_draw(self):
        arcade.start_render()
        # Render environment objects: blocks, players, etc.
        self.player_list.draw()
        self.block_list.draw()

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
    game = SunshineSuperman(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()