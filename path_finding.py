import pygame, sys
from mainMenu import mainMenu
from map import Map
from AStar import AStar, Node
from MinimalPath import minimalPath
from view import View, eventValues
import os

pygame.init()

icon = pygame.image.load('./images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Path Finder')

screenSize = (500,500)
screen = pygame.display.set_mode(screenSize)
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 50)
Algorithms = ["A*", "MinimalCost"]
menu = None
view = None
menuEnd = True
algorithmEnd = True
running = True
while running:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == timer_event:
        pass

    if not menuEnd:
        menuEnd = menu.DrawMainMenu(event)
        if menuEnd:
            algorithmEnd=False
            map = Map((30,30))
            view = View(screen,map,Algorithms[menu.algorithmSelected])
    elif not algorithmEnd:
        view.viewWork(event)
        algorithmEnd = view.reestart()
    else:
        menuEnd = False
        algorithmEnd = True
        menu = mainMenu(screen, Algorithms)
        menu.MainMenuConfiguration()


    pygame.display.update()
