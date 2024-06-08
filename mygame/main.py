import pygame
import random
import time
import sys
import asyncio

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
        self.rect = self.bullet.get_rect()

        self.rect.x = x + 14
        self.rect.y = y
        self.speed = 2


    def move(self):
        self.rect.y -= self.speed

    def draw(self):
        screen.blit(self.bullet, self.rect)


class Bullets:
    bullet_list: list = []

    def add(self, x: int, y: int):
        self.bullet_list.append(Bullet(x, y))

    def move(self):
        for b in self.bullet_list:
            b.move()
            if b.rect.y < 0:
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
            elif self.moving[0] == pygame.K_RIGHT:
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


class AnimationExplosion:
    def __init__(self, x=0, y=0):
        self.index = 0
        self.frames = []
        img = pygame.image.load(IMAGES_PATH + 'explosion.png')
        for i in range(-10, 10):
            k = 5 * (10 - abs(i) + 1)
            im = pygame.transform.scale(img, (k, k))
            self.frames.append(im)

        self.x = x
        self.y = y
        self.end_animation = False

    def animation(self):
        self.index += 1
        if self.index >= len(self.frames):
            self.end_animation = True
            self.index = 0

        screen.blit(self.frames[self.index], (self.x, self.y))


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
        self.bg_image = pygame.image.load(IMAGES_PATH + 'ground_tile_02.png')
        nx = int(SCREEN_WIDTH / self.bg_image.get_width())
        ny = int(SCREEN_HEIGHT / self.bg_image.get_height())
        w = self.bg_image.get_width()
        h = self.bg_image.get_height()

        # 1
        for y in range(ny * 2):
            for x in range(nx):
                self.bg_surface.blit(self.bg_image, (w * x, h * y))
        # 2
        # bg_image2 = self.bg_image.copy()
        # bg_image2 = pygame.transform.flip(bg_image2, 0, 180)
        # self.bg_surface.blit(self.bg_image, (0, 0))
        # self.bg_surface.blit(self.bg_image2, (0, 0))

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


# class Enemy:
#     x: int = 0
#     y: int = 0
#     speed: int = 0
#     image = None
#
#     def add(self):
#         pass
#
#     def move(self):
#         pass
#
#     def fire(self):
#         pass


enemies_group = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        n = random.randint(0, 9)
        self.image = pygame.image.load(IMAGES_PATH + f'ship_000{n}.png')
        self.image = pygame.transform.rotate(self.image, 180)
        x, y = random.randint(50, SCREEN_WIDTH-50), random.randint(-100, -50)
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = random.randint(30, 90)

    def update(self, dt):

        self.rect.centery += 2  # self.speed * dt

        print(self.rect)

        if self.rect.centery > SCREEN_HEIGHT:  # TODO 100 - треба забрати
            self.kill()


class Game:
    bg_game = None
    game_run: bool = False

    def __init__(self):
        self.player = Player()
        self.bg_game = Background()
        self.menu = Menu()

        self.dt = 1
        self.interval = time.time()

        self.enemy_event = pygame.event.custom_type()
        pygame.time.set_timer(self.enemy_event, random.randint(1500, 3000))

        self.collision_explosion = []

    def delta_time(self):
        clock.tick(FPS)
        self.dt = time.time() - self.interval
        self.interval = time.time()
        self.player.dt = self.dt

    def collision(self):
        for b in self.player.bullets.bullet_list:
            for e in enemies_group:
                if pygame.sprite.collide_rect(b, e):
                    self.collision_explosion.append(AnimationExplosion(e.rect.x, e.rect.y))
                    self.player.bullets.bullet_list.remove(b)
                    e.kill()
        for e in self.collision_explosion:
            e.animation()
            if e.end_animation:
                self.collision_explosion.remove(e )

    async def init(self):
        while True:
            if self.game_run:
                self.run()
            else:
                self.main_menu()

            pygame.display.update()
            await asyncio.sleep(0)

    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.game_run = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu.mouse_click() == 'run':
                    self.game_run = True

        self.menu.draw()

    def run(self):
        self.delta_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    if event.key not in self.player.moving:
                        self.player.moving.append(event.key)
                elif event.key == pygame.K_SPACE:
                    self.player.shoot()
                elif event.key == pygame.K_q:
                    self.game_run = False
                    break
            elif event.type == pygame.KEYUP:
                if event.key in self.player.moving:
                    self.player.moving.remove(event.key)
            if event.type == self.enemy_event:
                Enemy(enemies_group)

        # ---
        if self.game_run:
            self.bg_game.draw_background()
            self.player.move()
            self.player.draw()
            enemies_group.update(self.dt)
            self.collision()
            enemies_group.draw(screen)


# запуск програми
if __name__ == '__main__':
    game = Game()
    asyncio.run(game.init())


