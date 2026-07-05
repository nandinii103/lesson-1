
import pygame

pygame.init()

screen = pygame.display.set_mode((500,400))

player = pygame.Rect(50,50,50,50)

coin = pygame.Rect(300,150,40,40)

running = True

while running:

for event in pygame.event.get():

if event.type == pygame.QUIT:

running = False

keys = pygame.key.get_pressed()

if keys[pygame.K_LEFT]:

player.x -= 5

if keys[pygame.K_RIGHT]:

player.x += 5

if keys[pygame.K_UP]:

player.y -= 5

if keys[pygame.K_DOWN]:

player.y += 5

screen.fill((255,255,255))

pygame.draw.rect(screen,(0,0,255),player)

pygame.draw.rect(screen,(255,0,0),coin)

if player.colliderect(coin):

print("You collected the coin!")

pygame.display.update()

pygame.quit()