#!/usr/bin/env python3
#Grid
#Jason Mitchell
#11/16/17

import pygame
pygame.init()

size = (800, 800)
screen = pygame.display.set_mode(size)

Red = (255,0,0)

done = False
while not done:

    Y_offset = -4
    for x in range(1, 10):
        Y_offset = Y_offset + 10
        x_offset = 6
    for y in range(1, 100):
        pygame.draw.circle(screen, Red, [x_offset, Y_offset], 3, 0)

    pygame.display.update()

    for even in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()

