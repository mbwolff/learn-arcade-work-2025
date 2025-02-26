"""
This is an original drawing and animation of some chicks using the Python arcade for Lab 3.
Cluck! cluck!
"""

"""Import the "arcade" library"""
import arcade

"""Constant values"""
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

"""Opens window"""
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
arcade.set_background_color(arcade.color.SKY_BLUE)

"""Draw sky"""
def draw_sky():
    arcade.set_background_color(arcade.color.SKY_BLUE)

"""Draw ground"""
def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.BITTER_LIME)

"""Draw chick"""
def draw_chick(x, y):
    """Chick body: in LAB 2 x = 300 and y = 200"""
    arcade.draw_ellipse_filled(x, y, 120, 160, arcade.color.DANDELION)
    arcade.draw_point(x, y, arcade.color.RED, 5)
    """Chick head"""
    arcade.draw_circle_filled(x, y + 100, 50, arcade.color.CORN)
    """Left Wing"""
    arcade.draw_ellipse_filled(x - 70, y + 30, 40, 100, arcade.color.CORN, 45)
    """Right Wing"""
    arcade.draw_ellipse_filled(x + 70, y + 30, 40, 100, arcade.color.CORN, -45)
    """Left foot"""
    arcade.draw_triangle_filled(x - 50, y - 80, x - 15, y - 80, x - 35, y - 50, arcade.color.SELECTIVE_YELLOW)
    """Right foot"""
    arcade.draw_triangle_filled(x + 20, y - 80, x + 60, y - 80, x + 40, y - 50, arcade.color.SELECTIVE_YELLOW)
    """Left Eye"""
    arcade.draw_circle_filled(x - 20, y + 110, 9, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 20, y + 110, 5, arcade.color.BLACK)
    """Right eye"""
    arcade.draw_circle_filled(x + 20, y + 110, 9, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 20, y + 110, 5, arcade.color.BLACK)
    """Beak"""
    arcade.draw_triangle_filled(x - 10, y + 80, x + 10, y + 80, x, y + 60, arcade.color.SELECTIVE_YELLOW)

"""Draw Nest"""
def draw_nest(x, y):
    """Nest base"""
    arcade.draw_arc_filled(x + 200, y - 70, 190, 200, arcade.color.UNIVERSITY_OF_CALIFORNIA_GOLD, 180, 360)
    """Nest hole"""
    arcade.draw_ellipse_filled(x + 200, y - 70, 190, 60, arcade.color.BISTRE_BROWN)
    """Egg"""
    arcade.draw_ellipse_filled(x + 200, y - 70, 40, 50, arcade.color.BEIGE)

"""Call functions"""
arcade.start_render()
draw_sky()
draw_grass()
draw_chick(300, 200)
draw_nest(300, 200)
draw_chick(400, 100)
draw_nest(400, 100)


# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()