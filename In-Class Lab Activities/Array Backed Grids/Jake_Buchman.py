import arcade

width = 20
height = 20
margin = 5
ROW_COUNT=10
COLUMN_COUNT=10
SCREEN_WIDTH = width * COLUMN_COUNT + margin * (COLUMN_COUNT + 1)
SCREEN_HEIGHT = width * ROW_COUNT + margin * (ROW_COUNT + 1)


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

        arcade.start_render()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                color = arcade.color.WHITE
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                x = (margin + width) * column + margin + width // 2
                y = (margin + width) * row + margin + width // 2
                arcade.draw_rectangle_filled(x, y, width, height, color)




    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        column = x // (width + margin)
        row = y // (height+margin)

        print(f"Click coordinates: ( {x}, {y}. Grid Coordinates: ({row}, {column})")

        if row < ROW_COUNT and column < COLUMN_COUNT:

            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
