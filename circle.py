import pygame as pg
pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("red ball")
run = True
WHITE = (255, 255, 255)
RED = (250, 0, 0)
speed = 20
x, y = 400, 300
radius = 25
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    screen.fill(WHITE)
    pg.draw.circle(screen, RED, ((x, y)), radius, 0)
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x - radius > 0:
        x -= speed
    if keys[pg.K_RIGHT] and radius + x < 800:
        x += speed
    if keys[pg.K_UP] and y - radius > 0:
        y -= speed
    if keys[pg.K_DOWN] and y + radius < 600:
        y += speed
    pg.display.flip()
pg.quit()
