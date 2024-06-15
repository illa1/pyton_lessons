import sys
import pygame
import os
import random

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True
clock = pygame.time.Clock()

laser_surf = pygame.image.load(os.path.join('images', 'laser.png')).convert_alpha()
star_surf = pygame.image.load(os.path.join('images', 'star.png')).convert_alpha()

meteor_surf = []
for i in range(2):
    meteor_surf.append(pygame.image.load(os.path.join('images', f'meteor{i}.png')).convert_alpha())

explosion_frames = []
for i in range(21):
    explosion_frames.append(pygame.image.load(os.path.join('images', 'explosion', '{0}.png'.format(i))).convert_alpha())


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('images', 'Ship'+str(random.randint(1, 8))+'.png')).convert_alpha()
        self.rect = self.image.get_frect(center=(int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2)))
        self.direction = pygame.math.Vector2()
        self.speed = 300

        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 200

        self.rotation = 0

        # mask
        # self.mask = pygame.mask.from_surface(self.image) # не обовязково, створюється автоматично
        #mask = pygame.mask.from_surface(self.image)
        #mask_surf = mask.to_surface()
        #mask_surf.set_colorkey((0,0,0))
        #self.image = mask_surf


    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            print(pygame.K_SPACE)
            Laser(laser_surf, self.rect.center, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
            laser_sound.play()

        self.laser_timer()

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True


class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos: tuple = ()):
        super().__init__(groups)

        surf = pygame.transform.scale(surf, (random.randint(10, 50), random.randint(10, 50)))
        self.image = surf

        if not pos:
            pos = (random.randint(0, WINDOW_WIDTH), random.randint(0, WINDOW_HEIGHT))

        self.rect = self.image.get_frect(center=pos)

    def update(self, dt):
        self.rect.centery += 20 * dt

        if self.rect.top > WINDOW_HEIGHT:
            self.kill()


class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom=pos)

        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.rect.centery -= 400 * dt

        if self.rect.bottom < 0:
            self.kill()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)

        img = surf[random.randint(0, len(surf))-1]
        image_width, image_height = img.get_size()
        aspect_ratio = image_width / image_height

        new_width = random.randint(50, image_width)
        new_height = new_width / aspect_ratio
        self.original_surf = pygame.transform.scale(img, (int(new_width), int(new_height)))

        self.image = self.original_surf
        self.rect = self.image.get_frect(center=pos)

        self.start_time = pygame.time.get_ticks()
        self.lifetime = 5000
        self.direction = pygame.Vector2(random.uniform(-0.5, 0.5), 1)
        self.speed = random.randint(100, 250)

        #self.mask = pygame.mask.from_surface(self.image)
        self.rotation_speed = random.randint(-20, 20)
        self.rotation = 0

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt

        self.rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotate(self.original_surf, self.rotation)
        self.rect = self.image.get_frect(center=self.rect.center)

        if pygame.time.get_ticks() - self.start_time > self.lifetime:
            self.kill()


class AnimationExplosion(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups):
        super().__init__(groups)
        self.frames = frames
        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        self.rect = self.image.get_frect(midbottom=pos)

    def update(self, dt):
        self.frames_index += 50 * dt
        if self.frames_index <= len(self.frames):
            self.image = self.frames[int(self.frames_index)]
        else:
            self.kill()



# ===========================================
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()

for i in range(20):
    Star(all_sprites, star_surf)


player = Player(all_sprites)

# custom events -> meteor
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 1000)

star_event = pygame.event.custom_type()
pygame.time.set_timer(star_event, 1000)

font = pygame.font.Font(os.path.join('images', 'Oxanium-Bold.ttf'), 20)

laser_sound = pygame.mixer.Sound(os.path.join('audio', 'laser.wav'))
laser_sound.set_volume(0.04)
explosion_sound = pygame.mixer.Sound(os.path.join('audio', 'explosion.wav'))
explosion_sound.set_volume(0.04)
damage_sound = pygame.mixer.Sound(os.path.join('audio', 'damage.ogg'))
damage_sound.set_volume(0.04)
game_sound = pygame.mixer.Sound(os.path.join('audio', 'game_music.wav'))
game_sound.set_volume(0.06)
game_sound.play(loops=-1)


def collisions():
    collided_meteor = pygame.sprite.spritecollide(player, meteor_sprites, False, pygame.sprite.collide_mask)
    if collided_meteor:
        damage_sound.play()
        collided_meteor[0].kill()

    for laser in laser_sprites:
        collided_laser = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_laser:
            laser.kill()
            AnimationExplosion(explosion_frames, laser.rect.midtop, all_sprites)
            explosion_sound.play()


def display_score():
    current_time = str(pygame.time.get_ticks() // 100)
    text_surf = font.render(current_time, True, (240, 230, 230))
    text_rect = text_surf.get_rect(topleft=(20, 20))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, (240, 120, 230), text_rect.inflate(10, 5).move(0, -8), 2, 2)


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == meteor_event:
            x, y = random.randint(50, WINDOW_WIDTH-50), random.randint(-150, -50)
            Meteor(meteor_surf, (x, y), (all_sprites, meteor_sprites))
        elif event.type == star_event:
            x, y = random.randint(10, WINDOW_WIDTH-10), random.randint(-50, -10)
            Star(all_sprites, star_surf, (x, y))

    # update
    all_sprites.update(dt)
    collisions()

    # draw the game
    display_surface.fill('gray5')
    all_sprites.draw(display_surface)
    display_score()

    pygame.display.update()

pygame.quit()
sys.exit()
