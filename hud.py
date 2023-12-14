import pygame
import constants as c
from health import HealthBar
from score import Score
from lives import Lives

class HUD(pygame.sprite.Sprite):
    def __init__(self, hp, num_lives):
        super(HUD, self).__init__()
        self.image = pygame.image.load('.\\hud\\hud_bar.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (c.DISPLAY_WIDTH, self.image.get_height()*1.3))
        self.rect = self.image.get_rect()
        self.rect.x = ((c.DISPLAY_WIDTH - self.image.get_width())//2)
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.vel_x = 0
        self.vel_y = 0
        self.health_bar = HealthBar(hp)
        self.health_bar.rect.x = 10
        self.health_bar.rect.y = c.DISPLAY_HEIGHT - self.health_bar.rect.height - 30
        self.health_bar_group = pygame.sprite.Group()
        self.health_bar_group.add(self.health_bar)
        self.score = Score()
        self.score_group = pygame.sprite.Group()
        self.score_group.add(self.score)
        self.lives = Lives(num_lives)
        self.icons_group = pygame.sprite.Group()
        self.icons_group.add(self.lives)



    def update(self):        
        self.health_bar_group.update()

        hud_image_copy = self.image.copy()

        border_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        border_rect = border_surface.get_rect()
        pygame.draw.rect(hud_image_copy, (255, 255, 255), border_rect, 1)

        border_surface.blit(hud_image_copy, (0, 0))

        self.image = border_surface
        
        self.icons_group.update()
        self.score_group.update()

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
    