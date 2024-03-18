import pygame as pg
import os

import pygame.mixer

pg.init()
WIDTH = 800
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("music player")
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# font
font = pg.font.SysFont("arial", 36)
# uploading directory
run = True
dir_mus = "music"
files = [i for i in os.listdir(dir_mus) if i.endswith(".mp3")]
track_i = 0  # current id of music
playing = False
pygame.mixer.music.load(os.path.join(dir_mus, files[track_i]))  # upload


def play():
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def next():
    global track_i
    track_i = (track_i + 1) % len(files)
    pygame.mixer.music.load(os.path.join(dir_mus, files[track_i]))
    if playing:
        pygame.mixer.music.play()


def prev():
    global track_i
    track_i = (track_i - 1) % len(files)
    pygame.mixer.music.load(os.path.join(dir_mus, files[track_i]))
    if playing:
        pygame.mixer.music.play()


while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            if play_button_rect.collidepoint(x, y):
                if playing:
                    stop()
                    playing = False
                else:
                    play()
                    playing = True
            elif prev_button_rect.collidepoint(x, y):
                prev()
            elif next_button_rect.collidepoint(x, y):
                next()
            elif stop_button_rect.collidepoint(x, y):
                playing = False
                stop()

    screen.fill(WHITE)
    play_button = font.render('play', True, BLACK)
    play_button_rect = play_button.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(play_button, play_button_rect)
    prev_button = font.render('prev', True, BLACK)
    prev_button_rect = prev_button.get_rect(center=(WIDTH // 2 - 100, HEIGHT // 2))
    screen.blit(prev_button, prev_button_rect)
    next_button = font.render('next', True, BLACK)
    next_button_rect = next_button.get_rect(center=(WIDTH // 2 + 100, HEIGHT // 2))
    screen.blit(next_button, next_button_rect)
    stop_button = font.render('stop', True, BLACK)
    stop_button_rect = stop_button.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 105))
    screen.blit(stop_button, stop_button_rect)
    pg.display.flip()
pg.quit()
