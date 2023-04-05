import pygame


class Ship:
    def __init__(self, screen, settings):
        """初始化飞船相关参数"""
        self.center = None
        self.screen = screen
        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('resource/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom - self.rect.height
        # 飞船移动标志
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        # 引入飞船速度
        self.ai_settings = settings
        # 定义存储浮点坐标的成员变量
        self.f_center_x = float(self.rect.centerx)
        self.f_center_y = float(self.rect.centery)

    def update(self):
        # 如使用elif会导致向右移动的优先级最高
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.f_center_x += self.ai_settings.ship_speed
            # time.sleep(0.002)
        if self.moving_left and self.rect.left > 0:
            self.f_center_x -= self.ai_settings.ship_speed
            # time.sleep(0.002)
        if self.moving_up and self.rect.top > 0:
            self.f_center_y -= self.ai_settings.ship_speed
            # time.sleep(0.002)
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.f_center_y += self.ai_settings.ship_speed
            # time.sleep(0.002)
        self.rect.centerx = self.f_center_x
        self.rect.centery = self.f_center_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船恢复初始位置"""
        self.f_center_x = self.screen_rect.centerx
        self.f_center_y = self.screen_rect.bottom - self.rect.height
