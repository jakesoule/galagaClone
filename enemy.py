import pygame
import constants as c
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.img_explosion_01 = pygame.image.load('.\\spaceships\\explosion1.png').convert_alpha()
        self.img_explosion_01 = pygame.transform.scale(self.img_explosion_01, (self.img_explosion_01.get_width()*3, self.img_explosion_01.get_height()*3))
        self.img_explosion_02 = pygame.image.load('.\\spaceships\\explosion2.png').convert_alpha()
        self.img_explosion_02 = pygame.transform.scale(self.img_explosion_01, (self.img_explosion_02.get_width()*3, self.img_explosion_02.get_height()*3))
        self.img_explosion_03 = pygame.image.load('.\\spaceships\\explosion3.png').convert_alpha()
        self.img_explosion_03 = pygame.transform.scale(self.img_explosion_03, (self.img_explosion_03.get_width()*3, self.img_explosion_03.get_height()*3))
        self.img_explosion_04 = pygame.image.load('.\\spaceships\\explosion4.png').convert_alpha()
        self.img_explosion_04 = pygame.transform.scale(self.img_explosion_04, (self.img_explosion_04.get_width()*3, self.img_explosion_04.get_height()*3))
        self.img_explosion_05 = pygame.image.load('.\\spaceships\\explosion5.png').convert_alpha()
        self.img_explosion_05 = pygame.transform.scale(self.img_explosion_05, (self.img_explosion_05.get_width()*3, self.img_explosion_05.get_height()*3))

        self.anim_explosion = [
            self.img_explosion_01,
            self.img_explosion_02,
            self.img_explosion_03,
            self.img_explosion_04,
            self.img_explosion_05
        ]
        self.anim_index = 0
        self.frame_length = 3

        self.image = pygame.image.load('.\\spaceships\\ships\\blue.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*3, self.image.get_height()*3))
        self.is_destroyed = False
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

        if self.is_destroyed:
            max_index = len(self.anim_explosion) - 1
            if self.anim_index > max_index:
                self.kill()
            else:
                if self.frame_length == 0:
                    self.image = self.anim_explosion[self.anim_index]
                    self.anim_index += 1
                    self.frame_length = random.randrange(1,6)
                else:
                    self.frame_length -= 1
        
    def get_hit(self):
        self.hp -= 1
        self.snd_hit.play()
        if self.hp <= 0:
            self.is_destroyed = True
            self.rect.x = self.rect.x - 35
            self.rect.y = self.rect.y - 35
            self.image = self.anim_explosion[self.anim_index]