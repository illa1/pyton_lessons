import pygame
import random
import time

IMAGES_PATH = 'images/'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 500

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class Player:
    moving: int = ''
    def __init__(self):
        n = random.randint(0, 9)
        self.image = pygame.image.load(IMAGES_PATH + f'ship_000{n}.png')
        self.x = int(SCREEN_WIDTH / 2)
        self.y = SCREEN_HEIGHT - (self.image.get_height() + 10)
        self.speed = 5

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.moving == pygame.K_LEFT:
            self.move_left()
        if self.moving == pygame.K_RIGHT:
            self.move_right()

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
        else:
            self.x = 0

    def move_right(self):
        if self.x < SCREEN_WIDTH - self.image.get_width():
            self.x += self.speed
        else:
            self.x = SCREEN_WIDTH - self.image.get_width()

    def fire(self):
        pass


class Game:
    bg_image = None

    def __init__(self):
        self.bg_date = {}
        self.add_background()
        self.player = Player()
        self.dt = 1
        self.interval = time.time()

    def add_background(self):
        n = random.randint(1, 2)
        self.bg_image = pygame.image.load(IMAGES_PATH + f'Ground_Tile_0{n}.png')
        self.bg_date['nx'] = int(SCREEN_WIDTH / self.bg_image.get_width()) + 1
        self.bg_date['ny'] = int(SCREEN_HEIGHT / self.bg_image.get_height()) + 1
        self.bg_date['w'] = self.bg_image.get_width()
        self.bg_date['h'] = self.bg_image.get_height()

    def draw_background(self):
        for y in range(self.bg_date['ny']):
            for x in range(self.bg_date['nx']):
                screen.blit(self.bg_image, (self.bg_date['w']*x, self.bg_date['h']*y))

    def delta_time(self):
        clock.tick(FPS)
        self.dt = time.time() - self.interval
        self.interval = time.time()

        self.player.dt = self.dt

    def init(self):
        while True:
            self.delta_time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.moving = pygame.K_LEFT
                    if event.key == pygame.K_RIGHT:
                        self.player.moving = pygame.K_RIGHT
                elif event.type == pygame.KEYUP:
                    self.player.moving = 0

            self.draw_background()
            self.player.move()
            self.player.draw()

            pygame.display.update()


# запуск програми
if __name__ == '__main__':
    game = Game()
    game.init()
