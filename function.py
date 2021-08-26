import pygame
import sys
import stars
from sets import Settings

def check_event(graph_set, screen):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def upd_screen(graph_set, screen, img):
    screen.fill(graph_set.bg_color)
    screen.blit(img, (0, 0))
    stars.drawstar(screen, graph_set)
    pygame.display.flip()

    