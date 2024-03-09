# --------------------------------------------------- #
#   * * *   *   *  * * *      *     **    **  * * *   #
#   *   *    * *   *   *     * *    * *  * *  *       #
#   * * *    **    *         * *    *  *   *  * * *   #
#   *        *     *  **    * * *   *  *   *  *       #
#   *       *      * * *   *     *  *      *  * * *   #
# --------------------------------------------------- #

import pygame
import sys

screen_with = 800
screen_height = 600
# ініціалзація pygame
pygame.init()
# створюємо вікно
screen = pygame.display.set_mode((screen_with, screen_height))
# інтервал оновлення екрану
clock = pygame.time.Clock()
clock_tick = 60

# заголовок
pygame.display.set_caption('SPYDER')

# завантаження зображення
spyder_img = pygame.image.load('images/spyder.png')
spyder_position = {'x': 10, 'y': 100}

# background = pygame.Surface((screen_with, screen_height))
# background.fill('Black')
background = pygame.image.load('images/background.jpg')

# додаємо текст
count_fly = pygame.font.Font('fonts/MadimiOne-Regular.ttf',50)
text_count_fly = count_fly.render('Count: 0', False, 'Black')
#-----------------------------------------------------
while True:
    # перевіряємо події
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # 1 робимо разрахунки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if spyder_position['y'] > 0:
            spyder_position['y'] -= 4
    if keys[pygame.K_s]:
        if spyder_position['y'] < screen_height - 110:
            spyder_position['y'] += 4
    if keys[pygame.K_a]:
        if spyder_position['x'] > 0:
            spyder_position['x'] -= 4
    if keys[pygame.K_d]:
        if spyder_position['x'] < screen_with - 110:
            spyder_position['x'] += 4


    # 2 додаємо обєкт
    screen.blit(background, (0, 0))
    screen.blit(spyder_img, (spyder_position['x'], spyder_position['y']))
    screen.blit(text_count_fly, (600, 10))
    # 3 оновлюємо область екрану
    pygame.display.update()
    clock.tick(clock_tick)