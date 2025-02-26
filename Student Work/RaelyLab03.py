import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# sand function
def sand():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.SAND)

# fish function
def fish(x, y):

    # fish body
    arcade.draw_ellipse_filled(200 + x, 370+ y, 135, 80, arcade.csscolor.DARK_BLUE)

    # fish tail
    arcade.draw_triangle_filled(250 + x, 350 + y, 300, 400, 300, 300, arcade.csscolor.DARK_BLUE)

    # fish eye
    arcade.draw_circle_filled(160 + x, 370 + y, 8, arcade.csscolor.BLACK)

    # reference point
    arcade.draw_point(400, 300, arcade.color.RED, 5)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "im so confused")

    # ocean background
    arcade.set_background_color(arcade.color.POWDER_BLUE)
    arcade.start_render()

    sand()
    fish(50, 50)
    fish(80, 200)
    fish (200, 200)
    fish (500, 100)
    arcade.finish_render()
    arcade.run()

main()
