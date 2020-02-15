import pygame
pygame.init()
n = int(input())
size = width, height = 400, 400
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('yellow'))
while pygame.event.wait().type != pygame.QUIT:
    depth = 0
    length = 0
    for i in range(height//n):
        for j in range(width//n):
            pygame.draw.polygon(screen,pygame.Color('orange'),[(length,depth+0.5*n),
                                                               (length+0.5*n,depth),
                                                               (length+n,depth+0.5*n),
                                                               (length+0.5*n,depth+n)])
            length+=n
        depth+=n
        length = 0
    pygame.display.flip()
pygame.quit()
