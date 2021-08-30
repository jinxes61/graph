import pygame
import menu
import adjList
import sys

def Mst(graph_set, screen):
    adjList.back_button(graph_set, screen)
    menu.draw_graph(graph_set, screen)