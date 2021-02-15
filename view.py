from AStar import AStar, Node
from MinimalPath import minimalPath
import pygame

class eventValues():
    def __init__(self, inicio=False, fin=False, dragged=False, algorithmStart=False):
        self.inicio = inicio
        self.fin = fin
        self.dragged = dragged
        self.algorithmStart = algorithmStart
        self.AlgorithmEnd = False
        self.out=False



class View():

    def __init__(self, screen, map, algorithm):
        self.screen = screen
        self.map = map
        self.values = eventValues()
        self.algorithm = algorithm
        self.Alg = None

        #state = ['startMenu','pickStart','pickEnd','drawWalls','algorithmRunning','end','kill']


    def getIndexByPosition(self,posClick):
        selectedRow = None
        selectedColum = None
        rows = self.map.getNumberOfRows()
        columns = self.map.getNumberOfColums()

        for i in range(columns+1):
            if(selectedColum==None and (i*(self.screen.get_width()/rows) > posClick[0])):
                selectedColum = i-1
                break

        for i in range(rows+1):
            if(selectedRow==None and (i*(self.screen.get_height()/columns) > posClick[1])):
                selectedRow = i-1
                break

        index = (selectedRow,selectedColum)
        return index

    def getStartRetangle(self,posClick):
        inicio = False
        if(self.map.getStart()==None):
            inicio = self.map.setStart(self.getIndexByPosition(posClick))
        else:
            inicio = True
        return inicio

    def getEndRetangle(self,posClick):
        fin = False
        if(self.map.getObjective()==None):
            fin = self.map.setObjective(self.getIndexByPosition(posClick))
        else:
            fin = True
        return fin

    def reestart(self):
        return self.values.out

    def setWallByDrag(self,posClick):
        self.map.setWall(self.getIndexByPosition(posClick))

    def updateOpenRectangles(self,open):
        for node in open:
            self.map.setOpen(node.position)

    def updateClosedRectangles(self,closed):
        for node in closed:
            self.map.setClosed(node.position)

    def updateFinishRectangles(self,path):
        for i in path:
            self.map.setPath(i)

    def getColor(self,rectangle):
        value = self.map.getValue(rectangle)
        color = (0,0,0)
        if value == 'F':
            color = (200,200,200,100)
        elif value == 'W':
        	color = (20,20,20,100)
        elif value == 'S':
        	color = (73, 99, 251,100)
        elif value == 'G':
        	color = (235, 249, 60)
        elif value == 'O':
        	color = (245, 94, 19)
        elif value == 'C':
        	color = (106, 238, 56)
        elif value == 'P':
        	color = (100, 8, 200)
        else:
        	print('error, Value no existente')
        return color


    def drawGrid(self):
        NumberOfColums = self.map.getNumberOfColums()
        NumberOfRows = self.map.getNumberOfRows()
        blockSize = (self.screen.get_width()/NumberOfColums, self.screen.get_height()/NumberOfRows)
        for x in range(NumberOfColums):
            for y in range(NumberOfRows):

                color = self.getColor((y,x))
                rect = pygame.Rect(x*blockSize[0], y*blockSize[1], blockSize[0], blockSize[1])
                pygame.draw.rect(self.screen, color, rect)
                rect = pygame.Rect(x*blockSize[0], y*blockSize[1], blockSize[0], blockSize[1])
                pygame.draw.rect(self.screen, (60, 70, 108,60), rect,1)

    def setAlgorithm(self):
        if self.algorithm == "A*":
            self.Alg = AStar(self.map)
        elif self.algorithm == "MinimalCost":
            self.Alg = minimalPath(self.map)

    def updateEventos(self,event):

        posClick = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.values.inicio==True and self.values.fin==True:
                self.values.dragged = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.values.inicio==False:
                self.values.inicio = self.getStartRetangle(posClick)
            elif self.values.fin==False:
                self.values.fin = self.getEndRetangle(posClick)
            self.values.dragged = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                if self.values.algorithmStart == False and self.values.inicio and self.values.fin:
                    self.values.algorithmStart = True
                    self.setAlgorithm()
                elif self.values.algorithmStart == True and self.values.AlgorithmEnd == True:
                    self.values.out = True

    def viewWork(self,event):
        self.updateEventos(event)
        if(self.values.algorithmStart==False):
            if(self.values.dragged==True):
                posClick = pygame.mouse.get_pos()
                self.setWallByDrag(posClick)
        else:
            if(self.Alg.IsEnd() or self.values.AlgorithmEnd):
                self.updateFinishRectangles(self.Alg.getPath())
                self.values.AlgorithmEnd = True
            else:
                self.Alg.nextStep()
                self.updateOpenRectangles(self.Alg.getOpen())
                self.updateClosedRectangles(self.Alg.getClosed())
        self.screen.fill((0,0,0))
        self.drawGrid()
