import pygame
import random

IMAGES_PATH = 'images/'

screen_width: int = 800
screen_height: int = 500

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))


class Player:
    x: int = 0
    y: int = 0
    speed: int = 5
    width: int = 0
    height: int = 0
    image_name: str = 'player1.png'
    image_punch_name: str = 'player_punch.png'
    image = None
    image_left = None
    image_right = None
    image_punch = None

    def __init__(self):
        self.image_load()

    def image_load(self):
        self.image_right = pygame.image.load(IMAGES_PATH + self.image_name)
        self.image = self.image_right
        self.image_left = pygame.transform.flip(self.image_right, 180, 0)
        self.image_punch = pygame.image.load(IMAGES_PATH + self.image_punch_name)

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = int(screen_width / 2 - self.width / 2)
        self.y = int(screen_height / 2 - self.height / 2)

    def move(self, direction: str):
        if direction == 'left':
            self.image = self.image_left
            self.move_left()
        if direction == 'right':
            self.image = self.image_right
            self.move_right()
        if direction == 'up':
            self.move_up()
        if direction == 'down':
            self.move_down()

    def move_left(self):
        if self.x - self.speed >= 0:
            self.x -= self.speed
        else:
            self.x = 0

    def move_right(self):
        if self.x + self.speed <= screen_width - self.width:
            self.x += self.speed
        else:
            self.x = screen_width - self.width

    def move_up(self):
        if self.y - self.speed >= 0:
            self.y -= self.speed
        else:
            self.y = 0

    def move_down(self):
        if self.y + self.speed <= screen_height - self.height:
            self.y += self.speed
        else:
            self.y = screen_height - self.height

    def punch(self):
        self.image = self.image_punch

    def show(self, player_punch: str = ''):
        screen.blit(self.image, (self.x, self.y))
        if player_punch == 'True':
            self.punch()


class Game:
    run = True
    player: Player
    player_direction: str = ''
    player_punch = ''
    fps: int = 60
    clock = pygame.time.Clock()

    def __init__(self):
        self.bg = pygame.image.load('images/bg-title.png')
        self.player = Player()

    def background_add(self, image: str):
        self.bg = pygame.image.load(image)

    def background_draw(self, xy: tuple = (0, 0)):
        screen.blit(self.bg, xy)

    def play(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player_direction = 'left'
                    if event.key == pygame.K_d:
                        self.player_direction = 'right'
                    if event.key == pygame.K_w:
                        self.player_direction = 'up'
                    if event.key == pygame.K_s:
                        self.player_direction = 'down'
                    if event.key == pygame.K_r:
                        self.player_punch = 'True'
                elif event.type == pygame.KEYUP:
                    self.player_direction = ''
                    self.player_punch = ''


            if self.run:
                self.background_draw()
                self.player.move(self.player_direction)
                self.player.show()

                pygame.display.update()
                self.clock.tick(self.fps)


play = Game()
play.play()
