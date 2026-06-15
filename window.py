import pygame
pygame.init()
screen = pygame.display.set_mode((600,900))
pygame.display.set_caption("First window")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()


