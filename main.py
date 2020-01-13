#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Import and initialize pygame lib"""
import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.sprite import Group
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from chars import Player, Enemy
from scenery import Cloud
from configparser import ConfigParser

_cfg: ConfigParser = ConfigParser()
_cfg.read('game_config.ini')

SCREEN_WIDTH: int = int(_cfg['SCREEN']['WIDTH'])
SCREEN_HEIGHT: int = int(_cfg['SCREEN']['HEIGHT'])


def game_run() -> int:
    pygame.init()
    screen: Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: Clock = Clock()

    ADD_ENEMY: int = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_ENEMY, 250)

    ADD_CLOUD: int = pygame.USEREVENT + 2
    pygame.time.set_timer(ADD_CLOUD, 1000)

    player: Player = Player()

    enemies: Group = Group()
    clouds: Group = Group()
    all_sprites: Group = Group()

    all_sprites.add(player)

    running: bool = True

    while running:
        for event in pygame.event.get():
            exit_key: bool = (
                event.type == QUIT or
                event.type == KEYDOWN and event.key == K_ESCAPE
            )
            if exit_key:
                running = False
            elif event.type == ADD_ENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADD_CLOUD:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)

        key_pressed: dict = pygame.key.get_pressed()
        player.update(key_pressed)
        enemies.update()
        clouds.update()

        # Fill the background with white color
        screen.fill((135, 206, 250))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            end_game = player.reset()
            if end_game:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    return 0


if __name__ == "__main__":
    game_run()
