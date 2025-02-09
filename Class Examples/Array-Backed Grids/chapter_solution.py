import arcade

# SCREEN_WIDTH = 500
# SCREEN_HEIGHT = 600
WIDTH = 20
HEIGHT = 20
MARGIN = 5
ROW_COUNT = 16
COLUMN_COUNT = 16
SCREEN_WIDTH = ROW_COUNT * WIDTH + (ROW_COUNT + 1) * MARGIN
SCREEN_HEIGHT = COLUMN_COUNT * HEIGHT + (COLUMN_COUNT + 1) * MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        # --- Create grid of numbers
        # Create an empty list
        self.grid = []
        # Loop for each row
        for row in range(ROW_COUNT):
            # For each row, create a list that will
            # represent an entire row
            self.grid.append([])
            # Loop for each column
            for column in range(COLUMN_COUNT):
                # Add a the number zero to the current row
                self.grid[row].append(0)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # Set row 1, column 5 to one
#        self.grid[1][5] = 1

        arcade.start_render()

        for column in range(COLUMN_COUNT):
            x = column * WIDTH + WIDTH / 2 + (column + 1) * MARGIN
            for row in range(ROW_COUNT):
                y = row * HEIGHT + HEIGHT / 2 + (row + 1) * MARGIN
                color = arcade.color.WHITE
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                arcade.draw_rectangle_filled(center_x=x, center_y=y, width=WIDTH,
                                             height=HEIGHT, color=color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT or button == arcade.MOUSE_BUTTON_RIGHT:
            column = x // (WIDTH + MARGIN)
            row = y // (HEIGHT + MARGIN)
#            print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column}).")
            self.grid[row][column] = (self.grid[row][column] + 1) % 2


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
