import pygame
import sys
import sets
import adjList
import menu

def draw_floyd_button(graph_set, screen):
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
    text = ft.render("floyd", True, col)
    text_rect = text.get_rect()
    text_rect.center = (250, 260)
    screen.blit(text, text_rect)
    return


def draw_dijkstra_button(graph_set, screen):
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
    text = ft.render("dijkstra", True, col)
    text_rect = text.get_rect()
    text_rect.center = (250, 460)
    screen.blit(text, text_rect)
    return


def floyd(graph_set, screen):
    x = 250
    y = 400
    w = 50
    col = (220, 220, 220)
    b_col = (100, 149, 237)
    c_col = (0, 255, 255)
    ft = pygame.font.Font("font/comic.ttf", 28)
    nodes_pos = menu.get_nodes_pos()
    k = graph_set.floyd_k - 1
    if k < graph_set.node_num:
        pygame.draw.circle(screen, b_col, (nodes_pos[k]['x'], nodes_pos[k]['y']), graph_set.node_r, 2)

    num = graph_set.node_num + 1

    x -= num * w * 0.5
    y -= num * w * 0.5
    if graph_set.floyd_finish == False:
        text = ft.render("dis[i][j] = min(dis[i][k] + dis[k][j])", True, col)
    else:
        text = ft.render("finish", True, col)
    text_rect = text.get_rect()
    text_rect.center = (250, y - 100)
    screen.blit(text, text_rect)

    if graph_set.floyd_finish == False:
        s = "k: " + str(graph_set.floyd_k) + "   i: "
        s = s + str(graph_set.floyd_i) + "   j: "
        s = s + str(graph_set.floyd_j)
        text = ft.render(s, True, col)
        text_rect = text.get_rect()
        text_rect.center = (250, y - 50)
        screen.blit(text, text_rect)

    for i in range(0, num):
        for j in range(0, num):
            pygame.draw.rect(screen, col, (x + j * w, y + i * w, w, w), 2)
            if i == 0 and j == 0:
                text = ft.render("dis", True, col)
            elif i == 0:
                text = ft.render(str(j), True, col)
            elif j == 0:
                text = ft.render(str(i), True, col)
            elif graph_set.floyd_dis[i - 1][j - 1] == graph_set.inf:
                if graph_set.floyd_finish == False and i == graph_set.floyd_i and j == graph_set.floyd_j:
                    text = ft.render("inf", True, c_col)
                elif graph_set.floyd_finish == False and j == graph_set.floyd_i and i == graph_set.floyd_j:
                    text = ft.render("inf", True, c_col)
                else:
                    text = ft.render("inf", True, col)
            else:
                if graph_set.floyd_finish == False and i == graph_set.floyd_i and j == graph_set.floyd_j:
                    text = ft.render(str(graph_set.floyd_dis[i - 1][j - 1]), True, c_col)
                elif graph_set.floyd_finish == False and j == graph_set.floyd_i and i == graph_set.floyd_j:
                    text = ft.render(str(graph_set.floyd_dis[i - 1][j - 1]), True, c_col)
                else:
                    text = ft.render(str(graph_set.floyd_dis[i - 1][j - 1]), True, col)

            text_rect = text.get_rect()
            text_rect.center = (x + j * w + 0.5 * w, y + i * w + 0.5 * w)
            screen.blit(text, text_rect)

    if (graph_set.display_count < graph_set.display_interval / 2):
        graph_set.display_count += 1
        return
    if graph_set.floyd_finish == True:
        return
    
    graph_set.display_count = 0
    graph_set.floyd_j += 1
    if graph_set.floyd_j == num:
        graph_set.floyd_i += 1
        graph_set.floyd_j = graph_set.floyd_i + 1
        if graph_set.floyd_i == num - 1:
            graph_set.floyd_i = 1
            graph_set.floyd_j = 2
            graph_set.floyd_k += 1
            if graph_set.floyd_k == num:
                graph_set.floyd_finish = True
                return

    i = graph_set.floyd_i - 1
    j = graph_set.floyd_j - 1
    k = graph_set.floyd_k - 1
    dis = graph_set.floyd_dis[i][k] + graph_set.floyd_dis[k][j]
    if graph_set.floyd_dis[i][j] > dis:
        graph_set.floyd_dis[i][j] = dis
        graph_set.floyd_dis[j][i] = dis


