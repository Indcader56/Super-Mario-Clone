import pygame
import random

screen_width = 256
screen_height = 240

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

# The size of the actual game world (not including the ui)
game_size_x = 16
game_size_y = 13

# The total size of the screen
screen_tile_size_x = int(game_size_x)
screen_tile_size_y = int(game_size_y + 2)

# The scale x and y components for the tiles to properly fit them onto the screen
screen_scale_x = (screen_width/screen_tile_size_x)/tile_size_x
screen_scale_y = (screen_height/screen_tile_size_y)/tile_size_y

screen_tile_size_x = screen_width/screen_tile_size_x
screen_tile_size_y = screen_height/screen_tile_size_y

while True:
	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()


	# Game world
	for tile_y in range(13):
		for tile_x in range(16):
			tile = get_image(block_sheet, 0,0,tile_size_x,tile_size_y,screen_scale_x,screen_scale_y,(255,255,255))
			screen.blit(tile, (tile_x*screen_tile_size_x,tile_y*screen_tile_size_y))

	pygame.display.flip()
