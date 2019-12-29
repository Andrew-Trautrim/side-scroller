import arcade
import os

SCREEN_WIDTH = 1684
SCREEN_HEIGHT = 920
BLOCK_SIZE = 64
PLAYER_SPEED = 5
grass = dirt = stone = smoke = None

class Player():
    def __init__(self, position_x, position_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = 0
        self.change_y = 0
        self.color = color
    
    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, 32, self.color)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

class SunshineSuperman(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BABY_BLUE_EYES)
        self.player = Player(64, 64, arcade.color.WHITE)

    def setup(self):
        global grass, dirt, stone, smoke
        filename = os.getcwd() + '/assets/grass.tif'
        grass = arcade.load_texture(filename, scale=1)
        filename = os.getcwd() + '/assets/dirt.tif'
        dirt = arcade.load_texture(filename, scale=1)
        filename = os.getcwd() + '/assets/stone.tif'
        stone = arcade.load_texture(filename, scale=1)
        filename = os.getcwd() + '/assets/smoke.tif'
        smoke = arcade.load_texture(filename, scale=1)

    def on_draw(self):
        arcade.start_render()
        for x in range(0, 10):
            for y in range(0, 3):
                arcade.draw_texture_rectangle(100 + (x * BLOCK_SIZE), 0 + (y * BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE, smoke)
                arcade.draw_texture_rectangle(100 + (x * BLOCK_SIZE), 200 + (y * BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE, grass)
                arcade.draw_texture_rectangle(100 + (x * BLOCK_SIZE), 400 + (y * BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE, dirt)
                arcade.draw_texture_rectangle(100 + (x * BLOCK_SIZE), 600 + (y * BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE, stone)
        self.player.draw()

    def update(self, delta_time):
        self.player.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

def main():
    game = SunshineSuperman(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()