import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("first rectangle")
BLACK= (0,0,0)
BLUE = (0,125,255)
rectangle = pygame.Rect(250,200,300,150)
running= True
while running:
    screen.fill(BLACK)
    pygame.draw.rect(screen,BLUE,rectangle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()

    


