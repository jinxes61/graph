import pygame
import sys
from set import Settings

def check_event(graph_set, screen):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def upd_screen(graph_set, screen):

    screen.fill(graph_set.bg_color)
    pygame.display.flip()