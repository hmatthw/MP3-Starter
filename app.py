import pygame


pygame.init()


screen = pygame.display.set_mode((1080, 720))


pygame.display.set_caption("Free Spotify")
icon = pygame.image.load('ishowspeed.jpg')
pygame.display.set_icon(icon)

#base background
color = ('white')
screen.fill(color)
pygame.display.flip()

change_color = pygame.USEREVENT +1
hovering = pygame.USEREVENT +2

box = pygame.Rect((255,255,50,50))
grow = True

pygame.time.set_timer(change_color, 500)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == change_color:
            if color == 'white':
                screen.fill('white')
                color == 'black'
            elif color == 'black':
                screen.fill('black')
                color == 'white'

        if event.type == hovering:
            if grow:
                box.inflate_ip(3, 3)
                grow = box.width < 75
            else:
                box.inflate_ip(-3, -3)
                grow = box.width < 50

    if box.collidepoint(pygame.mouse.get_pos()):
        pygame.event.post(pygame.event.Event(hovering))

    pygame.draw.rect(screen, "RED", box)
    pygame.display.update()
pygame.quit()
