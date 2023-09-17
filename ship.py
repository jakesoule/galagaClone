import pygame
import constants as c
from bullet import Bullet

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load('.\\spaceships\\ships\\brown.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*3, self.image.get_height()*3))
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height * 2
        self.bullets = pygame.sprite.Group()
        self.snd_shoot = pygame.mixer.Sound('.\\sound_fx\\sounds\\Fire 1.ogg')
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.reload = 0
    
    def update(self):
        self.reload += 1
        self.bullets.update()
        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        self.rect.x += self.vel_x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= c.DISPLAY_WIDTH - self.rect.width:
            self.rect.x = c.DISPLAY_WIDTH - self.rect.width
        self.rect.y += self.vel_y

    def shoot(self):
        if self.reload >= 0:
            self.snd_shoot.play()
            new_bullet = Bullet()
            new_bullet.rect.x = self.rect.x + 22
            new_bullet.rect.y = self.rect.y
            self.bullets.add(new_bullet)
            self.reload = 0
        