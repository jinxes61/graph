import pygame
import sets
import sys


#the surface to draw AList
def draw_al_bg(graph_set, screen):
    graph_bg = graph_set.adjList_pos
    x = graph_bg[0]
    y = graph_bg[1]
    w = graph_bg[2]
    h = graph_bg[3]

    s = pygame.Surface((w, h))
    s.set_alpha(128)
    s.fill((50, 50, 50))
    screen.blit(s, (x, y))


#back button
def back_button(graph_set, screen):
    #button
    col = (220, 220, 220)
    x = 30
    y = 25
    w = 150
    h = 50
    button_pos = (x, y, w, h)

    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        s = pygame.Surface((w - 2, h - 2))
        s.set_alpha(128)
        s.fill((100, 100, 100))
        screen.blit(s, (x + 1, y + 1))
    pygame.draw.rect(screen, col, button_pos, 2)

    # text
    ft = pygame.font.Font("font/comic.ttf", 32)
    text = ft.render("<- back", True, col)
    text_rect = text.get_rect()
    text_rect.x = 50
    text_rect.centery = 50
    screen.blit(text, text_rect)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if 180 > mouse[0] > 30 and 75 > mouse[1] > 25:
                graph_set.status = 1


def draw_node(screen, num, x, y):
    col = (220, 220, 220)
    ft = pygame.font.Font("font/ebrima.ttf", 24)
    pygame.draw.circle(screen, col, (x, y), 20, 2)
    
    #Text    
    text = ft.render(str(num), True, col)
    text_rect = text.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    screen.blit(text, text_rect)
    return (x + 20, y)


#draw an edge
def draw_edge(screen, num1, num2, x, y, lx):
    #init
    col = (220, 220, 220)
    a = 30
    xx = x - a * 1.5
    yy = y - a * 0.5

    #draw line
    pygame.draw.aaline(screen, col, (lx, y), (xx, y), 1)

    #draw rect
    pygame.draw.rect(screen, col, (xx, yy, a, a), 2)
    xx += a
    pygame.draw.rect(screen, col, (xx, yy, a, a), 2)
    xx += a
    pygame.draw.rect(screen, col, (xx, yy, a, a), 2)

    #text
    ft = pygame.font.Font("font/ebrima.ttf", 18)
    text = ft.render(str(num1), True, col)
    text_rect = text.get_rect()
    text_rect.centerx = x - a
    text_rect.centery = y
    screen.blit(text, text_rect)

    text = ft.render(str(num2), True, col)
    text_rect = text.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    screen.blit(text, text_rect)

    return (x + a, y)


#display the adjacent list
def draw_list(graph_set, screen):
    graph_bg = graph_set.adjList_pos
    x = graph_bg[0]
    y = graph_bg[1]
    w = graph_bg[2]
    h = graph_bg[3]

    mx = 0
    for i in graph_set.nodes_edges:
        if len(i) + 1 > mx:
            mx = len(i) + 1

    w = w / mx
    h = h / graph_set.node_num

    lst = []
    for i in range(1, graph_set.node_num + 1):
        xx = x + w * 0.5
        yy = y + i * h - h * 0.5
        lst.append(draw_node(screen, i, xx, yy))

    for i in range(1, graph_set.node_num + 1):
        yy = y + i * h - h * 0.5
        l = len(graph_set.nodes_edges[i - 1])
        for j in range(1, l + 1):
            xx = x + j * w + w * 0.5
            num1 = graph_set.nodes_edges[i - 1][j - 1]['to']
            num2 = graph_set.nodes_edges[i - 1][j - 1]['len']
            lx = lst[i - 1][0]
            lst[i - 1] = draw_edge(screen, num1 + 1, num2 + 1, xx, yy, lx)


def AdjList(graph_set, screen):
    draw_al_bg(graph_set, screen)
    back_button(graph_set, screen)
    draw_list(graph_set, screen)