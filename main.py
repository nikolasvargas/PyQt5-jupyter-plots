#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Import and initialize pygame lib"""
import pygame
from pygame import Surface
from pygame.sprite import Sprite
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600


class Player(Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.surf = Surface((75, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.window_bounds = 0

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
        if key[K_DOWN]:
            self.rect.move_ip(0, 5)
        if key[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if key[K_RIGHT]:
            self.rect.move_ip(5, 0)

        self._check_bounds()


pygame.init()
screen: Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()
running: bool = True

while running:
    for event in pygame.event.get():
        exit_key: bool = (
            event.type == QUIT or
            event.type == KEYDOWN and event.key == K_ESCAPE
        )
        if exit_key:
            running = False

    key_pressed = pygame.key.get_pressed()
    player.update(key_pressed)

    # Fill the background with white color
    screen.fill((0, 0, 0))

    screen.blit(player.surf, player.rect)

    pygame.display.flip()

pygame.quit()
