import pygame


pygame.init()


screen = pygame.display.set_mode((1080, 720))


pygame.display.set_caption("Free Spotify")
icon = pygame.image.load('ishowspeed.jpg')
pygame.display.set_icon(icon)


color = ('white')
screen.fill(color)
pygame.time.delay(1000)
pygame.Surface.set_alpha(icon, 255)
screen.blit(icon, (0, 0))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
