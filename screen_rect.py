import pygame
pygame.init()
screen = pygame.display.set_mode((600,800))
pygame.display.set_caption("rectangle")
RED = (255,0,0)
BLUE = (0,125,255)
rect = pygame.Rect(200,300,250,150)
running = True
while running:
    screen.fill(RED)
    pygame.draw.rect(screen,BLUE,rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()
pygame.quit()