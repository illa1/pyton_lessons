
import pygame
import random
import time
import sys

IMAGES_PATH = 'images/'
IMAGES_MENU_PATH = 'images/menu/'
IMAGES_BG_PATH = 'images/background/'
FONTS_PATH = 'fonts/'
SCREEN_WIDTH = 256 * 3
SCREEN_HEIGHT = 256 * 2
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class Bullet:
    bullet = None

    def __init__(self, x: int, y: int):
        self.bullet = pygame.Surface((3, 5))
        self.bullet.fill((0, 0, 50))

        self.x = x + 14
        self.y = y
        self.speed = 2

    def move(self):
        self.y -= self.speed

    def draw(self):
        screen.blit(self.bullet, (self.x, self.y))


class Bullets:
    bullet_list: list = []

    def add(self, x: int, y: int):
        self.bullet_list.append(Bullet(x, y))

    def move(self):
        for b in self.bullet_list:
            b.move()

            if b.y < 0:
                self.bullet_list.remove(b)

            b.draw()


class Player:
    moving: list = []
    dt = 1
    bullets = None

    def __init__(self):
        n = random.randint(0, 9)
        self.image = pygame.image.load(IMAGES_PATH + f'ship_000{n}.png')
        self.x = int(SCREEN_WIDTH / 2)
        self.y = SCREEN_HEIGHT - (self.image.get_height() + 10)
        self.speed = 5

        self.bullets = Bullets()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if len(self.moving) > 0:
            if self.moving[0] == pygame.K_LEFT:
                self.move_left()
            if self.moving[0] == pygame.K_RIGHT:
                self.move_right()

        self.bullets.move()

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

    def shoot(self):
        self.bullets.add(self.x, self.y)


class Background:
    bg_image = None
    bg_surface = None

    def __init__(self):
        self.x = 0
        self.y = -SCREEN_HEIGHT
        self.speed = 1
        self.bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT * 2))

        self.add_background()

    def add_background(self):
        self.bg_image = pygame.image.load(IMAGES_PATH + 'Ground_Tile_01.png')
        nx = int(SCREEN_WIDTH / self.bg_image.get_width()) + 1
        ny = int(SCREEN_HEIGHT / self.bg_image.get_height()) + 1
        w = self.bg_image.get_width()
        h = self.bg_image.get_height()

        for y in range(ny * 2):
            for x in range(nx):
                self.bg_surface.blit(self.bg_image, (w * x, h * y))

    def draw_background(self):
        self.y += self.speed

        if self.y >= 0:
            self.y = -SCREEN_HEIGHT

        screen.blit(self.bg_surface, (self.x, self.y))


class Menu:
    def __init__(self):
        bg_img = pygame.image.load(IMAGES_MENU_PATH + 'bg-02.jpg')
        self.bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        box_img = pygame.image.load(IMAGES_MENU_PATH + 'm_01.png')
        self.box_img = pygame.transform.scale(box_img, (300, 400))

    def start_btn(self):
        color = (0, 0, 0)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if self.start_pos():
            color = (255, 255, 255)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        font = pygame.font.SysFont(FONTS_PATH + 'PermanentMarker-Regular.ttf', 40)
        text = font.render('START', True, color)
        screen.blit(text, (340, 130)) # 430 160

        font = pygame.font.SysFont('Arial', 14)
        text = font.render('or pres key - S', True, 'black')
        screen.blit(text, (338, 160))

    def draw(self):
        screen.blit(self.bg_img, (0, 0))
        screen.blit(self.box_img, ((SCREEN_WIDTH / 2 - (self.box_img.get_width() / 2)), (SCREEN_HEIGHT / 2 - self.box_img.get_height() / 2)))
        self.start_btn()
        self.start_pos()

    def start_pos(self):
        pos = pygame.mouse.get_pos()

        if (pos[0] > 340 and pos[0] < 430 and pos[1] > 130 and pos[1] < 160):
            return True

        return False

    def mouse_click(self):
        b = pygame.mouse.get_pressed()  # (False, False, False)

        if self.start_pos() and b[0]:
            return 'run'

        return None


class Enemy:
    x: int = 0
    y: int = 0
    speed: int = 3
    image = None

    def __init__(self, img):
        self.image = img
        self.x = random.randint(0, SCREEN_WIDTH)

    def move(self):
        self.y += self.speed

    def fire(self):
        pass

    def show(self):
        screen.blit(self.image, (self.x, self.y))


class Enemies:
    enemies_list = []

    def add(self):
        # self.enemies_list.append(self.enemy)
        img_ = pygame.image.load(IMAGES_PATH + 'ship_0016.png')
        img = pygame.transform.rotate(img_, 180)
        self.enemies_list.append(Enemy(img))

    def draw(self):
        for item in self.enemies_list:
            item.show()

    def move(self):
        for item in self.enemies_list:
            item.move()

    # def delete(self, bullets: int):
    #     for item in self.enemies_list:
    #         if ((bullets.x > item.x and bullets.x < item.x + 100) and (bullets.y > item.y and bullets.y < item.y + 3)):
    #             self.enemies_list.remove(item)


class Game:
    bg_game = None
    game_run: bool = False
    enemies_event = pygame.USEREVENT + 1

    def __init__(self):
        self.player = Player()
        self.bg_game = Background()
        self.menu = Menu()
        self.dt = 1
        self.interval = time.time()
        self.enemies = Enemies()
        self.bullets = Bullets()

    def enemies_add(self):
        pygame.time.set_timer(self.enemies_event, random.randint(500, 2000))
        self.enemies.add()

    def delta_time(self):
        clock.tick(FPS)
        self.dt = time.time() - self.interval
        self.interval = time.time()

        self.player.dt = self.dt

    def init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.run()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.menu.mouse_click() == 'run':
                        self.run()

            self.menu.draw()
            pygame.display.update()

    def run(self):
        self.game_run = True
        self.enemies_add()

        while self.game_run:
            self.delta_time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        if event.key not in self.player.moving:
                            self.player.moving.append(event.key)
                            print(self.player.moving)
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()
                    if event.key == pygame.K_q:
                        self.game_run = False
                        break
                elif event.type == pygame.KEYUP:
                    if event.key in self.player.moving:
                        self.player.moving.remove(event.key)
                elif event.type == self.enemies_event:
                    self.enemies_add()

            if self.game_run:
                self.bg_game.draw_background()
                self.player.move()
                self.player.draw()

                self.enemies.move()
                self.enemies.draw()
                # self.enemies.delete(self.bullets)

                pygame.display.update()


# запуск програми
if __name__ == '__main__':
    game = Game()
    game.init()
