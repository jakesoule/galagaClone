import pygame
import constants as c
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('.\\spaceships\\ships\\blue.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*3, self.image.get_height()*3))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.snd_hit = pygame.mixer.Sound('.\\sound_fx\\sounds\\Hit-1.ogg')
        self.hp = 3
        self.vel_x = 0
        self.vel_y = random.randrange(3, 8)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
    
    def get_hit(self):
        self.hp -= 1
        self.snd_hit.play()
        if self.hp <= 0:
            self.destroy()
        
    def destroy(self):
        self.kill()