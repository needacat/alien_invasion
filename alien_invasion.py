from settings import Settings
from ship import Ship
from enemy import Enemy
from game_functions import *
from pygame.sprite import Group


def run_game():
    pygame.init()
    settings = Settings()

    pygame.display.set_caption(settings.caption)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    ship = Ship(screen, settings)
    # enemy = Enemy(settings, screen)
    bullets = Group()
    enemys = Group()
    create_fleet(settings, screen, ship, enemys)

    while True:
        check_events(ship, settings, bullets, screen)
        ship.update()
        bullets.update(bullets)

        update_screen(settings, screen, ship, enemys, bullets)


run_game()
