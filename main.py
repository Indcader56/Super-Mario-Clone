import pygame
import random
import math

# Original size is 256x240 new is 768x720
screen_width = 768
screen_height = 720

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Super Mario Clone")
clock = pygame.time.Clock()

block_sheet = pygame.image.load("assents.png")

# Used for spritesheets and animation (Credits to Coding with Russ)
def get_image(sheet, frame_x, frame_y, width, height, scale_x, scale_y, color):
	image = pygame.Surface((width, height), pygame.SRCALPHA)
	image.blit(sheet, (0,0), ((frame_x* width),(frame_y* height), width, height))
	image = pygame.transform.scale(image, (width * scale_x, height * scale_y))
	image.set_colorkey(color)

	return image

# The size of one individual tile
tile_size_x = 16
tile_size_y = 16

# The size of the actual game world (not including the ui and in tiles)
game_size_x = 16
game_size_y = 13

# The total size of the screen (in tiles)
screen_size_x = int(game_size_x)
screen_size_y = int(game_size_y + 2)

# The size of a tile when accounting for the screen size
scaled_tile_size_x = screen_width/screen_size_x
scaled_tile_size_y = screen_height/screen_size_y


# The scale x and y components for the tiles to properly fit a tile onto the screen
tile_scale_x = scaled_tile_size_x/tile_size_x
tile_scale_y = scaled_tile_size_y/tile_size_y

# Level data
level_size_x = 256
level_size_y = int(game_size_y)

level_data = [[0 for x in range(level_size_x)] for y in range(level_size_y)]

# Player data and key data
player_x = 0
player_y = 0

d_pressed = False
a_pressed = False
left_click = False


# Grabs all the images from the spritesheet beforehand
image_list = [get_image(block_sheet, i,0,tile_size_x,tile_size_y,tile_scale_x,tile_scale_y,(255,255,255)) for i in range(4)]

selected_tile = 0

while True:
	# Grabs the mouse x and y
	mouse_x = pygame.mouse.get_pos()[0]
	mouse_y = pygame.mouse.get_pos()[1]

	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				d_pressed = True
			if event.key == pygame.K_a:
				a_pressed = True
			if event.key == pygame.K_SPACE:
				selected_tile += 1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_d:
				d_pressed = False
			if event.key == pygame.K_a:
				a_pressed = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			left_click = True
		if event.type == pygame.MOUSEBUTTONUP:
			left_click = False

	if d_pressed:
		player_x += 4
	if a_pressed:
		player_x -= 4
	if left_click:
		level_data[math.floor(mouse_y/scaled_tile_size_y)-(screen_size_y-game_size_y)][math.floor((mouse_x+player_x)//scaled_tile_size_x)] = selected_tile


	if player_x < 0:
		player_x = 0
	if player_x > level_size_x*scaled_tile_size_x:
		player_x = level_size_x*scaled_tile_size_x

	if selected_tile > 3:
		selected_tile = 0
	if selected_tile < 0:
		selected_tile = 3

	player_screen_x = math.floor(player_x/(scaled_tile_size_x*game_size_x))


	screen.fill((0,100,255))

	# Game world

	# Screen A
	for tile_y in range(13):
		for tile_x in range(16):
			tile = image_list[level_data[tile_y][tile_x+(game_size_x*player_screen_x)]]
			screen.blit(tile, (((tile_x*scaled_tile_size_x)-player_x)+(player_screen_x*(scaled_tile_size_x*game_size_x)),(tile_y*scaled_tile_size_y)+((screen_size_y-game_size_y)*scaled_tile_size_y)))

	# Screen B (offsetted one screen length to the right)
	for tile_y in range(13):
		for tile_x in range(16):
			tile = image_list[level_data[tile_y][tile_x+(game_size_x*player_screen_x)+game_size_x]]
			screen.blit(tile, (((tile_x*scaled_tile_size_x)-player_x)+(player_screen_x*(scaled_tile_size_x*game_size_x))+(scaled_tile_size_x*game_size_x),(tile_y*scaled_tile_size_y)+((screen_size_y-game_size_y)*scaled_tile_size_y)))

	#screen.blit(image_list[3],(0,player_y))

	pygame.display.flip()
