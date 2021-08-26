import pygame
import sys
from set import Settings
import function as fun

def main():
    #init
    pygame.init()
    graph_set = Settings()

    #init screen
    screen = pygame.display.set_mode(graph_set.screen_size)
    pygame.display.set_caption('Graph')

    while(True):
        fun.check_event(graph_set, screen)

        fun.upd_screen(graph_set, screen)


if __name__ == "__main__":
    main()