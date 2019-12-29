import arcade
import os

SCREEN_WIDTH = 1084
SCREEN_HEIGHT = 720
test = None

class SunshineSuperman(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BABY_BLUE_EYES)

    def setup(self):
        global test
        filename = os.getcwd() + '/assets/grass.tif'
        test = arcade.load_texture(filename, scale=1)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(400, 400, 256, 256, test)

    def update(self, delta_time):
        pass

def main():
    game = SunshineSuperman(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()