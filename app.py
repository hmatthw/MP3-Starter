import pygame
from pygame import mixer

pygame.init()
mixer.init()


screen = pygame.display.set_mode((1000, 750))
timer = pygame.time.Clock()


pygame.display.set_caption("Free Spotify")
icon = pygame.image.load('ishowspeed.jpg')
pygame.display.set_icon(icon)

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#base background
color = 'grey'
screen.fill(color)

font1 = pygame.font.SysFont('arial', 20)
text1 = font1.render('No Song Playing', True, (0, 0, 0))
text_rect = text1.get_rect(center=(500, 425))
screen.blit(text1, text_rect)

#picture when no song is being played
nomusic = pygame.transform.smoothscale(
    pygame.image.load('no music loaded icon.jpg').convert_alpha(), (250,250)
)
screen.blit(nomusic, nomusic.get_rect(center=(500,275)))

# button pictures
backpng = pygame.image.load('backwards.png')
fowardpng = pygame.image.load('fowards.png')
playpng = pygame.image.load('play.jpg')

#makes the size of the images
back_icon = pygame.transform.smoothscale(
    pygame.image.load("backwards.png").convert_alpha(), (35, 35)
)
play_icon = pygame.transform.smoothscale(
    pygame.image.load("play.jpg").convert_alpha(), (50, 50)
)
forward_icon = pygame.transform.smoothscale(
    pygame.image.load("fowards.png").convert_alpha(), (35, 35)
)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #creates the 3 circles
        pygame.draw.circle(screen, WHITE, (400, 500), 25)
        pygame.draw.circle(screen, WHITE, (500, 500), 35)
        pygame.draw.circle(screen, WHITE, (600, 500), 25)
        #puts the images onto the circles
        screen.blit(back_icon, back_icon.get_rect(center=(400, 500)))
        screen.blit(play_icon, play_icon.get_rect(center=(500, 500)))
        screen.blit(forward_icon, forward_icon.get_rect(center=(600, 500)))

        pygame.display.flip()

pygame.quit()
