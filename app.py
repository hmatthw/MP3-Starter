import pygame
from pygame import mixer


pygame.init()
mixer.init()


screen = pygame.display.set_mode((1000, 750))
height = screen.get_height()
width = screen.get_width()
timer = pygame.time.Clock()


pygame.display.set_caption("Free Spotify")
icon = pygame.image.load('ishowspeed.jpg')
pygame.display.set_icon(icon)

WHITE = (255, 255, 255)
color_dark = (100,100,100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#base background
color = 'grey'
screen.fill(color)


#default when no song is being played
nomusic = pygame.transform.smoothscale(
    pygame.image.load('no music loaded icon.jpg').convert_alpha(), (250,250)
)
screen.blit(nomusic, nomusic.get_rect(center=(500,275)))
font1 = pygame.font.SysFont('arial', 20)
text1 = font1.render('No Song Playing', True, (0, 0, 0))
text_rect = text1.get_rect(center=(500, 425))
screen.blit(text1, text_rect)

# button pictures
backpng = pygame.image.load('backwards.png')
fowardpng = pygame.image.load('fowards.png')
playpng = pygame.image.load('play.jpg')

#songs
songs = ["perfect.mp3", "treat.mp3"]
song_index = 0
pygame.mixer.music.load(songs[song_index])
#song pictures
perfectcover = pygame.image.load('perfectcover.jpg')
treatcover = pygame.image.load('treatcover.jpg')

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

paused = False
playing = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #creates the 3 squares
        back = pygame.draw.rect(screen, WHITE, (375, 475, 50, 50))  # centered at (400, 500)
        play = pygame.draw.rect(screen, WHITE, (465, 465, 70, 70))  # centered at (500, 500)
        forward = pygame.draw.rect(screen, WHITE, (575, 475, 50, 50))  # centered at (600, 500)
        #centers the images onto the squares
        screen.blit(back_icon, back_icon.get_rect(center=(400, 500)))
        screen.blit(play_icon, play_icon.get_rect(center=(500, 500)))
        screen.blit(forward_icon, forward_icon.get_rect(center=(600, 500)))

        mouse = pygame.mouse.get_pos()

        #play button function
        if play.collidepoint(mouse):
            pygame.draw.rect(screen,(189,188,188), play)
            screen.blit(play_icon, play_icon.get_rect(center=play.center))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play.collidepoint(mouse):
                if not playing:
                    pygame.mixer.music.play(song_index)
                    screen.blit(perfectcover, perfectcover.get_rect(center=(500,275)))
                    playing = True
                    paused = False
                elif paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else: 
                    pygame.mixer.music.pause()
                    paused = True

        #back button function
        if back.collidepoint(mouse):
            pygame.draw.rect(screen,(189,188,188), back)
            screen.blit(back_icon, back_icon.get_rect(center=back.center))

        #forward button function
        if forward.collidepoint(mouse):
            pygame.draw.rect(screen,(189,188,188), forward)
            screen.blit(forward_icon, forward_icon.get_rect(center=forward.center))


        pygame.display.flip()

pygame.quit()


