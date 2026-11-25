import pygame
import random

screen_width = 960
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

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	for tile_y in range(13):
		for tile_x in range(16):
			tile = get_image(block_sheet, 0,0,16,16,1,1,(255,255,255))
			screen.blit(tile, (tile_x*16,tile_y*16))

	pygame.display.flip()

clock.tick(60)