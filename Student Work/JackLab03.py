import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
car_x=100
def draw_grass():
    # Draw the ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.csscolor.DARK_GREEN)

def pine_tree(x, y):
    #Pine Tree
    # use x = 430, y = 240 as the position to determine the expressions for the
    # parameters of the drawing functions below
    arcade.draw_xywh_rectangle_filled(x - 10, y - 40, 20, 71, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(x - 40, y - 20, x + 40, y - 20, x, y, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(x - 35, y - 10, x + 35, y - 10, x, y + 15, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(x - 30, y, x + 30, y, x, y + 30, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(x - 25, y, x + 25, y, x, y + 45, arcade.csscolor.LIGHT_GREEN)
    arcade.draw_triangle_filled(x - 20, y, x + 20, y, x, y + 60, arcade.csscolor.LIGHT_GREEN)

    # Draw a point at x,y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)


#This function will draw a road through the forest
def road_draw(x,y):
    arcade.draw_xywh_rectangle_filled(0, 130, 800,50, arcade.csscolor.DARK_GRAY)
    arcade.draw_xywh_rectangle_filled(0, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(50, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(100, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(150, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(200, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(250, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(300, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(350, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(400, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(450, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(500, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(550, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(600, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(650, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(700, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(750, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(800, 150, 15,10, arcade.csscolor.YELLOW)
    arcade.draw_xywh_rectangle_filled(795, 150, 15,10, arcade.csscolor.YELLOW)
#This Function Will Draw a Car to drive down the road
def draw_car(x, y):
    arcade.draw_xywh_rectangle_filled(x, y , 30, 20, arcade.csscolor.RED)


    #draw_car(100,130)


def on_draw(delta_time):
    global car_x
    arcade.start_render()

    draw_grass()
#Draws the road
    road_draw(100,130)

    draw_car(car_x, 130)


    car_x += 1
    #Draws the car
    #draw_car(100,130)

    # Draw a pine tree
    pine_tree(430, 240)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 3")
    arcade.set_background_color(arcade.csscolor.SKY_BLUE)



    #  Finish and run
    #arcade.finish_render()
    # Call on draw every 60th of a second
    arcade.schedule(on_draw, 1/60)

    arcade.run()

# Call The Main Function to Get the Program Started
main()
