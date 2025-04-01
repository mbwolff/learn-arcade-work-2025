import arcade
#from pymunk.examples.arrows import width


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = 0  # Instead of zero, calculate the proper x location using 'column'
            x = column * 10 + 5
            y = 0  # Instead of zero, calculate the proper y location using 'row'
            y = row * 10 + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    for row in range(30):
        for column in range(30):
            x = 0  # Instead of zero, calculate the proper x location using 'column'
            # Shifts it to the right
            x = column * 10 + 300 + 5
            y = 0  # Instead of zero, calculate the proper y location using 'row'
            y = row * 10 + 5
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5,5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

    # Below, replace "pass" with your code for the loop.
    # Use the modulus operator and an if statement to select the color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x.
    pass


def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    for row in range(30):
        for column in range(30):
            x = 0  # Instead of zero, calculate the proper x location using 'column'
            #Shifts it to the right
            x = column * 10 + 600 + 5
            y = 0  # Instead of zero, calculate the proper y location using 'row'
            y = row * 10 + 5
            if row % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5,5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
    pass


def draw_section_4():
    for row in range(30):
        for column in range(30):
            x = 0  # Instead of zero, calculate the proper x location using 'column'
            # Shifts it to the right
            x = column * 10 + 900 + 5
            y = 0  # Instead of zero, calculate the proper y location using 'row'
            y = row * 10 + 5
            if (column + row) % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5,5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)

    # Use the modulus operator and just one 'if' statement to select the color.
    pass

#Essentially once you figure this out you just copy and paste it and manipulate the X
def draw_section_5():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    for row in range(30):
        for column in range(30 - row):
            x = 0  # Instead of zero, calculate the proper x location using 'column'
            x = (30 - column) * 10 - 5
            y = 0  # Instead of zero, calculate the proper y location using 'row'
            #Shifts the row up
            y = row * 10 + 5 + 300
            arcade.draw_rectangle_filled(x , y, 5, 5, arcade.color.WHITE)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
                #for column in range(row):
                    #arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    pass


def draw_section_6():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    for row in range(30):
        for column in range(30 - row):
            x = 0  # Instead of zero, calculate the proper x location using 'column'
            x = (column * 10 + 5 + 300)
            y = 0  # Instead of zero, calculate the proper y location using 'row'
            # Shifts the row up
            y = row * 10 + 5 + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            # for column in range(row):
            # arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

    pass


def draw_section_7():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    for row in range(30):
        for column in range(row + 1):
            x = 0  # Instead of zero, calculate the proper x location using 'column'
            x = (column * 10 + 5 + 600)
            y = 0  # Instead of zero, calculate the proper y location using 'row'
            # Shifts the row up
            y = row * 10 + 5 + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            # for column in range(row):
            # arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    pass
def draw_section_8():
    for row in range(30):
        for column in range(row + 1):
            x = 0  # Instead of zero, calculate the proper x location using 'column'
            x = (30 - column) * 10 + 895
            y = 0  # Instead of zero, calculate the proper y location using 'row'
            # Shifts the row up
            y = row * 10 + 5 + 300
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            # for column in range(row):
            # arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
    pass


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
