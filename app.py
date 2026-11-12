import pygame


pygame.init()


screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)


pygame.display.set_caption("Free Spotify")
icon = pygame.image.load('ishowspeed.jpg')
pygame.display.set_icon(icon)

color = ('white')
screen.fill(color)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()