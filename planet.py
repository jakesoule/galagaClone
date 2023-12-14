import pygame
import constants as c
import random

class Planet(pygame.sprite.Sprite):
    def __init__(self):
        super(Planet, self).__init__()
        self.planet = pygame.image.load('planet\\planet.png').convert_alpha()
        self.image = self.planet
        transform = random.randrange(2, 6)
        self.image = pygame.transform.scale(self.image, (transform*self.image.get_width(), transform*self.image.get_height()))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = 0 - self.rect.height
        self.vel_x = 0
        self.vel_y = random.randrange(1, 3)
    
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y