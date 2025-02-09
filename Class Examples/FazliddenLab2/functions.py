import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


def draw_two(r_w, r_h, value, top, color_1, color_2):
    if top == True:
        move = r_h * value + 10

        # BLOCK ONE
        arcade.draw_rectangle_filled((SCREEN_WIDTH / 2) - (r_w / 2), move, r_w, r_h, color_1)

        # BLOCK TWO
        arcade.draw_rectangle_filled((SCREEN_WIDTH / 2) + (r_w / 2), r_h * value, r_w, r_h + 20, color_2)

    else:
        move = r_h * value - 10

        # BLOCK ONE
        arcade.draw_rectangle_filled((SCREEN_WIDTH / 2) - (r_w / 2), r_h * value, r_w, r_h + 20, color_1)

        # BLOCK TWO
        arcade.draw_rectangle_filled((SCREEN_WIDTH / 2) + (r_w / 2), move, r_w, r_h, color_2)


def draw_four(r_w, r_h, value, top, color_1, color_2, color_3, color_4):
    # arcade.draw_rectangle_filled(left, bottom, width, height, color)
    white = arcade.color.WHITE

    # BLOCK ONE
    if top:
        arcade.draw_rectangle_filled((((SCREEN_WIDTH / 2) - r_w * 2) + r_w / 2) - 5, (r_h * value) - 8, r_w, r_h + 16,
                                     color_1)
    else:
        arcade.draw_rectangle_filled((((SCREEN_WIDTH / 2) - r_w * 2) + r_w / 2) - 5, r_h * value, r_w, r_h, color_1)

    # BLOCK TWO
    if top:
        arcade.draw_rectangle_filled((SCREEN_WIDTH / 2) + (r_w / 2), r_h * value, r_w, r_h, color_2)
    else:
        arcade.draw_rectangle_filled((SCREEN_WIDTH / 2) + (r_w / 2), r_h * value, r_w + 10, r_h, color_2)

    # BLOCK THREE
    if top == False:
        arcade.draw_rectangle_filled((SCREEN_WIDTH / 2) - (r_w / 2), r_h * value, r_w, r_h, color_3)
    else:
        arcade.draw_rectangle_filled((SCREEN_WIDTH / 2) - (r_w / 2), r_h * value, r_w + 10, r_h, color_3)

    # BLOCK FOUR
    if top == False:
        arcade.draw_rectangle_filled((((SCREEN_WIDTH / 2) + r_w * 2) - r_w / 2) + 5, r_h * value + 8, r_w, r_h + 16,
                                     color_4)
    else:
        arcade.draw_rectangle_filled((((SCREEN_WIDTH / 2) + r_w * 2) - r_w / 2) + 5, r_h * value, r_w, r_h, color_4)
