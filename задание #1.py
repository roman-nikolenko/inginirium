import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
speed = 0.10
x = 500 // 2
y = 500 // 2

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('да')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    win.fill(BLACK)
    pygame.draw.circle(win, (WHITE), (x, y), 25)

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP]:
        y -= speed
    if keystate[pygame.K_DOWN]:
        y += speed
    if keystate[pygame.K_LEFT]:
        x -= speed
    if keystate[pygame.K_RIGHT]:
        x += speed

    if event.type == pygame.KEYUP:
        x = 500 // 2
        y = 500 // 2

    pygame.display.flip()
    pygame.display.update()