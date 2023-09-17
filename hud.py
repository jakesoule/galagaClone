import pygame
import constants as c
from health import HealthBar

class HUD(pygame.sprite.Sprite):
    def __init__(self):
        super(HUD, self).__init__()
        self.image = pygame.image.load('.\\hud\\hud_bar.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (c.DISPLAY_WIDTH, self.image.get_height()*1.3))
        self.rect = self.image.get_rect()
        self.rect.x = ((c.DISPLAY_WIDTH - self.image.get_width())//2)
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.vel_x = 0
        self.vel_y = 0
        self.health_bar = HealthBar()
        self.health_bar.rect.x = 10
        self.health_bar.rect.y = c.DISPLAY_HEIGHT - self.health_bar.rect.height - 30
        self.health_bar_group = pygame.sprite.Group()
        self.health_bar_group.add(self.health_bar)



    def update(self):        
        self.health_bar_group.update()

        hud_image_copy = self.image.copy()

        border_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        border_rect = border_surface.get_rect()
        pygame.draw.rect(hud_image_copy, (255, 255, 255), border_rect, 1)

        border_surface.blit(hud_image_copy, (0, 0))

        self.image = border_surface

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
    