# draw input
def draw_input(graph_set, screen):
    #output message
    col = (220, 220, 220)
    ft = pygame.font.Font("font/comic.ttf", 20)
    text = ft.render("input number of the start point", True, col)
    text_rect = text.get_rect()
    text_rect.center = (250, 310)
    screen.blit(text, text_rect)

    #input bg
    s = pygame.Surface((400, 40))
    s.set_alpha(128)
    s.fill((50, 50, 50))
    screen.blit(s, (50, 340))

    #text_input
    txt = graph_set.txt
    screen.blit(txt.get_surface(), (250, 340))


def dijkstra(graph_set, screen):
    if graph_set.dij_start == -1:
        draw_input(graph_set, screen)
        return

    col = (220, 220, 220)
    b_col = (100, 149, 237)
    x = 250
    y = 400
    w = graph_set.prim_dis[0]
    h = graph_set.prim_dis[1]
    y -= h / 2 * graph_set.node_num
    ft = pygame.font.Font("font/comic.ttf", 24)
    nodes_pos = menu.get_nodes_pos()

    for i in range(0, graph_set.node_num):
        pygame.draw.rect(screen, col, (x - w, y, w, h), 2)
        text = ft.render("dis[" + str(i + 1) + "]", True, col)
        text_rect = text.get_rect()
        text_rect.center = (x - w * 0.5, y + h * 0.5)
        screen.blit(text, text_rect)

        pygame.draw.rect(screen, col, (x, y, w, h), 2)
        if graph_set.dij_node_dis[i] == graph_set.inf:
            text = ft.render("inf", True, col)
        else:
            text = ft.render(str(graph_set.dij_node_dis[i]), True, col)
        text_rect = text.get_rect()
        text_rect.center = (x + w * 0.5, y + h * 0.5)
        screen.blit(text, text_rect)
        y += h

    for i in range(0, graph_set.node_num):
        if i in graph_set.dij_choose:
            pygame.draw.circle(screen, b_col, (nodes_pos[i]['x'], nodes_pos[i]['y']), graph_set.node_r, 2)

    if graph_set.dij_finish == True:
        text = ft.render("finish", True, col)
        text_rect = text.get_rect()
        text_rect.center = (x, y + h * 0.5)
        screen.blit(text, text_rect)

    if graph_set.display_count < graph_set.display_interval:
        graph_set.display_count += 1
        return

    graph_set.display_count = 0

    for i in graph_set.dij_choose:
        for j in graph_set.nodes_edges[i]:
            to = j['to']
            if graph_set.dij_node_dis[to] > graph_set.dij_node_dis[i] + j['len'] + 1:
                graph_set.dij_node_dis[to] = graph_set.dij_node_dis[i] + j['len'] + 1

    mn = graph_set.inf
    p = -1
    for i in range(0, graph_set.node_num):
        if i not in graph_set.dij_choose and graph_set.dij_node_dis[i] < mn:
            mn = graph_set.dij_node_dis[i]
            p = i
    if p != -1:
        graph_set.dij_choose.append(p)
    else:
        graph_set.dij_finish = True

    for j in graph_set.nodes_edges[p]:
        to = j['to']
        if graph_set.dij_node_dis[to] > graph_set.dij_node_dis[i] + j['len'] + 1:
            graph_set.dij_node_dis[to] = graph_set.dij_node_dis[i] + j['len'] + 1


def check_num(graph_set, num):
    if len(num) != 1:
        return
    if (num[0] > graph_set.node_num or num[0] < 0):
        return
    graph_set.dij_start = num[0]
    graph_set.dij_node_dis[num[0]] = 0
    graph_set.dij_choose.append(num[0])


def check_button(graph_set, screen):
    events = pygame.event.get()
    mouse = pygame.mouse.get_pos()

    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if 180 > mouse[0] > 30 and 75 > mouse[1] > 25:
                graph_set.status = 1
                graph_set.floyd_dis.clear()
            if 360 > mouse[0] > 140 and 280 > mouse[1] > 240:
                graph_set.display_SP = 1
            if 360 > mouse[0] > 140 and 480 > mouse[1] > 440:
                graph_set.display_SP = 2

    flag = False
    flag = graph_set.txt.update(events)
    if (flag == True):
        num = menu.strToNum(graph_set.txt.get_text())
        check_num(graph_set, num)


def Short_path(graph_set, screen):
    adjList.back_button(graph_set, screen)
    menu.draw_graph(graph_set, screen)
    if graph_set.display_SP == 0:
        draw_floyd_button(graph_set, screen)
        draw_dijkstra_button(graph_set, screen)
    elif graph_set.display_SP == 1:
        floyd(graph_set, screen)
    else:
        dijkstra(graph_set, screen)

    check_button(graph_set, screen)