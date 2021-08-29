import pygame
import sys
from sets import Settings
import function as fun

def main():
    #init
    pygame.init()
    graph_set = Settings()

    #init screen
    screen = pygame.display.set_mode(graph_set.screen_size)
    pygame.display.set_caption('Graph')
    img = pygame.image.load("img/bg.bmp")

    #init clock
    clock = pygame.time.Clock()

    while(True):
        clock.tick(120)
        fun.check_event(graph_set, screen)
        fun.upd_screen(graph_set, screen, img)


if __name__ == "__main__":
    main()