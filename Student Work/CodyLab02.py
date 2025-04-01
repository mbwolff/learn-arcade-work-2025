# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Cody's House")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()
# Set the background color
arcade.set_background_color(arcade.color.SKY_BLUE)
# Draw the grass
arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.APPLE_GREEN)

# --- Draw the House ---

# House Main
arcade.draw_lrtb_rectangle_filled(300, 500, 300, 150, arcade.color.RED)
# Roof of the house
arcade.draw_triangle_filled(280, 300, 520, 300, 400, 400, arcade.color.DARK_BROWN)
# Front Door
arcade.draw_rectangle_filled(400, 200, 50, 100, arcade.color.DARK_BROWN)
# Draw Windows
arcade.draw_rectangle_filled(340, 240, 40, 40, arcade.color.GRAY)
arcade.draw_rectangle_filled(460, 240, 40, 40, arcade.color.GRAY)
# Window Panels/lines Horizontal
arcade.draw_line(340, 260, 340, 220, arcade.color.BLACK, 3)
arcade.draw_line(320, 240, 360, 240, arcade.color.BLACK, 3)
# Window Panels/lines Vertical
arcade.draw_line(460, 260, 460, 220, arcade.color.BLACK, 3)
arcade.draw_line(440, 240, 480, 240, arcade.color.BLACK, 3)

# --- Draw the barn ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
