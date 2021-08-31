import pygame
import menu
import adjList
import sys

def draw_prim_button(graph_set, screen):
    col = (220, 220, 220)
    x = 140
    y = 240
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
    text = ft.render("prim", True, col)
    text_rect = text.get_rect()
    text_rect.center = (250, 260)
    screen.blit(text, text_rect)
    return


def draw_kruskal_button(graph_set, screen):
    col = (220, 220, 220)
    x = 140
    y = 440
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
    text = ft.render("kruskal", True, col)
    text_rect = text.get_rect()
    text_rect.center = (250, 460)
    screen.blit(text, text_rect)
    return


#get shorten pos
def get_shorten_pos(pos1, pos2, r):
    x = pos2[0] - pos1[0]
    y = pos2[1] - pos1[1]
    l = (x * x + y * y) ** 0.5
    x = x * 20 / l;
    y = y * 20 / l;
    ans = []
    ans.append((pos1[0] + x, pos1[1] + y))
    ans.append((pos2[0] - x, pos2[1] - y))
    return ans


chosen_edges = []
#prim
def prim(graph_set, screen):
    col = (220, 220, 220)
    b_col = (100, 149, 237)
    x = 250
    y = 400
    w = graph_set.prim_dis[0]
    h = graph_set.prim_dis[1]
    y -= h / 2 * graph_set.node_num
    ft = pygame.font.Font("font/comic.ttf", 24)
    nodes_pos = menu.get_nodes_pos()

    for i in chosen_edges:
        pos1 = (nodes_pos[i[0]]['x'], nodes_pos[i[0]]['y'])
        pos2 = (nodes_pos[i[1]]['x'], nodes_pos[i[1]]['y'])
        pos = get_shorten_pos(pos1, pos2, 20)
        pygame.draw.aaline(screen, b_col, pos[0], pos[1], 1)

    for i in range(0, graph_set.node_num):
        pygame.draw.rect(screen, col, (x - w, y, w, h), 2)
        text = ft.render("dis[" + str(i + 1) + "]", True, col)
        text_rect = text.get_rect()
        text_rect.center = (x - w * 0.5, y + h * 0.5)
        screen.blit(text, text_rect)

        pygame.draw.rect(screen, col, (x, y, w, h), 2)
        if graph_set.prim_node_dis[i] == graph_set.inf:
            text = ft.render("inf", True, col)
        else:
            text = ft.render(str(graph_set.prim_node_dis[i]), True, col)
        text_rect = text.get_rect()
        text_rect.center = (x + w * 0.5, y + h * 0.5)
        screen.blit(text, text_rect)
        y += h

        if(graph_set.prim_node_dis[i] == -1):
            pygame.draw.circle(screen, b_col, (nodes_pos[i]['x'], nodes_pos[i]['y']), graph_set.node_r, 2)

    cnt = 0
    for i in range(0, graph_set.node_num):
        if (graph_set.prim_node_dis[i] == -1):
            cnt += 1
    if cnt == graph_set.node_num:
        text = ft.render("finish", True, col)
        text_rect = text.get_rect()
        text_rect.center = (x, y + h * 0.5)
        screen.blit(text, text_rect)
    elif graph_set.prim_connected == False:
        text = ft.render("not connected", True, col)
        text_rect = text.get_rect()
        text_rect.center = (x, y + h * 0.5)
        screen.blit(text, text_rect)
    

    if (graph_set.display_count < graph_set.display_interval):
        graph_set.display_count += 1
        return
    
    graph_set.display_count = 0

    mn = graph_set.inf
    temp = (-1, -1)
    for i in range(0, graph_set.node_num):
        if (graph_set.prim_node_dis[i] == -1):
            for j in graph_set.nodes_edges[i]:
                if graph_set.prim_node_dis[j['to']] > j['len'] + 1:
                    graph_set.prim_node_dis[j['to']] = j['len'] + 1
                if graph_set.prim_node_dis[j['to']] != -1 and j['len'] + 1 < mn:
                    mn = j['len'] + 1
                    temp = (i, j['to'])

    if temp[0] != -1:
        graph_set.prim_node_dis[temp[1]] = -1
        chosen_edges.append(temp)
    else:
        graph_set.prim_connected = False


