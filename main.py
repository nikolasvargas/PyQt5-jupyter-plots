#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Import and initialize pygame lib"""
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from chars import Player, Enemy
from scenery import Cloud
from configparser import ConfigParser

_cfg = ConfigParser()
_cfg.read('screen.ini')

SCREEN_WIDTH = int(_cfg['DEFAULT']['SCREEN_WIDTH'])
SCREEN_HEIGHT = int(_cfg['DEFAULT']['SCREEN_HEIGHT'])

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 250)
ADD_CLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_CLOUD, 1000)

player = Player()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

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
            enemies.add(new_cloud)
            all_sprites.add(new_cloud)

    key_pressed = pygame.key.get_pressed()
    player.update(key_pressed)
    enemies.update()
    clouds.update()

    # Fill the background with white color
    screen.fill((135, 206, 250))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
