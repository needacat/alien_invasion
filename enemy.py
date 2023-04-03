import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = settings
        self.image = pygame.image.load('resource/ufo.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.f_x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
