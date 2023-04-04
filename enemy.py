import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('resource/ufo.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.f_x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            # self.settings.fleet_direction = -1
            return True
        elif self.rect.left <= 0:
            # self.settings.fleet_direction = 1
            return True

    def update(self):
        self.f_x += self.settings.enemy_speed * self.settings.fleet_direction
        self.rect.x = self.f_x
