# so that we have a formula for every time we want to use sprite sheets
import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour):
        sprite_run_image = pygame.Surface((width, height)).convert_alpha()
        sprite_run_image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height ))
        sprite_run_image = pygame.transform.scale(sprite_run_image, (width * scale, height *scale)) # this is used to make the image bigger or smaller
        sprite_run_image.set_colorkey(colour)
        
        return sprite_run_image
