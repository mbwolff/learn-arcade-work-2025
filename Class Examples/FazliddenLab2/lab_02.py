import arcade
from functions import draw_two, draw_four

# Constants
SCREEN_TITLE = "Python Image"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


def draw_pic():
    r_w = 100
    r_h = 100
    fourth_floor = 4
    third_floor = 3.03
    second_floor = 1.97
    first_floor = 1

    # 2
    draw_two(r_w, r_h, fourth_floor, True, (arcade.color.SKY_BLUE), (arcade.color.SKY_BLUE))
    draw_four(r_w, r_h, third_floor, True, (arcade.color.SKY_BLUE), (arcade.color.SKY_BLUE), (arcade.color.SKY_BLUE),
              (arcade.color.YELLOW))
    draw_four(r_w, r_h, second_floor, False, (arcade.color.SKY_BLUE), (arcade.color.YELLOW), (arcade.color.YELLOW),
              (arcade.color.YELLOW))
    draw_two(r_w, r_h, first_floor, False, (arcade.color.YELLOW), (arcade.color.YELLOW))

    # HEAD
    arcade.draw_ellipse_filled((SCREEN_WIDTH / 2) - r_w, r_h * 4 + 10, 100, 100, arcade.color.SKY_BLUE)
    arcade.draw_ellipse_filled((SCREEN_WIDTH / 2) + r_w, r_h * 1 - 10, 100, 100, arcade.color.YELLOW)

    # EYES
    arcade.draw_ellipse_filled((SCREEN_WIDTH / 2) - r_w, r_h * 4 + 10, 30, 30, arcade.color.GRAY)
    arcade.draw_ellipse_filled((SCREEN_WIDTH / 2) + r_w, r_h * 1 - 10, 30, 30, arcade.color.GRAY)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.GRAY)

    arcade.start_render()

    draw_pic()

    arcade.finish_render()

    arcade.run()


if __name__ == "__main__":
    main()
