import pygame
import sys

#draw title
def draw_title(screen):
    #Title of the program
    ft = pygame.font.Font("font/comic.ttf", 54)
    text = ft.render("Data Structure - Graph", True, (220, 220, 220))

    #Set the position
    text_rect = text.get_rect()
    screen_rect = screen.get_rect()
    text_rect.centerx = screen_rect.centerx
    text_rect.y = 250

    screen.blit(text, text_rect)


#draw the 'start' button
def draw_button(graph_set, screen):
    #get the mouse position
    mouse = pygame.mouse.get_pos()

    #set the size and pos of button
    button_pos = graph_set.button_pos
    screen_rect = screen.get_rect()
    x = button_pos[0]
    y = button_pos[1]
    w = button_pos[2]
    h = button_pos[3]

    #draw button
    pygame.draw.rect(screen, (220, 220, 220), button_pos, 3)
    #mouse on the button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        s = pygame.Surface((w - 4, h - 4))
        s.set_alpha(128)
        s.fill((100, 100, 100))
        screen.blit(s, (x + 2, y + 2))
            
    #Text on the button
    ft = pygame.font.Font("font/comic.ttf", 32)
    text = ft.render("Start!", True, (220, 220, 220))
    
    #Set the position
    text_rect = text.get_rect()
    text_rect.centerx = screen_rect.centerx
    text_rect.y = 450

    screen.blit(text, text_rect)


# check if the button is clicked
def check_button(graph_set, screen):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            #check the mouse position
            button_pos = graph_set.button_pos
            x = button_pos[0]
            y = button_pos[1]
            w = button_pos[2]
            h = button_pos[3]

            mouse = pygame.mouse.get_pos()
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                graph_set.status += 1;

        if event.type == pygame.QUIT:
            sys.exit()
    

#Welcome cover
def wel(graph_set, screen):
    draw_title(screen)
    draw_button(graph_set, screen)
    check_button(graph_set, screen)
