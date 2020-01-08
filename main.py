#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Import and initialize pygame lib"""
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = (800, 600)
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    # Fill the background with white color
    screen.fill((255, 255, 255))

    surf = pygame.Surface((50, 50))
    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    surf_center = (
        (SCREEN_WIDTH - surf.get_width()) / 2,
        (SCREEN_HEIGHT - surf.get_height()) / 2,
    )

    screen.blit(surf, surf_center)

    # pygame.draw.circle(screen, (0, 0 ,255), (250, 250), 75)
    pygame.display.flip()

pygame.quit()

