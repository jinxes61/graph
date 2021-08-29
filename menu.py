import pygame
import sets
import random
import sys
from test_input import TextInput

#get the length of two points
def xylength(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    return x * x + y * y


#display the num of nodes now and draw the bottom to control
def draw_nodeNums(graph_set, screen):
    col = (220, 220, 220)
    # title
    ft = pygame.font.Font("font/comic.ttf", 32)
    text = ft.render("number of nodes:", True, col)
    text_rect = text.get_rect()
    text_rect.center = (250, 120)
    screen.blit(text, text_rect)

    #number
    ft = pygame.font.Font("font/comic.ttf", 36)
    text = ft.render(str(graph_set.node_num), True, col)
    text_rect = text.get_rect()
    text_rect.center = (250, 180)
    screen.blit(text, text_rect)

    #button
    col = (200, 200, 200)
    b_col = (100, 100, 100)
    surface = pygame.Surface((1080, 720), pygame.SRCALPHA)
    mouse = pygame.mouse.get_pos()

    if graph_set.node_num == 1:
        pygame.draw.circle(screen, b_col, (150, 180), 20, 2)
    else:
        pygame.draw.circle(screen, col, (150, 180), 20, 2)
        if xylength(mouse[0], mouse[1], 150, 180) <= 400:
            pygame.draw.circle(surface, (100, 100, 100, 128), (150, 180), 18)

    if graph_set.node_num == 9:
        pygame.draw.circle(screen, b_col, (350, 180), 20, 2)
    else:
        pygame.draw.circle(screen, col, (350, 180), 20, 2)
        if xylength(mouse[0], mouse[1], 350, 180) <= 400:
            pygame.draw.circle(surface, (100, 100, 100, 128), (350, 180), 18)
    screen.blit(surface, (0, 0))

    # '+' and '-' 
    ft = pygame.font.Font("font/ebrima.ttf", 40)
    if graph_set.node_num == 1:
        text = ft.render("-", True, b_col)
    else:
        text = ft.render("-", True, col)
    text_rect.center = (153, 172)
    screen.blit(text, text_rect)


    if graph_set.node_num == 9:
        text = ft.render("+", True, b_col)
    else:
        text = ft.render("+", True, col)
    text_rect.center = (347, 172)
    screen.blit(text, text_rect)
    return


#draw the botton to add edges
def draw_addEdge(screen):
    col = (220, 220, 220)
    x = 20
    y = 280
    w = 200
    h = 40
    button_pos = (x, y, w, h)

    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        s = pygame.Surface((w - 2, h - 2))
        s.set_alpha(128)
        s.fill((100, 100, 100))
        screen.blit(s, (x + 1, y + 1))
    pygame.draw.rect(screen, col, button_pos, 2)

    # text
    ft = pygame.font.Font("font/comic.ttf", 28)
    text = ft.render("add an edge", True, col)
    text_rect = text.get_rect()
    text_rect.center = (120, 300)
    screen.blit(text, text_rect)


#draw the botton to delete edges
def draw_delEdge(screen):
    col = (220, 220, 220)
    x = 240
    y = 280
    w = 220
    h = 40
    button_pos = (x, y, w, h)

    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        s = pygame.Surface((w - 2, h - 2))
        s.set_alpha(128)
        s.fill((100, 100, 100))
        screen.blit(s, (x + 1, y + 1))
    pygame.draw.rect(screen, col, button_pos, 2)

    # botton
    ft = pygame.font.Font("font/comic.ttf", 28)
    text = ft.render("delete an edge", True, col)
    text_rect = text.get_rect()
    text_rect.center = (350, 300)
    screen.blit(text, text_rect)


# draw input
def draw_input(graph_set, screen):
    #output message
    col = (220, 220, 220)
    ft = pygame.font.Font("font/comic.ttf", 20)
    text = ft.render("please input 3 numbers: node1  node2  length", True, col)
    text_rect = text.get_rect()
    text_rect.center = (250, 350)
    screen.blit(text, text_rect)

    #input bg
    s = pygame.Surface((400, 40))
    s.set_alpha(128)
    s.fill((50, 50, 50))
    screen.blit(s, (50, 380))

    #text_input
    txt = graph_set.txt
    screen.blit(txt.get_surface(), (180, 380))


# draw the nodes on the graph
nodes_pos = []
nodes_edges = []
def draw_nodes(graph_set, screen):
    # num of nodes should be the same with setting
    graph_bg = graph_set.graph_bg
    x = graph_bg[0]
    y = graph_bg[1]
    w = graph_bg[2]
    h = graph_bg[3]

    while len(nodes_pos) > graph_set.node_num:
        del(nodes_pos[-1])
    while len(nodes_pos) < graph_set.node_num:
        xx = random.randint(x + 20, x + w - 20)
        yy = random.randint(y + 20, y + h - 20)
        num = len(nodes_pos)
        nodes_pos.append({'x': xx, 'y': yy, 'num': str(num + 1)})

    #draw
    col = (220, 220, 220)
    ft = pygame.font.Font("font/ebrima.ttf", 24)
    for i in nodes_pos:
        pygame.draw.circle(screen, col, (i['x'], i['y']), graph_set.node_r, 2)
        #Text on the button
        
        text = ft.render(i['num'], True, col)
        text_rect = text.get_rect()
        text_rect.centerx = i['x']
        text_rect.centery = i['y']

        screen.blit(text, text_rect)


# draw the edges between nodes
def draw_edges(graph_set, screen):
    for i in nodes_pos:
        for j in nodes_edges:
            pass
    return


# draw the graph
def draw_graph(graph_set, screen):
    # background of the graph
    graph_bg = graph_set.graph_bg
    x = graph_bg[0]
    y = graph_bg[1]
    w = graph_bg[2]
    h = graph_bg[3]

    s = pygame.Surface((w, h))
    s.set_alpha(128)
    s.fill((50, 50, 50))
    screen.blit(s, (x, y))

    draw_nodes(graph_set, screen)
    

# check if the button is clicked
def check_button(graph_set, screen):
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            graph_set.node_moving = 10
            if xylength(mouse[0], mouse[1], 150, 180) <= 400 and graph_set.node_num > 1:
                graph_set.node_num -= 1
            if xylength(mouse[0], mouse[1], 350, 180) <= 400 and graph_set.node_num < 9:
                graph_set.node_num += 1
            if 220 > mouse[0] > 20 and 320 > mouse[1] > 280:
                graph_set.add_or_del = 1
                graph_set.txt = TextInput()
            if 460 > mouse[0] > 240 and 320 > mouse[1] > 280:
                graph_set.txt = TextInput()
            

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in nodes_pos:
                if xylength(mouse[0], mouse[1], i['x'], i['y']) <= 400:
                    graph_set.node_moving = int(i['num'])

        if (graph_set.node_moving <= graph_set.node_num):
            mov = graph_set.node_moving
            x = graph_set.graph_bg[0]
            y = graph_set.graph_bg[1]
            w = graph_set.graph_bg[2]
            h = graph_set.graph_bg[3]
            if (x + w - 20 > mouse[0] > x + 20 and y + h - 20 > mouse[1] > y + 20):
                nodes_pos[mov - 1]['x'] = mouse[0]
                nodes_pos[mov - 1]['y'] = mouse[1]

    graph_set.txt.update(pygame.event.get())


#display the menu
def Menu(graph_set, screen):
    draw_nodeNums(graph_set, screen)
    draw_graph(graph_set, screen)
    draw_addEdge(screen)
    draw_delEdge(screen)

    if graph_set.add_or_del > 0:
        draw_input(graph_set, screen)

    check_button(graph_set, screen)