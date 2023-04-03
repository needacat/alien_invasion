class Settings:
    def __init__(self):
        self.caption = 'Alien Invasion'
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed = 0.3
        # 子弹相关配置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 120, 50, 103
        self.bullet_speed = 0.8
        self.bullet_attack_interval = 0.1
