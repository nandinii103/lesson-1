import pygame
pygame.init()
screen = pygame.display.set_mode((600,700))
pygame.display.set_caption("First game screen")
background_colour= (50,150,200)
running = True
while running:
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    screen.fill(background_colour)
    pygame.display.update()
pygame.quit()

