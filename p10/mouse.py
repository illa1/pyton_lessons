import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

PAINT_CIRCLE = 1
CLEAR_CIRCLE = 2

colors = [(0, 0, 255), (0, 255, 0), (255, 0 ,0)]


def draw_circle(action, color):
    if action == CLEAR_CIRCLE:
        color = (0, 0, 0)

    pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, color, pos, 18)
    pygame.display.update()


def change_color():
    # keyboard
    current_color = colors[0]
    keys = pygame.key.get_pressed()

    if keys[pygame.K_1]:
        current_color = colors[0]
    elif keys[pygame.K_2]:
        current_color = colors[1]
    elif keys[pygame.K_3]:
        current_color = colors[2]
    return current_color


def main ():
    mouse_button = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_button = True
                if event.button == 3:
                    pass
                    # draw_circle(CLEAR_CIRCLE)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_button = False
        # ENd --------------------------------------------------------




        if mouse_button:
            draw_circle(PAINT_CIRCLE, change_color())


main()