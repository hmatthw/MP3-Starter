import pygame


pygame.init()


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

#album cover / song picture

#forward, backward, play buttons
pygame.draw.circle(screen, WHITE, (400,500), 25) #backwards
pygame.draw.circle(screen, WHITE, (500,500), 35) #play
pygame.draw.circle(screen, WHITE, (600,500), 25) #forwards

backpng = pygame.image.load('backwards.png')
fowardpng = pygame.image.load('fowards.png')
playpng = pygame.image.load('play.jpg')

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

        screen.fill("grey")

        pygame.draw.circle(screen, WHITE, (400, 500), 25)
        pygame.draw.circle(screen, WHITE, (500, 500), 35)
        pygame.draw.circle(screen, WHITE, (600, 500), 25)

        screen.blit(back_icon, back_icon.get_rect(center=(400, 500)))
        screen.blit(play_icon, play_icon.get_rect(center=(500, 500)))
        screen.blit(forward_icon, forward_icon.get_rect(center=(600, 500)))

        pygame.display.flip()

pygame.quit()
