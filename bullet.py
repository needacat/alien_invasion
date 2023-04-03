import threading
import time

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top - 20
        self.f_y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed
        self.attack_flag = True
        self.ai_settings = settings
        self.screen = screen
        self.ship = ship
        self.delay = settings.bullet_attack_interval

    def attack_timer(self, bullets):
        start_time = time.time()
        while start_time - time.time() < self.delay:
            continue
        new_bullet = Bullet(self.ai_settings, self.screen, self.ship, self.ai_settings.bullet_attack_interval)
        bullets.add(new_bullet)

    def update(self, bullets):
        """移动子弹"""
        self.f_y -= self.speed
        self.rect.y = self.f_y
        if self.rect.bottom > self.screen.get_rect().bottom:
            self.kill()

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
