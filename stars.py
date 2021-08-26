import pygame
import random
import sets

star_pos = []

def addStar(graph_set):
    #star num limit
    if len(star_pos) == graph_set.star_num:
        del(star_pos[0])
    star_pos.append({'x': random.randint(0, graph_set.screen_size[0] + 200), 'y': 0})
    print(len(star_pos))

def moving(graph_set):
    # move the stars
    for i in star_pos:
        i['x'] -= graph_set.star_speed
        i['y'] += graph_set.star_speed * 2

def Draw(screen):
    for i in star_pos:
        #get the start pos
        start_x = i['x'] - 30
        start_y = i['y'] + 60

        #from white to black
        for k in range(1, 16):
            #position of the point
            p_x = start_x + 2 * k
            p_y = start_y - 4 * k

            #get color
            star_color = (200 - 10 * k, 200 - 10 * k, 200 - 10 * k)

            pygame.draw.line(screen, star_color, (p_x, p_y), (p_x + 1, p_y - 2), 1)


def drawstar(screen, graph_set):
    #build a new star
    graph_set.star_build += 1;
    if (graph_set.star_build == 300):
        graph_set.star_build = 0
        addStar(graph_set)

    #moving stars
    graph_set.star_mov += 1
    if (graph_set.star_mov == 10):
        graph_set.star_mov = 0
        moving(graph_set)

    Draw(screen)