"""
Sprite Collect Coins

Simple program to show basic sprite usage.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_collect_coins
"""

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.35
SPRITE_SCALING_COIN = .25
COIN_COUNT = 10
ROCK_COUNT = 50

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Sprite Collect Coins Example"


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Rock(arcade.Sprite):

    def update(self):
        self.center_y += 1
        if self.center_y >= SCREEN_HEIGHT:
            self.center_y = 0

        self.center_x += 1
        if self.center_x >= SCREEN_WIDTH:
            self.center_x = 0


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.rock_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set up timer
        self.total_time = 0.0
        self.timer_text = arcade.Text(
            text="00:00:00",
            start_x=10,
            start_y=40,
            color=arcade.color.WHITE,
            font_size=14,
            anchor_x="left",
        )
        # Set up sound
        self.sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.sound_player = None

        arcade.set_background_color(arcade.color.AMAZON)

    # Code to move goes here

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        img = "../../kenney_sokoban-pack/PNG/Retina/Player/player_03.png"
        self.player_sprite = arcade.Sprite(img, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin(":resources:images/items/gold_1.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            # Add the coin and rock to the lists
            self.coin_list.append(coin)

        for i in range(ROCK_COUNT):
            # Create the rock instance
            # Meteor image from kenney.nl
            rock = Rock(":resources:images/space_shooter/meteorGrey_big2.png", SPRITE_SCALING_COIN)

            # Position the rock
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin and rock to the lists
            self.rock_list.append(rock)

        # Timer
        self.total_time = 0.0

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.rock_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(text=output, start_x=10, start_y=20,
                         color=arcade.color.WHITE, font_size=14)

        # Draw the timer text
        self.timer_text.draw()

        # Draw GAME OVER message if true
        if len(self.coin_list) == 0:
            arcade.Text(
                text="GAME OVER",
                start_x=SCREEN_WIDTH // 2,
                start_y=SCREEN_HEIGHT // 2 - 50,
                color=arcade.color.WHITE,
                font_size=100,
                anchor_x="center",
            ).draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.coin_list.update()
        self.rock_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        rocks_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.rock_list)

        # Accumulate the total time if there are still coins
        if len(self.coin_list) > 0:
            self.total_time += delta_time

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            if not self.sound_player or not self.sound_player.playing:
                self.sound_player = arcade.play_sound(self.sound)

        for rock in rocks_hit_list:
            rock.remove_from_sprite_lists()
            self.score -= 1

        # Calculate minutes
        minutes = int(self.total_time) // 60

        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60

        # Calculate 100s of a second
        seconds_100s = int((self.total_time - seconds) * 100)

        # Use string formatting to create a new text string for our timer
        self.timer_text.text = f"{minutes:02d}:{seconds:02d}:{seconds_100s:02d}"


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
