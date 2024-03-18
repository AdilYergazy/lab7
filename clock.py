import pygame as pg
from datetime import datetime
import time
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
kek = datetime.now()
kek = kek.strftime("%I:%M")
kek = kek.split(':')
print(int(kek[0]))
clock = pg.image.load('/home/aduly/PycharmProjects/dab/mickey/mainclock.png')
leftarm = pg.image.load('/home/aduly/PycharmProjects/dab/mickey/leftarm.png')
rightarm = pg.image.load('/home/aduly/PycharmProjects/dab/mickey/rightarm.png')
# rect
leftarm_rect = leftarm.get_rect(center=(WIDTH // 2, HEIGHT // 2))
rightarm_rect = rightarm.get_rect(center=(WIDTH // 2, HEIGHT // 2))
ratio = clock.get_width() / clock.get_height()
scaled_width = int(HEIGHT * ratio)
scaled_height = HEIGHT
clock = pg.transform.scale(clock, (scaled_width, scaled_height))
# resizing everything
ratio2 = leftarm.get_width() / clock.get_height()
scaled_width2 = int(HEIGHT * ratio2)
scaled_height2 = HEIGHT
leftarm = pg.transform.scale(leftarm, (scaled_width2, scaled_height2))

ratio3 = rightarm.get_width() / clock.get_height()
scaled_width3 = int(HEIGHT * ratio3)
scaled_height3 = HEIGHT
rightarm = pg.transform.scale(rightarm, (scaled_width3, scaled_height3))
clock_rect = clock.get_rect(center=(WIDTH // 2 - 10, HEIGHT // 2))
# angle = -360 / 12 * int(kek[0]) - (360 / 12 / 60) * int(kek[1])
# angle2 = -360 / 60 * int(kek[1])
angle = -3 - 360 / 12 * int(kek[0]) - (360 / 12 / 60) * int(kek[1])
angle2 = -65 - 360 / 60 * int(kek[1])
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    screen.blit(clock, clock_rect)
    rotated_right = pg.transform.rotate(rightarm, angle2)
    rotated_right_rect = rotated_right.get_rect(center=(rightarm_rect.center))
    screen.blit(rotated_right, rotated_right_rect)
    rotated_left = pg.transform.rotate(leftarm, angle)  # change angle
    rotated_left_rect = rotated_left.get_rect(center=(leftarm_rect.center))
    screen.blit(rotated_left, rotated_left_rect)
    time.sleep(0.5)
    pg.display.flip()
    kek = datetime.now()
    kek = kek.strftime("%I:%M")
    kek = kek.split(':')
    angle = -3 - 360 / 12 * int(kek[0]) - (360 / 12 / 60) * int(kek[1])
    angle2 = -65 - 360 / 60 * int(kek[1])