def find(x, graph_set):
    if x == graph_set.fa[x]:
        return x;
    graph_set.fa[x] = find(graph_set.fa[x], graph_set)
    return graph_set.fa[x]

#kruskal
def kruskal(graph_set, screen):
    col = (220, 220, 220)
    b_col = (100, 149, 237)
    c_col = (0, 255, 255)
    nodes_pos = menu.get_nodes_pos()
    ft = pygame.font.Font("font/comic.ttf", 32)

    for i in chosen_edges:
        pos1 = (nodes_pos[i[0]]['x'], nodes_pos[i[0]]['y'])
        pos2 = (nodes_pos[i[1]]['x'], nodes_pos[i[1]]['y'])
        pos = get_shorten_pos(pos1, pos2, 20)
        pygame.draw.aaline(screen, b_col, pos[0], pos[1], 1)

    e = graph_set.check_edge
    if e[0] != -1:
        pos1 = (nodes_pos[e[0]]['x'], nodes_pos[e[0]]['y'])
        pos2 = (nodes_pos[e[1]]['x'], nodes_pos[e[1]]['y'])
        pos = get_shorten_pos(pos1, pos2, 20)
        pygame.draw.aaline(screen, c_col, pos[0], pos[1], 1)
        if graph_set.choose_flag == 2:
            text = ft.render("pass", True, col)
            text_rect = text.get_rect()
            text_rect.center = (250, 400)
            screen.blit(text, text_rect)
        elif graph_set.choose_flag == 1:
            text = ft.render("choose", True, col)
            text_rect = text.get_rect()
            text_rect.center = (250, 400)
            screen.blit(text, text_rect)
    elif graph_set.prim_connected == False:
        text = ft.render("not connected", True, col)
        text_rect = text.get_rect()
        text_rect.center = (250, 400)
        screen.blit(text, text_rect)
    elif len(graph_set.edge_li) == 0:
        text = ft.render("finish", True, col)
        text_rect = text.get_rect()
        text_rect.center = (250, 400)
        screen.blit(text, text_rect)

    if (graph_set.display_count < graph_set.display_interval):
        graph_set.display_count += 1
        return
    
    graph_set.display_count = 0
    if e[0] == -1 and len(graph_set.edge_li) == 0:
        if len(chosen_edges) != graph_set.node_num - 1:
            graph_set.prim_connected = False
        return

    if find(e[0], graph_set) == find(e[1], graph_set):
        pass
    else:
        chosen_edges.append(e)
        graph_set.fa[find(e[0], graph_set)] = find(e[1], graph_set)

    if len(graph_set.edge_li) == 0:
        graph_set.check_edge = (-1, -1)
        return

    graph_set.check_edge = graph_set.edge_li[0]
    del(graph_set.edge_li[0])
    e = graph_set.check_edge

    if find(e[0], graph_set) == find(e[1], graph_set):
        graph_set.choose_flag = 2
    else:
        graph_set.choose_flag = 1


def check_button(graph_set, screen):
    events = pygame.event.get()
    mouse = pygame.mouse.get_pos()

    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if 180 > mouse[0] > 30 and 75 > mouse[1] > 25:
                graph_set.status = 1
                graph_set.prim_node_dis.clear()
                chosen_edges.clear()
                graph_set.fa.clear()
            if 360 > mouse[0] > 140 and 280 > mouse[1] > 240:
                graph_set.display_mst = 1
            if 360 > mouse[0] > 140 and 480 > mouse[1] > 440:
                graph_set.display_mst = 2

def Mst(graph_set, screen):
    adjList.back_button(graph_set, screen)
    menu.draw_graph(graph_set, screen)
    if graph_set.display_mst == 0:
        draw_prim_button(graph_set, screen)
        draw_kruskal_button(graph_set, screen)
    elif graph_set.display_mst == 1:
        prim(graph_set, screen)
    else:
        kruskal(graph_set, screen)
    check_button(graph_set, screen)