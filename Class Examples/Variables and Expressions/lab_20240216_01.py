import arcade

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

arcade.draw_circle_filled(400, 300, 50, arcade.color.FOREST_GREEN)

arcade.finish_render()
arcade.run()