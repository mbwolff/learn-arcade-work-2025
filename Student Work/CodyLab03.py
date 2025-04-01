# Import the "arcade" library
import arcade

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

def draw_codys_car():

    arcade.draw_circle_filled(75, 170, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(200, 170, 20, arcade.color.BLACK)
    arcade.draw_rectangle_filled(130, 230, 170, 100, arcade.color.WHITE)
    arcade.draw_rectangle_filled(200, 205, 130, 50,arcade.color.WHITE)
    arcade.draw_rectangle_filled(170, 250, 60, 40, arcade.color.BLACK)

def draw_trees():
    arcade.draw_rectangle_filled(600, 200, 40, 270, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(600,400, 100, arcade.color.FERN_GREEN)

def draw_birds():
    arcade.draw_circle_filled(400, 500, 20, arcade.color.BLACK)
    arcade.draw_triangle_filled(440, 490, 420, 490, 420, 515, arcade.color.ORANGE)
    arcade.draw_ellipse_filled(400, 500, 20, 80, arcade.color.BLACK)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Cody's Function")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

    draw_codys_car()
    draw_trees()
    draw_birds()

    arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.APPLE_GREEN)


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

    arcade.finish_render()
    arcade.run()

main()
