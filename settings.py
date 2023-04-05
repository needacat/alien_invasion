class Settings:
    def __init__(self):
        self.caption = 'Alien Invasion'
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed = 0.8
        self.ship_limit = 3
        # 子弹相关配置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 120, 50, 103
        self.bullet_speed = 1.2
        self.bullet_attack_interval = 0.1
        # 敌人相关配置
        self.enemy_speed = 0.2
        self.fleet_drop_speed = 10
        ## -1为左，1为右
        self.fleet_direction = 1
