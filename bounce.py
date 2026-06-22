import pygame
import random
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("bounce back colourful")
class Box(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.speed_x = 4
        self.speed_y = 4
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        bounced = False
        if self.rect.right >= WIDTH:
            self.speed_x = -self.speed_x
            bounced = True
        if self.rect.left <= 0:
             self.speed_x = -self.speed_x
             bounced = True
        if self.rect.bottom >= HEIGHT:
            self.speed_y = -self.speed_x
            bounced = True
        if self.rect.top <= 0:
             self.speed_y = -self.speed_x
             bounced = True 
        if bounced:
            self.image.fill(
                (
                    random.randint(0,255),
                    random.randint(0,255),
                    random.randint(0,255)

                    
                )
            ) 
            return True
        return False
box = Box()
all_sprites = pygame.sprite.Group()
all_sprites.add(box)
background_colour = (255,255,255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    bounced = box.update()
    if bounced:
        background_colour = (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)

        )
    screen.fill(background_colour)
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()
    



        


    

