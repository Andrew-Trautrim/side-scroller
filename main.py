import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 32

PLAYER_SPEED = 8
JUMP_SPEED = 16
SPRITE_SCALE = 0.125
GRAVITY = 1

grass = dirt = stone = smoke = None

class SunshineSuperman(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BABY_BLUE_EYES)

        # set up sprite lists
        self.wall_list = None
        self.player_list = None

        # set up player values
        self.player_sprite = None
        self.phyics_engine = None
        self.view_left = 0
        self.view_bottom = 0

    def setup(self):

        # block rendering
        """global grass, dirt, stone, smoke
        filename = os.getcwd() + '/assets/grass.tif'
        grass = arcade.load_texture(filename, scale=1)
        filename = os.getcwd() + '/assets/dirt.tif'
        dirt = arcade.load_texture(filename, scale=1)
        filename = os.getcwd() + '/assets/stone.tif'
        stone = arcade.load_texture(filename, scale=1)
        filename = os.getcwd() + '/assets/smoke.tif'
        smoke = arcade.load_texture(filename, scale=1)"""

        self.wall_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # draw blocks on the bottom
        for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
            filename = os.getcwd() + '/side-scroller/assets/grass.tif'
            wall = arcade.Sprite(filename, SPRITE_SCALE)

            wall.bottom = 0
            wall.left = x
            self.wall_list.append(wall)

        # platform
        for x in range(BLOCK_SIZE * 3, BLOCK_SIZE * 8, BLOCK_SIZE):
            filename = os.getcwd() + '/side-scroller/assets/smoke.tif'
            wall = arcade.Sprite(filename, SPRITE_SCALE)

            wall.bottom = BLOCK_SIZE * 3
            wall.left = x
            self.wall_list.append(wall)

        # set up player
        filename = os.getcwd() + '/side-scroller/assets/stone.tif'
        self.player_sprite = arcade.Sprite(filename, SPRITE_SCALE)
        self.player_list.append(self.player_sprite)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 256

        # set up physics engine
        self.phyics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, gravity_constant=GRAVITY)

    def on_draw(self):
        arcade.start_render()

        # render environment objects: blocks, players, etc.
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
    game = SunshineSuperman(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()