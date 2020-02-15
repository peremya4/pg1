import pygame

pygame.init()
n = int(input())
k = 150 // n
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
while pygame.event.wait().type != pygame.QUIT:
    for i in range(0, 150, k):
        pygame.draw.ellipse(screen, (255, 255, 255), (0, i, 300, (150 - i) * 2), 1)
        pygame.draw.ellipse(screen, (255, 255, 255), (i, 0, (150 - i) * 2, 300), 1)
    pygame.display.flip()
pygame.quit()
