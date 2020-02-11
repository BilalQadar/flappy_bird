import pygame
import random

### STEP ONE: RENAME YOUR GAME ###
def name_your_game() -> str:
    """Return a string of the name that you would like to give your game"""
    pass

### STEP TWO: LOAD A BACKGROUND IMAGE ###
def get_background() -> str:
    """Return a string containing the location of your background image.
    Remember computers need to know where every file is, not just their name.
    Be sure that your string contains the location of your background image in
    relation to where this file is in your computer

    For your image to fit correctly with this game make sure its 1250 x 700
    pixels in size
    """
    pass
### STEP TWO: LOAD A BACKGROUND IMAGE ###
def get_gameover_background() -> str:
    """Return a string containing the location of your background image.
    Remember computers need to know where every file is, not just their name.
    Be sure that your string contains the location of your background image in
    relation to where this file is in your computer

    For your image to fit correctly with this game make sure its 1250 x 700
    pixels in size
    """
    pass
    
def get_character() -> str:
    """Return a string containing the location of your sprite image.
    Remember computers need to know where every file is, not just their name.
    Be sure that your string contains the location of your sprite image in
    relation to where this file is in your computer

    For your image to work with this game make sure its 255 x 255 pixels in size
    """
    pass

### STEP THREE: MOVE THE SPRITE ###
def sprite_down(sprite_position: list) -> list:
    """Return a list of new x and y coordinates for the character sprite. In
    flappy bird the bird is always moving down and its up to the player to move
    it upwards. Let's focus on making the bird travel downward.

    In game design, we make a sprite move by specifying a new location for it to
    travel to. Be careful to not have the sprite go off the screen.

    REMINDER: In python the top left corner of the screen is point (0,0)"""

    pass

def move_sprite(key: str, sprite_position: list) -> list:
    """Return a list of new x and y coordinates for the character sprite based
    on which key is pressed. In flappy bird the bird is always moving down and
    its up to the player to move it upwards. Let's focus on making the bird
    travel up if the up arrow key is pressed. If the player is pressing the up
    arrow key, the parameter key will be 'UP'.

    In game design, we make a sprite move by specifying a new location for it to
    travel to. Be careful to not have the sprite go off the screen.

    REMINDER: In python the top left corner of the screen is point (0,0) and the
    bottom right corner is (600,600)"""
    pass

def move_pipe(pipe_position: list, pipe_speed: float) -> list:
    """In a video game such as this one, its common to think the character is
    moving forward. In actuality it is the background that moves!
    By making the pipes move from right to left across the screen it makes it
    appear as if the character is moving.

    Similar to making the character move up and down, update the pipes position
    pipe_speed steps. Return a list of pipe_position [x,y].

    REMINDER: In python the top left corner of the screen is point (0,0)"""
    pass
### STEP FOUR: MAKE PIPES MOVE ACROSS THE SCREEN ###
def spawn_pipe(pipes: list) -> list:
    """Time to add some pipes to this game! pipes is a list of  2 pipe images.
    One being upside down and others is right side up.

    We want to randomly select one of these 2 pipes to spawn. Furthermore, we
    want to specify the size of each pipe (width, height). We may want to
    have a long and short pipe version to make your game more difficult.

    Lastly, we need to specify the location for each pipe to spawn. Most likey
    we want the pipe to spawn on the right corner of the screen. The right side
    up pipes will want to start on the bottom of the screen and the upside down
    pipe will want to start on the top of the screen.

    I wonder if there is a way to tell the pipe kind from its name? Remember
    file names include the location in the name!

    Return a list containing the pipe name, a tuple of the pipes size
    (width,height) and a tuple containing the pipes spawn position (x,y).
    """
    #Delete the 'pass' above. Write your code below this line
    pass

### STEP FIVE: CHECK FOR COLLISIONS ###
def x_intersection(rect1_left: float, rect1_right: float, rect2_left: float,
    rect2_right: float) -> bool:
    """In Scratch, we checked if two objects were touching based on color. In
    python however, things are a little bit different. In game design we
    determine whether two objects are touching based on if they are occupying
    the same space at any given time.

    In this function we want to check if two rectangles are occupying the same
    x space. Each paramter given represents an x coordinate of one of two
    rectangles. Return True if they are occupying the same x space, and False
    otherwise!

    It may be helpful to draw out two touching rectangles. This will help you
    write the logic for it!
    """
    pass

def y_interection(rect1_top: float, rect1_bottom: float, rect2_top: float,
    rect2_bottom: float) -> bool:
    """In this function we want to check if two rectangles are occupying the
    same y space. Each paramter given represents an y coordinate of one of two
    rectangles. Return True if they are occupying the same y space, and
    False otherwise!

    It may be helpful to draw out two touching rectangles. This will help you
    write the logic for it!
    """
    pass

### STEP SIX: KEEP SCORE ###
def update_score(pipe_list: list, score: int) -> int:
    """Let's add a scoreboard to our flappy bird game! We need to return an
    updated score based on how many pipes our character has traversed.

    pipe_list is a list of pipe objects. We need to iterate through them all
    using a loop and see if any of their x coordinates are negitive. If they
    are negitive that means our pipe has gone past our character successfully!

    For each pipe in pipe_list use pipe.get_position() to get an [x,y] list for
    the location of that particular pipe.

    Once we have incremented the score by 1, make sure to remove that pipe from
    the list!
    """
    pass

### ADD ON: MAKE THE GAME GET FASTER ###
def change_level(score: int, pipe_speed: float) -> float:
    """We want our game to get harder the longer a player plays. A cool way to
    do that is make our game get faster! Increase pipe_speed based on score.

    STUMPED? Level up everytime you pass 5 pipes. Think about what your scores
    will be divisible by."""
    #Delete the 'pass' above. Write your code below this line
    pass

### ADD ON: ADD MUSIC TO YOUR GAME###
def get_game_audio() -> str:
    """ Return a string with the name and location of a song you would like to
    play during your game!"""
    #Delete the 'pass' above. Write your code below this line
    pass

def get_gameover_audio() -> str:
    """Return a strong with the name and location of a song or sound clip you
    would like to play the game over screen is displayed"""

    pass