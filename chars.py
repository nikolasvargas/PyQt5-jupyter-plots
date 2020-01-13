import random
from pygame import image, Rect, Surface
from pygame.sprite import Sprite
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL
from configparser import ConfigParser
from assets.colors import COLORS

_cfg = ConfigParser()
_cfg.read('game_config.ini')

SCREEN_WIDTH = int(_cfg['SCREEN']['WIDTH'])
SCREEN_HEIGHT = int(_cfg['SCREEN']['HEIGHT'])


class Player(Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.surf: Surface = image.load("assets/jet.png").convert()
        self.surf.set_colorkey(COLORS['WHITE'], RLEACCEL)

        self.rect: Rect = self.surf.get_rect()
        self.original_pos: Rect = self.surf.get_rect()

        self.window_bounds: int = 0
        self.lives: int = int(_cfg['PLAYER']['LIVES'])

    def _check_bounds(self) -> None:
        if self.rect.left < self.window_bounds:
            self.rect.left = self.window_bounds
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= self.window_bounds:
            self.rect.top = self.window_bounds
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def update(self, key: dict) -> None:
        if key[K_UP]:
            self.rect.move_ip(0, -5)
        elif key[K_DOWN]:
            self.rect.move_ip(0, 5)
        elif key[K_LEFT]:
            self.rect.move_ip(-5, 0)
        elif key[K_RIGHT]:
            self.rect.move_ip(5, 0)

        self._check_bounds()

    def reset(self) -> int:
        if not bool(self.lives):
            return 1

        self.lives = self.lives - 1
        self.reset_position()
        return 0

    def reset_position(self) -> None:
        self.rect = self.original_pos


class Enemy(Sprite):
    def __init__(self):
        super().__init__()

        self.surf: Surface = image.load("assets/missile.png").convert()
        self.surf.set_colorkey(COLORS['WHITE'], RLEACCEL)
        self.rect: Rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT)
            )
        )
        self.speed: int = random.randint(5, 20) * -1

    def update(self) -> None:
        self.rect.move_ip(self.speed, 0)
        if self.rect.right < 0:
            self.kill()
