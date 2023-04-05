from settings import Settings
from ship import Ship
from game_functions import *
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    pygame.init()
    settings = Settings()

    pygame.display.set_caption(settings.caption)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    ship = Ship(screen, settings)
    stats = GameStats(settings)

    # enemy = Enemy(settings, screen)
    bullets = Group()
    enemys = Group()
    create_fleet(settings, screen, ship, enemys)

    while True:
        check_events(ship, settings, bullets, screen)
        if stats.game_active:
            ship.update()
            update_bullets(settings, screen, ship, bullets, enemys)
            update_enemys(settings, stats, screen, ship, enemys, bullets)

        update_screen(settings, screen, ship, enemys, bullets)


run_game()
