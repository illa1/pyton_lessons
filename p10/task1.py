# Розкоментувати і виправити помилки в програмі

import pygame as pg
import sys


pg.init()
run = True
window = pg.display.set_mode((600, 600))
SkyColor = (124, 255, 235)
window.fill(SkyColor)
hero = pg.image.load("images/pikachu.png")

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    window.blit(hero, (44, 64))
    pg.display.flip()


