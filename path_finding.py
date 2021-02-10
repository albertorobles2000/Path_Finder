import pygame, sys
from map import Map
from AStar import astar, Node
import os

map = Map((30,30))


def getIndexByPosition(posClick,screen, n_blocks):
    fila = -1
    columna = -1
    for i in range(n_blocks+1):
        if(columna==-1 and (i*(screen.get_width()/n_blocks) > posClick[0])):
            columna = i-1
        if(fila==-1 and (i*(screen.get_height()/n_blocks) > posClick[1])):
            fila = i-1
        if(fila>=0 and columna>=0):
            index = (fila,columna)
    return index

def getStartAndEndRetangle(posClick,inicio,fin,screen,n_blocks):

    if(inicio==False):
        inicio = True
        map.setStart(getIndexByPosition(posClick,screen,n_blocks))

    elif(fin==False):
        fin = True
        map.setObjective(getIndexByPosition(posClick,screen,n_blocks))
    return inicio, fin

def setWallByDrag(posClick,screen, n_blocks):
    rectangle = getIndexByPosition(posClick,screen,n_blocks)
    map.setWall(rectangle)

def updateOpenRectangles(open):
    for node in open:
        map.setOpen(node.position)

def updateClosedRectangles(closed):
    for node in closed:
        map.setClosed(node.position)

def updateFinishRectangles(path):
    for i in path:
        map.setPath(i)

def getColor(value):
    color = (0,0,0)
    if value == 'F':
        color = (200,200,200,100)
    elif value == 'W':
    	color = (20,20,20,100)
    elif value == 'S':
    	color = (73, 99, 251,100)
    elif value == 'G':
    	color = (242, 123, 46)
    elif value == 'O':
    	color = (245, 94, 19)
    elif value == 'C':
    	color = (106, 238, 56)
    elif value == 'P':
    	color = (100, 8, 200)
    else:
    	print('error, Value no existente')
    return color

def drawGrid(screen, n_blocks):
    blockSize = (screen.get_width()/n_blocks, screen.get_height()/n_blocks)
    for x in range(n_blocks):
        for y in range(n_blocks):

            color = getColor(map.getValue((y,x)))
            rect = pygame.Rect(x*blockSize[0], y*blockSize[1], blockSize[0], blockSize[1])
            pygame.draw.rect(screen, color, rect)
            rect = pygame.Rect(x*blockSize[0], y*blockSize[1], blockSize[0], blockSize[1])
            pygame.draw.rect(screen, (60, 70, 108,60), rect,1)



#os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

icon = pygame.image.load('./images/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Path Finder')

screenSize = (500,500)
minSize = (200,200)
posClick = -1
inicio = False
fin = False
dragged = False
screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE, pygame.FULLSCREEN)
running = True
AlgorithmRunning = False
AlgorithmEnd = False
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 50)
while running:
    #Handle events
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.VIDEORESIZE:
        valor_minimo = screen.get_size()
        screenSize = (max(valor_minimo[0],minSize[0]),max(valor_minimo[1],minSize[1]))
        screen = pygame.display.set_mode(screenSize, pygame.RESIZABLE)
    elif event.type == pygame.VIDEOEXPOSE:  # handles window minimising/maximising
        screen.fill((182,244,238))
        actualSize = screen.get_size()
    elif event.type == pygame.MOUSEBUTTONUP:
        posClick = pygame.mouse.get_pos()
        inicio, fin = getStartAndEndRetangle(posClick,inicio,fin,screen,map.getSize()[0])
        dragged = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        dragged = True
    elif event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RETURN:
            AlgorithmRunning = True
            pathFinding = astar(map)
    elif event.type == timer_event:

        if(AlgorithmRunning==False):
            if(dragged and inicio==True and fin==True):
                posClick = pygame.mouse.get_pos()
                setWallByDrag(posClick,screen, map.getSize()[0])
        else:
            if(pathFinding.IsEnd() or AlgorithmEnd):
                updateFinishRectangles(pathFinding.getPath())
                AlgorithmEnd = True
            else:
                pathFinding.nextStep()
                updateOpenRectangles(pathFinding.getOpen())
                updateClosedRectangles(pathFinding.getClosed())

        drawGrid(screen,map.getSize()[0])
        pygame.display.update()
