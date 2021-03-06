import random


# STEP ONE: LOAD A BACKGROUND IMAGE
def get_background() -> str:
	""" Return a string containing the path to your background image.

	Remember computers need to know where every file is, not just its name. More
	specifically the computer needs the path to that image!

	For your image to fit correctly with this game make sure its 900 x 700
	pixels in size
	"""

	file_name = "assets/images/background.png"
	return file_name


# STEP TWO: LOAD A BACKGROUND IMAGE
def get_gameover_background() -> str:
	""" Return a string containing the path to your game over background image.

	Remember computers need to know where every file is, not just its name. More
	specifically the computer needs the path to that image!

	For your image to fit correctly with this game make sure its 900 x 700
	pixels in size
	"""

	file_name = "assets/images/game-over.jpg"
	return file_name


# STEP THREE: LOAD A CHARACTER IMAGE
def get_character() -> str:
	""" Return a string containing the path to your character image.

	Remember computers need to know where every file is, not just its name. More
	specifically the computer needs the path to that image!

	For your image to fit correctly with this game make sure its 255 x 255
	pixels in size
	"""

	file_name = "assets/images/bird.png"
	return file_name


# STEP FOUR: MOVE THE SPRITE DOWN
def sprite_down(sprite_position: list) -> list:
	""" Return a list of new x and y coordinates for the character sprite. In
	flappy bird the bird is always moving down and its up to the player to move
	it upwards. Let's focus on making the bird travel downward.

	In game design, we make a sprite move by specifying a new location for it to
	travel to. Be careful to not have the sprite go off the screen.

	REMINDER: In python the top left corner of the screen is point (0,0). The
	bottom right corner of the screen is (800,600)
	"""

	fall_amount = 10

	if sprite_position[1] < 600:
		sprite_position[1] = sprite_position[1] + fall_amount
	else:
		sprite_position[1] = 600

	return sprite_position


# STEP FIVE: MOVE THE SPRITE UP
def move_sprite(key: str, sprite_position: list) -> list:
	""" Return a list of new x and y coordinates for the character sprite based
	on which key is pressed. Let's focus on making the bird travel up if the up
	arrow key is pressed. If the player is pressing the up arrow key, the
	parameter key will be 'UP'.

	In game design, we make a sprite move by specifying a new location for it to
	travel to. Be careful to not have the sprite go off the screen.

	REMINDER: In python the top left corner of the screen is point (0,0) and the
	bottom right corner is (800,600)
	"""
	jump_amount = 60

	if key == 'UP' and sprite_position[1] >= 0:
		sprite_position[1] -= jump_amount

	return sprite_position


# STEP SIX: SPAWN A PIPE
def spawn_pipe(pipes: list) -> list:
	""" Time to add some pipes to this game! pipes is a list of file paths for
	two pipe images. The list looks like this:

	["assets/images/pipe_upside_down.png" , "assets/images/pipe.png"]

	We want to randomly select one of these 2 pipes to spawn. Furthermore, we
	want to specify the size of each pipe (width, height). Given below is two
	different sizes. Large is a long configuration of a pipe and small is a
	short configuration of the pipe. We want to randomly select the size as
	well.

	Lastly, we need to specify the location for each pipe to spawn. We want the
	pipe to spawn on the right corner of the screen. The right side up pipes
	will want to start on the bottom of the screen and the upside down pipe will
	want to start on the top of the screen.

	Return a list containing the pipe name, a list of the pipes size
	[width,height] and a list containing the pipes spawn position [x,y].
	
	REMINDER: In python the top left corner of the screen is point (0,0). The bottom right corner of the screen is (800,600)
	"""

	# size = [x,y]
	large = [100, 400]
	small = [100, 300]
	possible_sizes = [large, small]

	# Pick a random pipe image
	pipe = random.choice(pipes)
	# Pick a random pipe size
	size = random.choice(possible_sizes)

	# If the pipe is upside down make it start on the bottom of the screen
	if pipe == "assets/images/pipe_upside_down.png":
		start_position = [900, 0]
	else:
		start_position = [900, 450]

	return [pipe, size, start_position]


# STEP SEVEN: MOVE THE PIPES
def move_pipe(pipe_position: list, pipe_speed: float) -> list:
	"""In a video game such as this one, its common to think the character is
	moving forward. However it is the background that moves!

	By making the pipes move from right to left across the screen it creates the
	illusion that it is the character which is moving.

	Similar to making the character move up and down, update the pipes position
	using its speed. Return a list of pipe_position [x,y].

	REMINDER: In python the top left corner of the screen is point (0,0)
	"""

	pipe_position[0] -= pipe_speed
	return pipe_position


# STEP EIGHT: DETECT COLLISIONS
def x_intersection(rect1_left: float, rect1_right: float, rect2_left: float,
    rect2_right: float) -> bool:
	""" In Scratch, we checked if two objects were touching based on color. In
	python however, things are a little bit different. In game design we
	determine whether two objects are touching based on if they are occupying
	the same space at any given time.

	In this function we want to check if two rectangles are occupying the same
	'x space'. Each paramater given represents an x coordinate on a rectangle.

	Return True Rect1 and Rect2 are occupying the same x space, and False
	otherwise!

	HINT: Draw two rectanlges touching. This may help write the logic for it!
	"""

	if rect1_left < rect2_right and rect1_right > rect2_left:
		return True
	else:
		return False

def y_interection(rect1_top: float, rect1_bottom: float, rect2_top: float,
    rect2_bottom: float) -> bool:
	""" In this function we want to check if two rectangles are occupying the
	same 'y space'. Each paramater given represents an y coordinate on a
	rectangle.

	Return True Rect1 and Rect2 are occupying the same y space, and False
	otherwise!

	HINT: Draw two rectanlges touching. This may help write the logic for it!
	"""

	if rect1_top < rect2_bottom and rect1_bottom > rect2_top:
		return True
	else:
		return False


# ADD ON: KEEPING SCORE
def update_score(pipe_list: list, score: int) -> int:
	"""Let's add a scoreboard to our flappy bird game! We need to return an
	updated score based on how many pipes our character has passed.

	pipe_list is a list of pipe objects. We need to iterate through them all
	using a loop and see if any of their x coordinates are negitive. If they
	are negitive that means the pipe has gone off the screen.

	For each pipe in pipe_list use pipe.get_position() to get an [x,y] list for
	the location of that particular pipe.
	"""

	for pipe in pipe_list:
		position = pipe.get_position()
		if position[0] < 0:
			score += 1

	return score


# ADD ON: MAKE THE GAME FASTER
def change_level(score: int, pipe_speed: float) -> float:
	"""We want our game to get harder the longer a player plays. A cool way to
	do that is make our game get faster! Increase pipe_speed based on score.

	STUMPED? Increase the speed whenever the score is divisible by 5. Is 0 divisible by 5?
	"""

	if score % 5 == 0 and score != 0:
		pipe_speed += 2

	return pipe_speed