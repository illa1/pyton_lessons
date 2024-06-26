import pygame
import random
import time

IMAGES_PATH = 'images/'

screen_width: int = 800
screen_height: int = 500

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))


class Goblin:
    x: int = 0
    y: int = 0
    speed: int = 2
    width: int = 0
    height: int = 0
    image_name: str = 'goblin1.png'
    image = None
    goblins_list: list = []

    def __init__(self):
        self.image_load()

    def image_load(self):
        self.image = pygame.image.load(IMAGES_PATH + self.image_name)

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = int(screen_width)
        self.y = int(screen_height / 2 - self.height / 2)

    def show(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.x > -self.width:
            self.x -= self.speed

    def add(self):
        self.goblins_list.append(self.image)

    def draw(self):
        for item in self.goblins_list:
            item.show()


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
    loop_punch = -1

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
        elif direction == 'right':
            self.image = self.image_right
            self.move_right()
        elif direction == 'up':
            self.move_up()
        elif direction == 'down':
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

    def punch(self, player_punch):

        if self.loop_punch > 0:
            self.loop_punch += 1

            if self.loop_punch > 5:
                self.image = self.image_right
                self.loop_punch = -1

        if player_punch == 'punch' and self.loop_punch < 0:
            self.image = self.image_punch
            self.loop_punch = 1

    def show(self):
        screen.blit(self.image, (self.x, self.y))


class Game:
    run = True
    goblin = None
    player: Player
    player_direction: str = ''
    player_punch: str = ''
    fps: int = 60
    clock = pygame.time.Clock()
    goblin_event = pygame.USEREVENT + 1

    def __init__(self):
        self.bg = pygame.image.load('images/bg-title.png')
        self.player = Player()

        self.goblin = Goblin()

    def background_add(self, image: str):
        self.bg = pygame.image.load(image)

    def background_draw(self, xy: tuple = (0, 0)):
        screen.blit(self.bg, xy)

    def goblin_add(self):
        pygame.time.set_timer(self.goblin_event, random.randint(500, 2000))
        self.goblin.add()

    def play(self):
        while self.run:
            self.clock.tick(self.fps)

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
                        self.player_punch = 'punch'
                elif event.type == pygame.KEYUP:
                    self.player_direction = ''
                    self.player_punch = ''
                elif event.type == self.goblin_event:
                    self.goblin_add()
                    print(1)

            if self.run:
                self.background_draw()
                self.player.move(self.player_direction)
                self.player.punch(self.player_punch)
                self.goblin.show()
                self.goblin.move()
                self.goblin.draw()
                self.player.show()

                pygame.display.update()


play = Game()
play.play()
