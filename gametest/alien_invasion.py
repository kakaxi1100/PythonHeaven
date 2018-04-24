
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf 
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings();
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)

    ship = Ship(screen)
    bullets = Group()
    while True:
        gf.check_events(ship, screen, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()