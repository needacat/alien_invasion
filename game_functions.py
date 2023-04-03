import sys
import pygame
from bullet import Bullet
from enemy import Enemy


def check_keydown_event(event, screen, ship, bullets, ai_settings):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    # 检测是否按下空格
    if event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ship, ai_settings, bullets, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, screen, ship, bullets, ai_settings)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship, enemys, bullets):
    screen.fill(ai_settings.bg_color)
    # 绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制飞船
    ship.blitme()
    enemys.draw(screen)
    pygame.display.flip()


def get_number_enemys_x(settings, enemy_width):
    available_space_x = settings.screen_width - 2 * enemy_width
    number_enemys_x = int(available_space_x / (2 * enemy_width))
    return number_enemys_x


def create_enemy(settings, screen, enemys, enemy_number, row_number):
    enemy = Enemy(settings, screen)
    enemy_width = enemy.rect.width
    enemy.f_x = enemy_width + 2 * enemy_width * enemy_number
    enemy.rect.x = enemy.f_x
    enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row_number
    enemys.add(enemy)


def create_fleet(settings, screen, ship, enemys):
    enemy = Enemy(settings, screen)
    number_enemys_x = get_number_enemys_x(settings, enemy.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, enemy.rect.height)
    for row_number in range(number_rows):
        for enemy_number in range(number_enemys_x):
            create_enemy(settings, screen, enemys, enemy_number, row_number)


def get_number_rows(settings, ship_height, enemy_height):
    available_space_y = (settings.screen_height - (3 * enemy_height) - ship_height)
    number_rows = int(available_space_y / (2 * enemy_height))
    return number_rows
