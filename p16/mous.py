import pygame

pygame.init()
display = pygame.display.set_mode((300, 300), pygame.OPENGL)
pygame.display.set_caption('MOUSE')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print('x={}, y={}'.format(pos[0], pos[1]))
