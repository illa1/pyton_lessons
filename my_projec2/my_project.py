import pygame
import random
import time

IMAGES_PATH = 'images/'

screen_width: int = 800
screen_height: int = 500


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))


class Heart:
    x: int = 5
    y: int = 5
    width: int = 0
    height: int = 0
    image_name: str = 'heart1.png'
    image = None

    def __init__(self):
        self.image_load()

    def image_load(self):
        image = pygame.image.load(IMAGES_PATH + self.image_name)
        self.image = pygame.transform.scale(image, (30, 30))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def show(self):
        screen.blit(self.image, (self.x, self.y))


class Hearts:
    heart_list = []

    def __init__(self):
        step = 0

        for i in range(1, 4):
            heart = Heart()
            heart.x += step
            self.heart_list.append(heart)
            step += 32

    def draw(self):
        for h in self.heart_list:
            h.show()
            # if heart_lost == 0:
            #     self.heart_list.remove(h)


    def collision(self):
        pass


class Goblin:
    speed: int = 2
    width: int = 0
    height: int = 0
    image_name: str = 'goblin1.png'
    image = None
    goblins_list: list = []
    heart_lost: int = 3

    def __init__(self):
        self.image_load()

    def image_load(self):
        self.image = pygame.image.load(IMAGES_PATH + self.image_name)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def show(self, item):
        screen.blit(item['im'], (item['x'], item['y']))

    def move_item(self, item):
        if item['x'] >= -self.width:
            item['x'] -= self.speed
            self.show(item)
            return 1

        return 0

    def add(self):
        g = {'im': self.image, 'x': screen_width, 'y': random.randint(0, screen_height-100)}
        self.goblins_list.append(g)

    def draw(self, player):
        for item in self.goblins_list:
            n = self.move_item(item)

            # if self.check_col():
            if n == 0:
                self.goblins_list.remove(item)
                if self.heart_lost > 0:
                    self.heart_lost -= 1
                    print(self.heart_lost)
                    if self.heart_lost == 0:
                        pygame.quit()

            if player.image == player.image_punch:
                if ((item['x'] + self.width / 2 >= player.x and item['x'] <= player.x + player.width / 2) and
                        (item['y'] + self.height / 2 >= player.y and item['y'] <= player.y + player.height / 2)):
                    self.goblins_list.remove(item)

    # def check_col(self, obj):
    #     if 1 == 2:
    #         return True
    #
    #     return False


class Player:
    direction: list = []
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

    # def move(self, direction: str):
    #     if direction == 'left':
    #         self.image = self.image_left
    #         self.move_left()
    #     elif direction == 'right':
    #         self.image = self.image_right
    #         self.move_right()
    #     elif direction == 'up':
    #         self.move_up()
    #     elif direction == 'down':
    #         self.move_down()


    def move(self):
        if len(self.direction) > 0:
            if self.direction[0] == pygame.K_a:
                self.move_left()
            if self.direction[0] == pygame.K_d:
                self.move_right()
            if self.direction[0] == pygame.K_w:
                self.move_up()
            if self.direction[0] == pygame.K_s:
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
    heart: Heart
    # player_direction: str = ''
    player_punch: str = ''
    fps: int = 60
    clock = pygame.time.Clock()
    goblin_event = pygame.USEREVENT + 1

    def __init__(self):
        self.bg = pygame.image.load('images/bg-title.png')
        self.player = Player()
        self.hearts = Hearts()

        self.goblin = Goblin()
        pygame.time.set_timer(self.goblin_event, random.randint(500, 2000))

    def background_add(self, image: str):
        self.bg = pygame.image.load(image)

    def background_draw(self, xy: tuple = (0, 0)):
        screen.blit(self.bg, xy)

    def goblin_add(self):
        pygame.time.set_timer(self.goblin_event, random.randint(500, 2000))
        self.goblin.add()

    def heart_lost_game(self, heart_lost: int):
        if heart_lost == 0:
            self.run = False

    def play(self):
        while self.run:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
                        if event.key not in self.player.direction:
                            self.player.direction.append(event.key)

                    if event.key == pygame.K_r:
                        self.player_punch = 'punch'
                elif event.type == pygame.KEYUP:
                    if event.key in self.player.direction:
                        self.player.direction.remove(event.key)
                    self.player_punch = ''
                elif event.type == self.goblin_event:
                    self.goblin_add()

            if self.run:
                self.background_draw()
                self.player.move()
                self.player.punch(self.player_punch)
                self.goblin.draw(self.player)
                self.player.show()
                self.hearts.draw()

                pygame.display.update()


play = Game()
play.play()
