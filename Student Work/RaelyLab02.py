"""
i think this is what i have to do for arcade to work
"""

# This is how I import arcade

import arcade

arcade.open_window(600, 600, "Drawing Example")

arcade.set_background_color(arcade.csscolor.POWDER_BLUE)

# Ocean
# Water

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 599, 160, 0, arcade.csscolor.LIGHT_YELLOW)

# Ocean floor
# Sand

arcade.draw_ellipse_filled(200, 370, 135, 80, arcade.csscolor.DARK_BLUE)

# Fish body

arcade.draw_triangle_filled(250, 350, 300, 400, 300, 300, arcade.csscolor.DARK_BLUE)

# Fish tail
# Took like 5 hours to get in the correct position


arcade.draw_circle_filled(160, 370, 8, arcade.csscolor.BLACK)

# Fish eye

arcade.draw_ellipse_filled(480, 250, 80, 45, arcade.csscolor.GREY)

# Submarine body

arcade.draw_circle_filled(500, 252, 6, arcade.csscolor.CYAN)

# Submarine window 1

arcade.draw_circle_filled(480, 252, 6, arcade.csscolor.CYAN)

# Submarine window 2

arcade.draw_circle_filled(460, 252, 6, arcade.csscolor.CYAN)

# Submarine window 3

arcade.draw_rectangle_filled(490, 280, 8, 30, arcade.csscolor.GREY)

arcade.draw_circle_filled(500, 300, 6, arcade.csscolor.CYAN)

arcade.draw_rectangle_filled(490, 300, 12, 15, arcade.csscolor.GREY)

# Submarine parts

arcade.draw_line(300, 160, 340, 200, arcade.color.GREEN, 3)

arcade.draw_line(300, 250, 300, 160, arcade.color.GREEN, 3)

arcade.draw_line(310, 160, 240, 200, arcade.color.GREEN, 3)

# Sea grass

arcade.draw_rectangle_filled(450, 400, 10, 60, arcade.csscolor.DARK_GREY)

arcade.draw_rectangle_filled(450, 370, 50, 10, arcade.csscolor.DARK_GREY)

arcade.draw_rectangle_filled(450, 400, 50, 10, arcade.csscolor.DARK_GREY)

arcade.draw_circle_filled(450, 430, 18, arcade.csscolor.DARK_GREY)

arcade.draw_circle_filled(450, 430, 12, arcade.csscolor.LIGHT_BLUE)

# Diver stick-man

arcade.draw_circle_filled(96, 500, 50, arcade.csscolor.LIGHT_PINK)

arcade.draw_rectangle_filled(96, 470, 100, 60, arcade.csscolor.POWDER_BLUE)

arcade.draw_rectangle_filled(60, 470, 5, 60, arcade.csscolor.LIGHT_PINK)

arcade.draw_rectangle_filled(75, 470, 5, 60, arcade.csscolor.LIGHT_PINK)

arcade.draw_rectangle_filled(90, 470, 5, 60, arcade.csscolor.LIGHT_PINK)

arcade.draw_rectangle_filled(105, 470, 5, 60, arcade.csscolor.LIGHT_PINK)

arcade.draw_rectangle_filled(120, 470, 5, 60, arcade.csscolor.LIGHT_PINK)

arcade.draw_rectangle_filled(135, 470, 5, 60, arcade.csscolor.LIGHT_PINK)

arcade.finish_render()

arcade.run()
