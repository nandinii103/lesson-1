import pygame
pygame.init()
screen = pygame.display.set_mode((500,800))
pygame.display.set_caption("Pictures window")
screen.fill((150,155,255))
image = pygame.image.load("pic.webp") 
screen.blit(image , (150,100))
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()


